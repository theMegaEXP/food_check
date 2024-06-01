from database.db import DB
from database.tables import Tables

class SymptomsAvailable:
    def create(symptom):
        if not DB.Query.value_exists('symptoms', 'symptom', symptom):
            DB.Query.insert_into('symptoms', ['symptom'], [symptom])

    def update(old_symptom, new_symptom):
        DB.Query.update_by_column('symptoms', ['symptom'], [old_symptom], 'symptom', new_symptom)

    def delete(symptom):
        DB.Query.delete_by_column('symptoms', 'symptom', symptom)

    def fetch():
        return DB.Query.fetch_columns('syptoms', ['symptom'])
    
    def reset():
        DB.Query.drop_table('symptoms')
        Tables.create_symptoms_table()
        
