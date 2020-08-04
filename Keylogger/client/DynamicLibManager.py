from ctypes import *
from sys import platform


class DynamicLibManager:

    @staticmethod
    def LoadDynamicLibrary(dyPath):
        if platform == 'win32':
            try:
                cdll.LoadLibrary(dyPath)
            except WindowsError:
                print("Error %d when loading dll %s" % GetLastError(), dyPath)
        if platform == 'darwin':
            try:
                cdll.LoadLibrary(dyPath)
            except OSError:
                print("Error when loading dylib %s" % dyPath)

