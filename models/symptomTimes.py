from datetime import datetime

from database.db import DB
from database.tables import Tables
from helpers import format_datetime

class SymptomTimes:
    def store(**data):
        if DB.Query.value_exists('symptoms', 'symptom', data['symptom']):
            symptom_id = DB.Query.fetch_id('symptoms', 'symptom', data['symptom'])
            DB.Query.insert_into('symptom_times', ['symptom_id', 'severity', 'date', 'time', 'datetime'], [symptom_id, data['severity'], data['date'], data['time'], format_datetime(data['date'], data['time'])])

    def update(old_symptom, new_symptom):
        DB.Query.update_by_column('symptoms', ['symptom'], [old_symptom], 'symptom', new_symptom)

    def delete(symptom):
        pass

    def fetch():
        return DB.Query.query_results("SELECT symptom, severity, date, time FROM symptom_times JOIN symptoms ON symptom_times.symptom_id = symptoms.id")
    
    def fetch_by_date(date: str):
        try:
            datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            raise ValueError

        return DB.Query.query_results(f"SELECT symptom, severity, date, time FROM symptom_times JOIN symptoms ON symptom_times.symptom_id = symptoms.id WHERE date = '{date}'")
    
    def reset():
        DB.Query.drop_table('symptom_times')
        Tables.create_symptom_times_table()