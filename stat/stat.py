import time
import os
import json

from utils import get_hours_by_day_with_empty, get_avarage_day_time_per_day, get_avarage_day_time_per_week
from pathlib import Path

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dir_name = os.path.join(parent_dir, "data", "parsed")
output_dir = os.path.join(parent_dir, "data", "stat")

DATA_FILE_NAME = "data.json"
RESULT_FILE_NAME = "stat.json"

def stat():
    with open(os.path.join(dir_name, DATA_FILE_NAME), "r", encoding="utf-8") as file:
        content = file.read()
        data = json.loads(content)

        data_stat = get_hours_by_day_with_empty(data)
        result = {'average_per_day': get_avarage_day_time_per_day(data_stat), 'average_per_week': get_avarage_day_time_per_week(data_stat), 'data_stat': data_stat}

        Path(output_dir).mkdir(exist_ok=True)
        with open(os.path.join(output_dir, RESULT_FILE_NAME), "w", encoding="utf-8") as result_file:
          result_file.write(json.dumps(result))

if __name__ == "__main__":
    stat()