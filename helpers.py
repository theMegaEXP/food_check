from datetime import datetime
import re
import math

def format_datetime(date_str, time_str):
    date = datetime.strptime(date_str, '%m-%d-%Y')
    time = datetime.strptime(time_str, '%I:%M%p')

    combined_datetime =  datetime(date.year, date.month, date.day, time.hour, time.minute)
    formatted_datetime = combined_datetime.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_datetime

def ingredients_to_array(ingredients):
    if ingredients[-1] == '.':
        ingredients = ingredients[:-1]
    return [elem.strip().lower() for elem in re.split(r', |\(|\)|\[|\]', ingredients) if elem != '']

def hour_to_unit(hour):
    if hour > 1 and isinstance(hour, float):
        decimal, integer = math.modf(hour)
        return f"{int(integer)}h {int(decimal * 60)}m"
    elif hour >= 1:
        return f"{hour}h"
    else:
        return f"{int(hour * 60)}m"
    
def calc_time_diff(date1, date2):
    datetime1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    datetime2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    time_diff = abs(datetime1 - datetime2)
    hours_diff = time_diff.total_seconds() / 3600

    return hours_diff

def index_exists(lst: list, index: int):
    try: 
        lst[index]
        return True
    except IndexError:
        return False