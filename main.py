import pandas as pd
import os

files_list = os.listdir("all_files")

files = {}
for file in files_list:
    data = pd.read_csv(f"all_files/{file}", sep="delimiter", header=None, engine="python").to_string().lower()
    files[file] = data

while True:
    s = input("Enter String to search for: ").lower()
    if s == "quit":
        break
    else:
        for key, value in files.items():
            print(f"Match found in {key}, Total Occurrence: {value.count(s)}")\
                if s in value else print(f"No Match found in {key}")


