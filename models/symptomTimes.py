from database.db import DB
from helpers import format_datetime

class SymptomsTimes:
    def create(data):
        symptom_id = DB.Query.fetch_id('symptoms', 'symptom', data['symptom'])
        DB.Query.insert_into('symptom_times', ['symptom_id', 'date', 'time', 'datetime'], [symptom_id, data['date'], data['time'], format_datetime(data['date'], data['time'])])

    def update(old_symptom, new_symptom):
        DB.Query.update_by_column('symptoms', ['symptom'], [old_symptom], 'symptom', new_symptom)

    def delete(symptom):
        pass

    def fetch():
        return DB.Query.query_results("SELECT symptom, date, time FROM symptom_times JOIN symptoms ON symptom_times.symptom_id = symptom.id")