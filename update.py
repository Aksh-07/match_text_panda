import os
import pandas as pd


class Update:

    def __init__(self):
        self.all_files_list = os.listdir("all_files/")
        self.all_files_dates = {}
        self.new_files = {}

    def update_data(self, files_data, dates_data):

        for file in self.all_files_list:
            if file not in files_data.keys():
                self.new_files[file] = pd.read_csv(
                    f"all_files/{file}", sep="delimiter", header=None, engine="python"
                ).to_string().lower()

            self.all_files_dates[file] = os.stat(f"all_files/{file}").st_mtime
        for k, v in self.new_files.items():
            files_data[k] = v

        for name, date in self.all_files_dates.items():
            if name in files_data.keys():
                if date not in dates_data.values():
                    files_data[name] = pd.read_csv(
                        f"all_files/{name}", sep="delimiter", header=None, engine="python"
                    ).to_string().lower()

        return files_data
