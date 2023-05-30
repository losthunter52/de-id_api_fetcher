import json
import os.path
import csv
from .settings import DATASETS_PATH, RESULTS_PATH

def read_file(filename):
    path = DATASETS_PATH + filename

    if os.path.exists(path):
        with open(path, 'r') as reader:
            data = reader.read()
    else:
        raise FileNotFoundError(f"{filename} was not found!")
    
    return json.loads(data)

def write_file(thread_count, archive, rows):

    file = archive.split(".")[0]
    thread = (str(thread_count) + "_threads") if int(thread_count) > 1 else (str(thread_count) + "_thread")
    filename = f"anonimized_data_{thread}_{file}.csv"
    path = RESULTS_PATH + filename
    header = ["thread", "registro", "tempo1", "tempo2", "tempo3", "tempo4", "tempo5"]

    with open(path, 'w', newline='', encoding='utf8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
