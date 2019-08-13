# Figurebot 📈

Figurebot was created in an Object-Oriented style. Each class represents an object of the system.

The program was built to model a system of foreign relations. The envoys talk to the devices, receive data, and then create graphs based on the obtained data. This program is designed to be able to handle many new systems and additions by defining a new envoy and adding it to the system in the `Application.py` file.

The program is made to record data to the `Data` folder and it will create graphs and throw them into the `Output` Folder.

|Class|Description|
|-|-|
|`Application.py`|The base application. Contains the entry point of the application along with the argument parser.|
|`Envoy.py`|This is an abstract base class for all envoys. This defines the basic functions necessary to be an envoy.|
|`Plotter.py`|This is the class that contains all functions related to creating a graph based on some data.|
|`SensorEnvoy.py`|An envoy. Specialized to talk to the G2cam sensor array. Outputs graphs based on the `Settings.ini` file.|
|`Settings.py`|The central script that controls the settings and their initial conditions.|
|`Timeseries.py`|A datastructure created to keep track of data over time. The data is stored as a window of time, and the number of data never exceeds the specified value in the `Settings.ini` file.|
|`Utility.py`|This class contains utility functions that may serve to be useful throughout the program. It is currently unused.|
