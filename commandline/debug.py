import re

from commandline.print import Print
import database.tables as tables
from database.db import DB

def debug():
    Print.bold("You have entered the debug area for the database.")
    print("Type 'exit' to exit. Type 'show' followed by a table to show a table.")
    print("Type 'reset' to reset the database.")
    print("Type 'show' followed by a table name to view a DB table.")
    print("Type -q followed by a query to query the database.")
    Print.orange("WARNING: Editing database tables may break the app!")
    
    while True:
        query_input = input("Command: ")
        
        if query_input == 'exit':
            DB.Operations.close()
            Print.green("Database closed.")
            break

        elif query_input == 'reset':
            DB.Operations.reset()
            tables.create_tables()

        elif re.search(r'^show ([^\s]+)$', query_input):
            table_name = query_input.split(' ')[1]
            
            try:
                DB.View.table(table_name)
            except Exception:
                Print.red(f"Table {table_name} does not exist.")
        
        elif re.search(r'^-q .*', query_input):
            try:
                query = query_input[3::]
                DB.Query.query_print(query)
            except Exception:
                Print.red("This query raised an error.")

        else:
            Print.red("This command is not valid.")