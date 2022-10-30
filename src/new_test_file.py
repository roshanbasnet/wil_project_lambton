class FileHandlerCSV:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.file_name, 'w') as file:
            file.write(data)

    def append(self, data):
        with open(self.file_name, 'a') as file:
            file.write(data)

    def read_lines(self):
        with open(self.file_name, 'r') as file:
            return file.readlines()

    def write_lines(self, data):
        with open(self.file_name, 'w') as file:
            file.writelines(data)

    def append_lines(self, data):
        with open(self.file_name, 'a') as file:
            file.writelines(data)

    def read_csv(self):
        with open(self.file_name, 'r') as file:
            return csv.reader(file)

    def write_csv(self, data):
        with open(self.file_name, 'w') as file:
            csv.writer(file, data)

    def append_csv(self, data):
        with open(self.file_name, 'a') as file:
            csv.writer(file, data)

    def read_csv_dict(self):
        with open(self.file_name, 'r') as file:
            return csv.DictReader(file)

    def write_csv_dict(self, data):
        with open(self.file_name, 'w') as file:
            csv.DictWriter(file, data)

    def append_csv_dict(self, data):
        with open(self.file_name, 'a') as file:
            csv.DictWriter(file, data)

    def read_json(self):
        with open(self.file_name, 'r') as file:
            return json.load(file)

    def write_json(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

    def append_json(self, data):
        with open(self.file_name, 'a') as file:
            json.dump(data, file)

    def read_pickle(self):
        with open(self.file_name, 'rb') as file:
            return pickle.load(file)

    def write_pickle(self, data):
        with open(self.file_name, 'wb') as file:
            pickle.dump(data, file)

    def append_pickle(self, data):
        with open(self.file_name, 'ab') as file:
            pickle.dump(data, file
