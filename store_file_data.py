import os
import pandas as pd


class StoreData:

    def __init__(self):
        self.files_list = os.listdir("all_files")
        self.files = {}
        self.dates = {}

    def store_file_data(self):
        for file in self.files_list:
            self.files[file] = pd.read_csv(f"all_files/{file}", sep="delimiter", header=None,
                                           engine="python").to_string().lower()
            # self.dates[file] = os.path.getmtime(f"all_files/{file}")
            self.dates[file] = os.stat(f"all_files/{file}").st_mtime
        return self.files, self.dates

