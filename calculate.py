from helpers import hour_to_unit
from database.db import DB
from commandline.print import Print


class Results:

    def all():
        query = """
            SELECT
                symptoms.symptom,
                symptom_times.severity,
                (julianday(symptom_times.datetime) - julianday(ingredient_times.datetime)) * 24 AS symptom_delay,
                ingredients.ingredient
            FROM
                symptoms
            JOIN
                symptom_times ON symptoms.id = symptom_times.symptom_id
            JOIN
                ingredient_times ON ingredient_times.id = symptom_times.symptom_id
            JOIN
                ingredients ON ingredients.id = ingredient_times.ingredient_id
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


    def likey_symptom_cause():
        query = """
            SELECT
                symptoms.symptom,
                (
                    SELECT
                        ingredients.ingredient
                    FROM
                        symptoms AS s
                    JOIN
                        symptom_times AS st ON s.id = st.symptom_id
                    JOIN
                        ingredient_times AS it ON it.id = st.symptom_id
                    JOIN
                        ingredients ON ingredients.id = it.ingredient_id
                    WHERE
                        s.id = symptoms.id 
                        AND 
                        (julianday(st.datetime) - julianday(it.datetime)) * 24 BETWEEN 0 AND 24 
                        AND 
                        ingredients.ingredient NOT IN (SELECT ingredient FROM ignored_ingredients)
                    GROUP BY
                        ingredients.id
                    ORDER BY
                        COUNT(*) * AVG(st.severity) DESC
                    LIMIT
                        1
                ) AS top_ingredient
            FROM
                symptoms;
        """
        results = DB.Query.query_results(query)
        
        Print.underline_bold("Most likely ingredient to be causing each symptom.")
        for result in results:
            symptom = result[0].title()
            ingredient = result[1] if result[1] != None else 'N/A'

            Print.key_value(symptom, ingredient)

