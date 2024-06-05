from database.db import DB
from commandline.print import Print
import inspect

class Tables:
    def create_tables():
        current_method = inspect.currentframe().f_code.co_name

        for name, method in inspect.getmembers(Tables, predicate=inspect.isfunction):
            if name != current_method:
                method()

        Print.green("Database tables created.")

    def create_ingredients_table():
        DB.Query.create_table('ingredients', ['id INTEGER PRIMARY KEY', 
                                            'ingredient TEXT UNIQUE'])
        
    def create_product_ingredient_times_table():
        DB.Query.create_table('product_ingredient_times', ['id INTEGER PRIMARY KEY',
                                                'ingredient_id INTEGER',
                                                'product_id INTEGER NULL',
                                                'date TEXT NULL',
                                                'time TEXT NULL',
                                                'datetime TEXT',
                                                'FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)',
                                                'FOREIGN KEY (product_id) REFERENCES products(id)'])

    def create_products_table():
        DB.Query.create_table('products', ['id INTEGER PRIMARY KEY', 
                                        'product TEXT UNIQUE', 
                                        'barcode TEXT UNIQUE'])

    def create_symptoms_table():
        DB.Query.create_table('symptoms', ['id INTEGER PRIMARY KEY', 
                                        'symptom TEXT UNIQUE'])

    def create_symptom_times_table():
        DB.Query.create_table('symptom_times', ['id INTEGER PRIMARY KEY', 
                                                'symptom_id INTEGER', 
                                                'severity INTEGER CHECK(severity >= 1 AND severity <= 10)',
                                                'date TEXT NULL',
                                                'time TEXT NULL',
                                                'datetime TEXT',
                                                'FOREIGN KEY (symptom_id) REFERENCES symptoms(id)'])

    def create_ignored_ingredients_table():   
        DB.Query.create_table('ignored_ingredients', ['id INTEGER PRIMARY KEY',
                                                    'ingredient TEXT'])
    
    

