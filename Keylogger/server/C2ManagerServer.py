import socket


class C2Manager:

    def __init__(self):
        self.__C2Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__Server = "127.0.0.1"
        self.__Port = 4444

    def Run(self):
        try:
            self.__C2Sock.bind((self.__Server, self.__Port))  # throws
        except socket.error as error:
            print("[~] C2Manager.Run error: {}".format(error))
            return False
        # Start listening on socket
        self.__C2Sock.listen(1)
        self.__C2ManMainloop()
        return True

    def __C2ManMainloop(self):
        while True:
            # wait to accept a connection - blocking call
            conn, addr = self.__C2Sock.accept()
            print('Connected with ' + addr[0] + ':' + str(addr[1]))

    def __DoHandshake(self):
        if self.C2ManReceive() == "client install":
            self.C2ManSend("ok")

    def C2ManReceive(self):
        buffer = self.__C2Sock.recv(1024)  # does not throw !
        return buffer

    def C2ManSend(self, log):
        self.__C2Sock.sendall(log.encode("ascii"))  # does not throw !

    def GetFileContent(self):
        dylib_data = ""
        while True:
            buffer = self.C2ManReceive()
            if not buffer:
                break
            dylib_data += buffer
        return dylib_data

    def __notify(self):
        self.C2ManSend("Client Run")
