import queue
from threading import Thread


class KeyloggerCallbackWorker:

    def __init__(self):
        self.__WorkerThread = Thread(target=self.__WaitForTasks)
        self.__OpQueue = queue.Queue()

    def Run(self):
        self.__WorkerThread.start()

    def QueueInsertTask(self, task: dict):
        self.__OpQueue.put(task)

    def __ProcessSingleTask(self, arg=None):
        callback_dict = self.__OpQueue.get()
        callback: list = callback_dict["task"]
        pipe = callback_dict["pipe"]

        if arg:
            callback.append(arg)

        if len(callback) > 1:
            args = []
            for i in range(1, len(callback)):
                args.append(callback[i])
            retVal = callback[0](*args)
        else:
            retVal = callback[0]()
        self.__OpQueue.task_done()
        if pipe:
            return retVal

    def __WaitForTasks(self):
        pipeVal = None
        while True:
            retVal = self.__ProcessSingleTask(pipeVal)
            if retVal is not None:
                pipeVal = retVal
