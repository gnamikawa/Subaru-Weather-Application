from Timeseries import Timeseries
from SensorEnvoy import SensorEnvoy
import threading as t
import os
import time
import asyncio
from multiprocessing import Process, freeze_support
import sched, time
import argparse 

import Settings as s

class Application:
    def __init__(self):
        self.__envoys = {}
        self.__parser = argparse.ArgumentParser(description='Create graphs for the Subaru Weather Application.')

        # Add Arguments
        self.__parser.add_argument("-o", "--output", action="store_true", help="Create graphs and output to file.")
        self.__parser.add_argument("-l", "--datalog", action="store_true", help='Download and logs data to files.')

        self.__args = self.__parser.parse_args()

        # Add Envoys
        self.__envoys["SensorEnvoy"] = SensorEnvoy()
 
    @property
    def Config(self): self.__config

    def Execute(self):

        # starttime = time.time()
        # while True:
        #     print("tick")
        #     self.__envoys["SensorEnvoy"].UpdateData()
        #     self.__envoys["SensorEnvoy"].Output()
        #     time.sleep(60.0 - ((time.time() - starttime) % 60.0))

        updatetasks = [t.Thread(target=envoy.UpdateData) for envoy in self.__envoys.values()]
        outputtasks = [t.Thread(target=envoy.Output) for envoy in self.__envoys.values()]

        # Run all udpate taskts together
        if(self.__args.datalog):
            print("=== Running updatetasks =================")
            for utask in updatetasks: utask.start()
            for utask in updatetasks: utask.join()
            print("=== Finished updatetasks =================")
            print()

        # Run all IO operations together
        if(self.__args.output):
            print("=== Running outputtasks =================")
            for otask in outputtasks: otask.start()
            for otask in outputtasks: otask.join()
            print("=== Finished updatetasks =================")
            print()


# === Entrypoint =============================
# try:
# except Exception as e: pass
#     print("Yikes! Something unexpected has occurred...")
#     print(e)
#     exit(1)
if __name__ == '__main__':
    freeze_support()
    Main = Application()
    Main.Execute() # Execute once