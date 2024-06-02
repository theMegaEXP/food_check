from datetime import datetime
from PyQt5.QtCore import QDate, QTime

# DB date format: MM-DD-YYYY
# DB time foramt: H:M AM/PM
# DB datetime format: YYYY-MM-DD HH:MM:SS

class Time:
    def strTime_widgetTime(str_time):
        str_time_parsed = datetime.strptime(str_time, '%I:%M %p')
        widget_time = QTime(str_time_parsed.hour, str_time_parsed.minute)
        return widget_time
    
    def strDate_widgetDate(str_date):
        str_date_parsed = datetime.strptime(str_date, '%m/%d/%Y')
        widget_date = QDate(str_date_parsed.year, str_date_parsed.month, str_date_parsed.day)
        return widget_date

