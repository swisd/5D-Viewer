import tkinter
from tkinter import *
import time
from plyer import notification
import keyboard
import numpy
import io


IO_ERROR = 631

class linear(object):

    def __main___(self, *args):
        pass

    def list(self, *args):
        pass

    def createModule(self, spec):
        pass

    def createGUI(self, size_x, size_y, vsys):
        tkinter.create(vsys, vsys, vsys, True)

    def draw(self, method, **kwargs):
        pass

    def erase(self):
        pass

    def clear(self):
        pass

    def close(self, mode):
        pass

    def saveToDisk(self, disk, location):
        pass

    def loadFromDisk(self, disk, location):
        f = open(location, "r")
        print(disk, f.read())
        f.close()

    def wait(self, secs):
        time.sleep(secs)

    def reloadFromDisk(self):
        pass

    def saveAll(self, location):
        pass

    def diskData(self):
        pass

    def calculate(self):
        pass

    def recordToDisk(self, arm, location):
        pass

    def IOcontrol(self):
        print(io.__all__)

    def keyTrack(self):
        pass

    def sendNotif(title, message, icon, wait):
         notification.notify(
            title=title,
            message=message,
            app_icon=icon,
            timeout=wait,
         )


"""
    def
        pass

"""
class system(object):

    def sysInfo(self):
        pass

