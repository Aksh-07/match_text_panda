import pandas as pd
import os

files_list = os.listdir("all_files")


def store_file_data():
    files = {}
    for file in files_list:
        files[file] = pd.read_csv(f"all_files/{file}", sep="delimiter", header=None,
                                  engine="python").to_string().lower()
    return files


file_data = store_file_data()


def update_data(files_data):
    all_files_list = os.listdir("all_files/")
    new_files = {}

    for file in all_files_list:
        if file not in files_data.keys():
            new_files[file] = pd.read_csv(
                f"all_files/{file}", sep="delimiter", header=None, engine="python"
            ).to_string().lower()

    for k, v in new_files.items():
        files_data[k] = v
    return files_data


while True:
    s = input("Enter String to search for: ").lower()
    updated_data = update_data(file_data)
    if s == "quit":
        break
    else:
        for key, value in updated_data.items():
            print(f"Match found in {key}, Total Occurrence: {value.count(s)}") \
                if s in value else print(f"No Match found in {key}")
