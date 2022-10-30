import pandas as pd
import os


class Filehandler:

    def __init__(self, path=None, file_name='fetched_data.csv') -> None:
        self.file_name = file_name
        self.path = path

    def write_to_csv(self, data):
        """ Write data to csv 

           Args:
                file_name (str, optional): The file_name to be saved. Defaults to 'fetched_data.csv'

            Returns:
                .csv file: Returns a csv file
        """
        # print(data)
        full_path = os.path.join(self.path, self.file_name)
        # print("File Path:", full_path)
        return data.to_csv(full_path)

    def read_csv_file(self):
        full_path = os.path.join(self.path, self.file_name)
        return pd.read_csv(full_path)
