class DataStorage:
    def __init__(self, file_path):
        self._file_path = file_path
        self.status = "disconnected"
        self.content = None

    def _create_storage(self):
        with open(self._file_path, "w") as file:
            return file

    def connect(self):
        try:
            file = open(self._file_path, "r")
            self.content = file.read()
            file.close()
            self.status = "connected"
        except FileNotFoundError:
            file = self._create_storage()
            self.content = file.read()
            self.status = "connected"
        return file

    def disconnect(self):
        file = open(self._file_path, "a")
        file.close()
        print("File is closed")

class DataStorageWrite(DataStorage):
    def _create_storage(self):
        with open(self._file_path, "a") as file:
            return file

    def connect(self):
        file = super().connect()
        # file.write(self.content)
        # file.close()

    def append(self, text):
        file = open(self._file_path, "a")
        file.write(text)
        file.close()

# Пример использования
data_storage = DataStorageWrite("data.txt")
file = data_storage.connect()
data_storage.append("\nNew data line")
data_storage.disconnect()
