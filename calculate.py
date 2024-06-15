from collections import defaultdict
import heapq

from helpers import hour_to_unit
from time_helpers import Time
from database.db import DB
from commandline.print import Print

def all():
    query = """
        SELECT
            symptoms.symptom,
            symptom_times.severity,
            (julianday(symptom_times.datetime) - julianday(product_ingredient_times.datetime)) * 24 AS symptom_delay,
            ingredients.ingredient
        FROM
            symptoms
        JOIN
            symptom_times ON symptoms.id = symptom_times.symptom_id
        JOIN
            product_ingredient_times ON product_ingredient_times.id = symptom_times.symptom_id
        JOIN
            ingredients ON ingredients.id = product_ingredient_times.ingredient_id
        WHERE
            symptom_delay BETWEEN 0 AND 24
        
    """
    
    results = DB.Query.query_results(query)
    
    Print.underline_bold("All data ingredietns that could be causing symptoms within 24 hours.")
    for result in results:
        symptom = result[0]
        severity = result[1]
        delay = hour_to_unit(result[2])
        ingredient = result[3]

        Print.key_value('Symptom', symptom)
        Print.key_value('Severity', severity)
        Print.key_value('Delay', delay)
        Print.key_value('Ingredient', ingredient)
        print()


def likey_symptom_cause(max_results: int=4, delay_times: tuple[float, float, float]=(2.35, 5.42, 24.00), start_date: str='05/14/2024', end_date: str='06/14/2024'):
    #check for incorrect values
    if 0 > max_results >= 10:
        raise Exception("max_results out of range. Must be between 1-10")
    if len(delay_times) > 3:
        raise Exception("delay_times tuple is too large in length.")
    if not Time.is_correct_date_format(start_date):
        raise Exception("start_date is not formatted correctly.")
    if not Time.is_correct_date_format(end_date):
        raise Exception("end_date is not formatted correctly.")
    
    
    symptoms = [symptom[0] for symptom in DB.Query.query_results("SELECT symptom FROM symptoms")]

    results = {}
    for symptom in symptoms:
        symptom_id = DB.Query.fetch_id('symptoms', 'symptom', symptom)
        
        # Get all datetimes associated with the symptom
        query = f"""
                SELECT DISTINCT datetime 
                FROM symptom_times
                WHERE symptom_id = '{symptom_id}'
                """
        symptom_datetimes = [datetime[0] for datetime in DB.Query.query_results(query)]

        # Get most likely ingredient
        all_ingredients = []
        for symptom_datetime in symptom_datetimes:
            query = f"""
                    SELECT ingredient
                    FROM ingredients
                    JOIN product_ingredient_times ON ingredients.id = product_ingredient_times.ingredient_id
                    WHERE (julianday(product_ingredient_times.datetime) - julianday('{symptom_datetime}')) * 24 BETWEEN 0 AND 24
                    """
            
            ingredients = [ingredient[0] for ingredient in DB.Query.query_results(query)]
            all_ingredients.append(ingredients)

        all_ingredient_counts = defaultdict(int)
        for ingredients in all_ingredients:
            for ingredient in ingredients:
                all_ingredient_counts[ingredient] += 1

        if all_ingredient_counts:
            top = heapq.nlargest(3, all_ingredient_counts, key=all_ingredient_counts.get)
            Print.key_value(symptom, ', '.join(top))
            results[symptom] = {}
            results[symptom][hour_to_unit(24)] = top

    return results


