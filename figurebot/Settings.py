# Import Settings
import configparser
from pathlib import Path
import re

s = configparser.ConfigParser()
s.read("Settings.ini")

# Path config
pac = s["PATH"]
pac.DataDir   = Path(pac["DataDirectory"])
pac.OutputDir = Path(pac["OutputDirectory"])

# General config
gc = s["GENERAL"]
gc.Name        = gc["Name"]
gc.EpochReqStr = gc["EpochRequestString"]

# Connection config
cc = s["CONNECTION"]
cc.Host       = cc["Host"]
cc.Port       = cc.getint("Port")
cc.Username   = cc["Username"]
cc.Passphrase = cc["Passphrase"]

# Sensor-envoy figure and plot config
fc = {}
pc = {}

plotReg = re.compile("ENVOY.SENSOR.F[0-9]+.P[0-9]+")       # Plot regex
figReg = re.compile("(?!.*P[0-9]+)ENVOY\.SENSOR\.F[0-9]+") # Figure regex

figIdReg  = re.compile("F[0-9]+")          # Figure regex
plotIdReg = re.compile("P[0-9]+")          # Plot regex
idReg     = re.compile(".*F[0-9]+P[0-9]+") # Figure-Plot regex

#[ fig1[ plot, plot, plot ], fig2[plot, plot], fig3[plot] ]
for sectionName in s.sections():

    #If we get a match for a figure 
    if figReg.match(sectionName):
        figId = figIdReg.search(sectionName).group() #Parse the figure ID from the file.

        fc[figId] = s[sectionName] #Assign the settings for that figure.
        pc[figId] = {}             #Assign a new collection to sort and contain plot settings

    # If we get a match for a plot
    if plotReg.match(sectionName):  
        figId  = figIdReg.search(sectionName).group()  #Parse the figure ID from the file.
        plotId = plotIdReg.search(sectionName).group() #Parse the plot ID from the file.

        pc[figId][plotId] = s[sectionName] #Assign the settings for that plot.
