import re

from commandline.print import Print
from database.tables import Tables
from database.db import DB

from models.foods import Foods
from models.ignoredIngredients import IgnoredIngredients
from models.symptomsAvailable import SymptomsAvailable
from models.symptomTimes import SymptomTimes

def debug():
    Print.bold("You have entered the debug area for the database.")
    print("Type 'exit' to exit.")
    print("Type 'reset' to reset the entire database.")
    print("Type 'reset' followed by a table name to reset a DB table.")
    print("Type 'show' followed by a table name to view a DB table.")
    print("Type 'add' followed by a model name and an amount to add testing data.")
    print("Type '-q' followed by a SQL query to query the database.")
    Print.orange("WARNING: Editing database tables may break the app! If this happens type 'reset' to reset the app.")
    
    while True:
        query_input = input("Command: ")
        
        if query_input == 'exit':
            #DB.Operations.close()
            #Print.green("Database closed.")
            break

        elif query_input == 'reset':
            DB.Operations.reset()
            Tables.create_tables()

        elif re.search(r'^reset ([^\s]+)$', query_input):
            table_name = query_input.split(' ')[1]
            method_name = f'create_{table_name}_table'

            try:
                DB.Query.drop_table(table_name)
                getattr(Tables, method_name)() # calls the method to recreate the table
                Print.green(f"Table {table_name} reset.")
            except Exception:
                Print.red(f"Table {table_name} does not exist.")

        elif re.search(r'^show ([^\s]+)$', query_input):
            table_name = query_input.split(' ')[1]
            
            try:
                DB.View.table(table_name)
            except Exception:
                Print.red(f"Table {table_name} does not exist.")

        elif re.search(r'^add [a-zA-Z]+ [0-9]+', query_input):

            try:
                classname = globals()[query_input.split(' ')[1]]
                amount = int(query_input.split(' ')[2])

                if 0 < amount <= 50:
                    Print.blue("Inserting data...")
                    classname.factory(amount)
                    Print.green("Data inserted.")
                else:
                    Print.red("The amount provided must be beetween 1-50")
            except Exception:
                Print.red("That model does not exist.")
        
        elif re.search(r'^-q .*', query_input):
            try:
                query = query_input[3::]
                DB.Query.query_print(query)
            except Exception:
                Print.red("This query raised an error.")

        else:
            Print.red("This command is not valid.")