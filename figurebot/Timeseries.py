from collections import deque
from collections.abc import Iterable
from dateutil import parser
from chest import Chest
import os
from typing import Tuple
import math
from pathlib import PurePath
import pickle
from datetime import datetime
import Timeseries

# === Timeseries ====================================================
# Timeseries is a class desgined to keep a (short) set of data as an
# accessible set of data that will be dynamically resizable. When 
# resizing the Timeseries object, elements will be truncated or added
# automatically (in-order) from the head of the data structure. This
# allows for the data structure to expand and contract to show 
# obvious traces of data truncation and expansion.
# 
# ~Example of resizing~
# Original(20 Elements):                        [----]<0><1><2><3><...><18><19>
# Expanded from original (22 Elements):         <0><0><0><1><2><3><...><18><19>
# Reduced from original (18 Elements):          [----------]<2><3><...><18><19>
# Add 2 elements after reduction (20 Elements): [----------]<4><5><...><20><21>
# ===================================================================

class Timeseries():

    # === Constructors, Destructors, and Properties ====================
    def __init__(self, name, maxLength, location=os.getcwd()):
        assert isinstance(maxLength, int), "\'maxLength\' must be an integer!"
        assert isinstance(location, str) | isinstance(location, PurePath), "\'location\' must be a string or PurePath!"
        assert isinstance(name, str), "\'name\' must be a string!"
        assert maxLength >= 1, "\'maxLength\' must be at-least one!"

        # Private variables
        self.__maxLength = 0
        self.__data = deque([], maxLength)
        self.__name = name
        self.__location = location
        self.__storage = Chest(path=location) # Change dumping/loading method here

        self.maxLength = maxLength
        self.load()

    @property
    def name(self): return self.__name
    @property
    def location(self): return self.__location
    @property
    def storage(self): return self.__storage

    @property
    def maxLength(self):
        assert self.__maxLength == self.__data.maxlen, "Dispairity between self.__maxLength and self.__data.maxlength! This is most likely a bug." # Assert that the value aligns with reality.
        return self.__maxLength
    @maxLength.setter
    def maxLength(self, value):
        assert isinstance(value, int), "\'maxLength\' must be an integer!"
        assert value >= 1, "\'maxLength\' must be greater than or equal to one!"

        # Define initial state
        prevValue = self.__maxLength
        setValue  = value
        delta     = setValue - prevValue
        distance  = abs(delta)

        # Resize Container
        if(delta == 0):  pass
        else:
            oldValues = list(self.__data)
            self.__data = deque(oldValues, setValue)
            for _ in range(delta): self.__data.appendleft(None)
        
        # Reflect changes
        self.__maxLength = setValue

        return self.__maxLength



    # === Public Start ==================================================
    def insert(self, obj=None):
        self.__data.append(obj) # Add the element itself if its not iterable.
        return self
        
    def insertRange(self, iterable=None):
        if(iterable is None): pass
        else:
            for element in iterable: self.__data.append(element)
        return self

    def __repr__(self):
        return self.__data.__repr__()

    def load(self):
        if(self.__name in self.__storage._keys): # If there is something to work with in the storage, then continue on.
            self.insertRange(list(self.__storage[self.__name]))
        else: # If not, save ourselves so that we have something to work with next time.
            self.save()

    def save(self):
        self.__storage[self.__name] = list(self.__data)
        self.__storage.flush()
    
    def RawData(self): return self.__data
        
    def AsList(self): 
        return list(self.__data)

    def AsPlottable(self) -> Tuple[list,list]:
        # [[a,b], [a,b], ..., [a,b]] -> [[a,a...,a], [b,b,...,b]]   
        (x,y) = ([None],[None])
        for elem in self.__data:
            if isinstance(elem, Iterable):
                x.append(datetime.fromtimestamp(elem[0]))
                y.append(elem[1])
        return (x,y)