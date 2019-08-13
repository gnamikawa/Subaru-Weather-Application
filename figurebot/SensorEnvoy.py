import os.path
import os
import gc
import copy
import csv
import asyncio
import json
import itertools
import numpy as np
import Utility as u
import Settings as s
import datetime as dt
import matplotlib as mpl
import multiprocessing as mp
import matplotlib.dates as mdates
import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker
from numpy import nan
from Envoy import Envoy
from numpy import linspace
from cycler import cycler
from typing import Dict, List, Sequence, Tuple
from typing import NewType
from pathlib import Path
from Plotter import Plotter
from itertools import product
from matplotlib import cm
from Timeseries import Timeseries
from matplotlib.cm import get_cmap
from collections.abc import Iterable
from g2cam.status.client import StatusClient

class SensorEnvoy(Envoy):

    def __init__(self):
        self.__Name = s.gc.Name
        self.__Storage = {}
        self.__RecentData = {}
        self.__Artists = {}
        self.__StatusClient = StatusClient(
            host     = s.cc.Host,
            port     = s.cc.Port,
            username = s.cc.Username,
            password = s.cc.Passphrase
        )

        self.InitializeStorage()
        self.InitializePlotters()

    def InitializeStorage(self):
        for CollectionKey, ConfigCollection in zip(s.pc.keys(), s.pc.values()):
            for ConfigKey, PlotConfig in zip(ConfigCollection.keys(), ConfigCollection.values()):
                Label           = CollectionKey + ConfigKey
                PlotGranularity = PlotConfig.getint("Granularity")
                Datapath        = s.pac.DataDir

                self.__Storage[Label] = Timeseries(Label, PlotGranularity, Datapath)

    def InitializePlotters(self):
        for CollectionKey in s.pc.keys(): # Each pc-collection key is directly correspondant to the fc key
            Config          = s.fc[CollectionKey] # Grab the figure-configuration using the plot-collection keys.
            OutputDirectory = s.pac.OutputDir

            self.__Artists[CollectionKey] = Plotter(CollectionKey, Config, OutputDirectory) # Make a plotting object based on config for a figure and its save director

    def DataSnapshot(self):
    
        JsonText     = json.dumps(self.__RecentData)
        snapshotPath = s.pac.DataDir / "SensorDump.json"

        with open(snapshotPath, "w+") as file:
            file.write(JsonText )
            
    def FetchData(self):
        try:
            # Define each request with its definition in the config file and initialize its value with "None"
            EpochReqStr = s.gc["EpochRequestString"]
            PlotConfig  = s.pc
            RecentData  = {}
            Request     = {}

            # Create an empty request object
            Request[EpochReqStr] = None
            for ConfigCollection in PlotConfig.values():
                for Config in ConfigCollection.values():
                    RequestString = Config["RequestString"]
                    Request[RequestString] = None

            # Send fetch request
            self.__StatusClient.connect()
            self.__StatusClient.fetch(Request)
            
            for CollectionKey, ConfigCollection in zip(PlotConfig.keys(), PlotConfig.values()):
                RecentData[CollectionKey] = {}
                for ConfigKey, PlotConfig in zip(ConfigCollection.keys(), ConfigCollection.values()):
                    RequestString = PlotConfig["RequestString"]

                    RecentData[CollectionKey][ConfigKey] = {}

                    RecentData[CollectionKey][ConfigKey]["Value"] = Request[RequestString]
                    RecentData[CollectionKey][ConfigKey]["Label"] = PlotConfig["Label"]
                    RecentData[CollectionKey][ConfigKey]["RequestString"] = RequestString
            
            RecentData["Epoch"] = {}
            RecentData["Epoch"]["RequestString"] = EpochReqStr
            RecentData["Epoch"]["Value"] = Request[EpochReqStr]

            self.__RecentData = RecentData
            return self.__RecentData

        except ValueError as e:
            print(e)
            print("Error: Could not fetch new data!")

    def UpdateData(self):
        Data        = self.FetchData()
        Epoch       = Data["Epoch"]["Value"]

        
        print(f"Updating SensorData...")
        for CollectionKey, ConfigCollection in zip(s.pc.keys(), s.pc.values()):
            for ConfigKey, PlotConfig in zip(ConfigCollection.keys(), ConfigCollection.values()):
                Label         = CollectionKey + ConfigKey
                DataEntry     = [ Epoch, Data[CollectionKey][ConfigKey] ]

                self.__Storage[Label].insert( DataEntry )
                self.__Storage[Label].save()
        print(f"Finished updating SensorData.")

    def Output(self):
        # Each pc-collection key is directly correspondant to the fc key

        # l = []    

        for ckey, plotCollection in zip(s.pc.keys(), s.pc.values()) :
            artist      = self.__Artists[ckey]
            plotConfigs = s.pc[ckey]
            datasets = {}
            for pkey in plotCollection.keys():
                d = self.__Storage[ckey + pkey]
                datasets[ckey + pkey] = d.AsPlottable()
            artist.Plot(ckey, plotConfigs, datasets)
            # l.append( (ckey, plotConfigs, datasets) )

        # with mp.Pool(processes=mp.cpu_count()) as pool:
        #     pool.starmap(artist.Plot, l)

        self.DataSnapshot()