import pandas as pd
import os

files_list = os.listdir("all_files")


def store_file_data():
    files = {}
    dates = {}
    for file in files_list:
        files[file] = pd.read_csv(f"all_files/{file}", sep="delimiter", header=None,
                                  engine="python").to_string().lower()
        dates[file] = os.path.getmtime(f"all_files/{file}")
    return files, dates


file_data, date_data = store_file_data()


def update_data(files_data, dates_data):
    all_files_list = os.listdir("all_files/")
    all_files_dates = {}

    new_files = {}
    for file in all_files_list:
        if file not in files_data.keys():
            new_files[file] = pd.read_csv(
                f"all_files/{file}", sep="delimiter", header=None, engine="python"
            ).to_string().lower()

        all_files_dates[file] = os.path.getmtime(f"all_files/{file}")

    for k, v in new_files.items():
        files_data[k] = v

    for name, date in all_files_dates.items():
        if name in files_data.keys():
            if date not in dates_data.values():
                files_data[name] = pd.read_csv(
                    f"all_files/{name}", sep="delimiter", header=None, engine="python"
                ).to_string().lower()

    return files_data


while True:
    s = input("Enter String to search for: ").lower()
    updated_data = update_data(file_data, date_data)
    if s == "quit":
        break
    else:
        for key, value in updated_data.items():
            print(f"Match found in {key}, Total Occurrence: {value.count(s)}") \
                if s in value else print(f"No Match found in {key}")
