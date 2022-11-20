import time
import os
import json
from pathlib import Path

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dir_name = os.path.join(parent_dir, "data", "parsed")
output_dir = os.path.join(parent_dir, "data", "stat")

DATA_FILE_NAME = "data.json"
RESULT_FILE_NAME = "day_stat.json"

def get_hours_by_day(data):
  hours_by_day = {}
  for day in data.keys():
    intervals = data[day]

    hours_by_day_in_sec = 0

    for interval in intervals:
      start_point, end_point = interval.split('-')
      full_start_time_obj = time.strptime(
        '{day} {start_point}'.format(day=day, start_point=start_point),
        "%d.%m.%y %H.%M")
      full_end_time_obj = time.strptime(
        '{day} {end_point}'.format(day=day, end_point=end_point),
        "%d.%m.%y %H.%M")

      difference = time.mktime(full_end_time_obj) - time.mktime(
        full_start_time_obj)

      hours_by_day_in_sec += difference

    hours_by_day[day] = time.strftime('%H.%M', time.gmtime(hours_by_day_in_sec))

  return hours_by_day

def day_stat():
    with open(os.path.join(dir_name, DATA_FILE_NAME), "r", encoding="utf-8") as file:
        content = file.read()
        data = json.loads(content)

        Path(output_dir).mkdir(exist_ok=True)
        with open(os.path.join(output_dir, RESULT_FILE_NAME), "w", encoding="utf-8") as result_file:
            result_file.write(json.dumps(get_hours_by_day(data)))

if __name__ == "__main__":
    day_stat()