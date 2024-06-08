from datetime import datetime

from database.db import DB
from database.tables import Tables
from time_helpers import Time
from database.generate import Generate

class SymptomTimes:
    def store(**data):
        if DB.Query.value_exists('symptoms', 'symptom', data['symptom']):
            symptom_id = DB.Query.fetch_id('symptoms', 'symptom', data['symptom'])
            DB.Query.insert_into('symptom_times', ['symptom_id', 'severity', 'date', 'time', 'datetime'], [symptom_id, data['severity'], data['date'], data['time'], Time.format_datetime(data['date'], data['time'])])

    def update(symptom_id: int, **new_data):
        # Expected from new_data: severity, date, time
        print("SymptomTimes.update() called")
        DB.Query.update_by_column('symptom_times', ['symptom_id', 'severity', 'date', 'time'], [symptom_id, new_data['severity'], new_data['date'], new_data['time']], 'symptom_id', symptom_id)

    def delete(id):
        DB.Query.delete_by_column('symptom_times', 'id', id)

    def fetch():
        return DB.Query.query_results("SELECT symptom, severity, date, time FROM symptom_times JOIN symptoms ON symptom_times.symptom_id = symptoms.id")
    
    def fetch_by_date(date: str, return_id:bool=False):
        try:
            datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            raise ValueError

        return DB.Query.query_results(f"SELECT symptom, severity, date, time{', symptom_times.id' if return_id else ''} FROM symptom_times JOIN symptoms ON symptom_times.symptom_id = symptoms.id WHERE date = '{date}' ORDER BY datetime")
    
    def factory(amount):
        for i in range(amount):
            symptom = Generate.symptom()
            severity = Generate.integer(1, 10)
            date = Generate.date()
            time = Generate.time()

            SymptomTimes.store(symptom=symptom, severity=severity, date=date, time=time)

    def reset():
        DB.Query.drop_table('symptom_times')
        Tables.create_symptom_times_table()