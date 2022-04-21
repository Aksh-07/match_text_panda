from store_file_data import StoreData
from update import Update

store_data = StoreData()
file_data, date_data = store_data.store_file_data()

while True:
    s = input("Enter String to search for: ").lower()
    update = Update()
    updated_data = update.update_data(file_data, date_data)
    if s == "quit":
        break
    else:
        for key, value in updated_data.items():
            print(f"Match found in {key}, Total Occurrence: {value.count(s)}") \
                if s in value else print(f"No Match found in {key}")
