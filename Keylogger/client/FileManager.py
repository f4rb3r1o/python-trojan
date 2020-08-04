

class FileManager:

    @staticmethod
    def WriteFile(FilePath, buffer):
        with open(FilePath, "a") as file:
            file.write(buffer)

    @staticmethod
    def ReadFile(FilePath):
        with open(FilePath, "r") as file:
            return file.read()
