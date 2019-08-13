from datetime import datetime
from pathlib import Path
import Settings as s
import Utility as u
import numpy as np
import os
import gc

import Timeseries

class Plotter:

    # We need to keep count of the number of instances of figure plots 
    # in Matplotlib because of their (questionable) implementation for 
    # plotting. (static)    


    def __init__(self, figureId, config, outputDir):
        self.__Config         = config
        # self.__InstanceId     = None
        self.__Savepath       = Path(outputDir / self.__Config["Title"])
        self.__FigureId       = figureId

        # self.Configure()

    def Id(figureId, plotId): f"F{figureId}P{plotId}" if plotId is not None else f"F{figureId}"
    def ConfName(setting, figureId, plotId = None): f"{Id(figureId, plotId)}{setting}"
    def FigureName(config, figId): config[str(figId) + "Title"]
    def Plot(self, figureId, plotConfigs, datasets):
        import matplotlib as mpl

        mpl.use('Agg')

        print(f"Opened plot[{figureId}]...")

        assert len(datasets) > 0, "There must have be least one dataset to plot!"
        assert len(datasets) == len(plotConfigs) , "The configurations and datasets must match in size!"

        sizeConfig       = [ self.__Config.getfloat("sizex"), self.__Config.getfloat("sizey") ]
        resolutionConfig = self.__Config.getfloat("dpi")
        title            = self.__Config["Title"]
        titlefontsize    = self.__Config["TitleFontSize"]
        xlabel           = self.__Config["XAxisLabel"]
        ylabel           = self.__Config["YAxisLabel"]
        dateformat       = self.__Config["DateFormat"]
        gridenabled      = True

        Figure = mpl.pyplot.figure(figsize=sizeConfig, dpi=resolutionConfig)

        Figure.suptitle(title, fontsize=titlefontsize)

        plot = mpl.pyplot.subplot()

        # Plot Config
        plot.xaxis.set_major_locator(mpl.ticker.AutoLocator())
        plot.yaxis.set_minor_locator(mpl.ticker.AutoLocator())
        plot.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(4))
        plot.yaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(4))
        plot.xaxis.set_major_formatter(mpl.dates.DateFormatter(dateformat))
        plot.grid(gridenabled)
        plot.set_xlabel(xlabel, fontsize=9)
        plot.set_ylabel(ylabel, fontsize=9)

        # Automatically choose a color for each plot in the graph.
        start     = 0.0
        stop      = 1.0
        colornum  = len(datasets)
        clrspace  = np.linspace(start, stop, colornum) 

        colors = [ mpl.cm.jet(x) for x in clrspace ]

        def FilterNone(L): return [x for x in L if x is not None]

        for plotConfig, dataset, color in zip(plotConfigs.values(), datasets.values(), colors):
            dates = mpl.dates.date2num(FilterNone(dataset[0]))
            values = [data["Value"] for data in FilterNone(dataset[1])]
            mpl.pyplot.plot(dates, values, color=color, label=plotConfig["Label"])

        # savepath = Path(u.ensureDir(s.pac.OutputDir)) # figconfig["figtitle"] + ".png"))

        mpl.pyplot.legend(loc='best')
        savepath = os.path.abspath(Path(u.ensureDir(s.pac.OutputDir / (self.__Config["Title"] + ".png"))))
        mpl.pyplot.savefig(savepath, format="png", bbox_inches="tight")

        mpl.pyplot.clf()
        mpl.pyplot.cla()
        mpl.pyplot.close()
        # gc.collect()
        print(f"Closed plot[{figureId}]...")

        return self
    