from abc import ABC

class Envoy(ABC):

    def __init__(self) -> None: 
        self.__name:str = None
    
    @property
    def name(self): return self.__Name

    def UpdateData(self) -> None: pass
    def Output(self) -> None: pass