import numpy as np
import time

def fill_empty_days(day, keys, hours_by_day):
  sec_in_one_day = 60 * 60 * 24
  day_time_obj = time.strptime(day, "%d.%m.%y")

  if keys.index(day) != 0:
    previous_day = keys[keys.index(day) - 1]
    previous_day_time_obj = time.strptime(previous_day, "%d.%m.%y")
    
    previous_day_time_sec = time.mktime(previous_day_time_obj)
    difference_in_sec = time.mktime(day_time_obj) - previous_day_time_sec

    while difference_in_sec > sec_in_one_day:
      next_day = previous_day_time_sec + sec_in_one_day
      hours_by_day[time.strftime("%d.%m.%y", time.localtime(next_day))] = "0.0"
      difference_in_sec = difference_in_sec - sec_in_one_day
      previous_day_time_sec = next_day

  return hours_by_day


def get_hours_by_day_with_empty(data):
  hours_by_day = {}

  keys = list(data.keys())

  for day in keys:

    intervals = data[day]

    hours_by_day = fill_empty_days(day, keys, hours_by_day)

    hours_by_day_in_sec = 0

    for interval in intervals:
      start_point, end_point = interval.split('-')
      full_start_time_obj = time.strptime(
        '{day} {start_point}'.format(day=day, start_point=start_point),
        "%d.%m.%y %H.%M")
      full_end_time_obj = time.strptime(
        '{day} {end_point}'.format(day=day, end_point=end_point),
        "%d.%m.%y %H.%M")

      difference = time.mktime(full_end_time_obj) - time.mktime(full_start_time_obj)

      hours_by_day_in_sec += difference

    hours_by_day[day] = time.strftime('%H.%M', time.localtime(hours_by_day_in_sec))

  return hours_by_day

def get_avarage_day_time_per_day(day_stat):
  hours_by_day = []

  keys = list(day_stat.keys())

  for day in keys:

    hours, mins = day_stat[day].split('.')

    hours_num = int(hours) + int(mins) / 60
    if hours_num != 0:
      hours_by_day.append(hours_num)

  result = np.array(hours_by_day).mean()
  return round(result, 2)


def get_avarage_day_time_per_week(day_stat):
  hours_by_week = {}

  keys = list(day_stat.keys())

  for day in keys:

    day_time_obj = time.strptime(day, "%d.%m.%y")

    week_name = str(day_time_obj.tm_yday // 7) + "_" + str(
      day_time_obj.tm_year)

    hours, mins = day_stat[day].split('.')
    hours_num = int(hours) + int(mins) / 60

    if week_name in hours_by_week:
      hours_by_week[week_name] += hours_num
    else:
      hours_by_week[week_name] = hours_num

  result = np.array(list(hours_by_week.values())).mean()
  return round(result / 5, 2)