from database.db import DB
from database.tables import Tables
from database.generate import Generate

class SymptomsAvailable:
    def store(symptom):
        if not DB.Query.value_exists('symptoms', 'symptom', symptom):
            DB.Query.insert_into('symptoms', ['symptom'], [symptom])

    def update(old_symptom, new_symptom):
        DB.Query.update_by_column('symptoms', ['symptom'], [old_symptom], 'symptom', new_symptom)

    def delete(symptom):
        symptom_id = DB.Query.fetch_id('symptoms', 'symptom', symptom)
        if not DB.Query.value_exists('symptom_times', 'symptom_id', symptom_id):
            DB.Query.delete_by_column('symptoms', 'symptom', symptom)
            return True
        return False

    def fetch():
        return DB.Query.fetch_columns('symptoms', ['symptom'])
    
    def exists(symptom: str):
        return DB.Query.value_exists('symptoms', 'symptom', symptom)
    
    def factory(amount):
        for i in range(amount):
            SymptomsAvailable.store(Generate.symptom())
    
    def reset():
        DB.Query.drop_table('symptoms')
        Tables.create_symptoms_table()
        
