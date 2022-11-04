import os
import json

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dir_name = os.path.join(parent_dir, "data", "dirty")
output_dir = os.path.join(parent_dir, "data", "parsed")

DATE_SEPARATOR = ":"
FILE_NAME = "data"
FILE_NAME_TXT = FILE_NAME + ".txt"
FILE_NAME_JSON = FILE_NAME + ".json"

def parser():
    with open(os.path.join(dir_name, FILE_NAME_TXT), "r", encoding="utf-8") as file:
        clean_file = file.read().strip().splitlines()
        dirty_data = {}

        for line in clean_file:
            if line: 
                date = ""
                time_lines = []
                if DATE_SEPARATOR in line:
                    date = line.split(DATE_SEPARATOR)[0]
                    dirty_data[date] = []
                else:
                    last_date = list(dirty_data.keys())[-1]
                    dirty_data[last_date].append(line)

        with open(os.path.join(output_dir, FILE_NAME), "w", encoding="utf-8") as result_file:
            result_file.write(json.dumps(dirty_data))

if __name__ == "__main__":
    parser()