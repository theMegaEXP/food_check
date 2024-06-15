from datetime import datetime
from PyQt5.QtCore import QDate, QTime

# DB date format: MM/DD/YYYY
# DB time foramt: H:M AM/PM
# DB datetime format: YYYY-MM-DD HH:MM:SS

class Time:

    def format_datetime(date_str: str, time_str: str):
        date = datetime.strptime(date_str, '%m/%d/%Y')
        time = datetime.strptime(time_str, '%I:%M %p')

        combined_datetime =  datetime(date.year, date.month, date.day, time.hour, time.minute)
        formatted_datetime = combined_datetime.strftime('%Y-%m-%d %H:%M:%S')

        return formatted_datetime

    def strTime_widgetTime(str_time: str):
        str_time_parsed = datetime.strptime(str_time, '%I:%M %p')
        widget_time = QTime(str_time_parsed.hour, str_time_parsed.minute)
        return widget_time
    
    def strDate_widgetDate(str_date: str):
        str_date_parsed = datetime.strptime(str_date, '%m/%d/%Y')
        widget_date = QDate(str_date_parsed.year, str_date_parsed.month, str_date_parsed.day)
        return widget_date
    
    def is_correct_date_format(date: str):
        try:
            datetime.strptime(date, '%m/%d/%Y')
            return True
        except Exception:
            return False

