from database.db import DB
from time_helpers import Time

class Foods:
    def store(**data):
        product_provided = False
        
        
        if data['barcode'] and data['product']: 
            product_provided = True
            
            # Insert into products table
            if not DB.Query.value_exists('products', 'product', data['product']) and not DB.Query.value_exists('products', 'barcode', data['barcode']):
                DB.Query.insert_into('proudcts', ['proudct', 'barcode'], [data['product'], data['barcode']])

            # Insert into product_times table
            product_id = DB.Query.fetch_id('products', 'barcode', data['barcode']) or DB.Query.fetch_id('products', 'product', data['product'])
            DB.Query.insert_into('product_times', ['product_id', 'date', 'time', 'datetime'], [product_id, data['date'], data['time'], Time.format_datetime(data['date'], data['time'])])
            
        for ingredient in data['ingredients']:
            
            # Insert into ingredients table
            if not DB.Query.value_exists('ingredients', 'ingredient', data['ingredients']):
                DB.Query.insert_into('ingredients', ['ingredient'], [ingredient])

            # Insert into product_ingredients table
            if product_provided:
                product_id = DB.Query.fetch_id('products', 'barcode', data['barcode']) or DB.Query.fetch_id('products', 'product', data['product'])
                ingredient_id = DB.Query.fetch_id('ingredients', 'ingredient', ingredient)
                DB.Query.insert_into('product_ingredients', ['product_id', 'ingredient_id'], [product_id, ingredient_id])

            # Insert into ingredient_times table
            ingredient_id = DB.Query.fetch_id('ingredients', 'ingredient', ingredient)
            DB.Query.insert_into('ingredient_times', ['ingredient_id', 'date', 'time', 'datetime'], [ingredient_id, data['date'], data['time'], Time.format_datetime(data['date'], data['time'])])

    def update():
        pass

    def delete():
        pass

    def fetch():
        pass

    # def check_barcode(self, barcode):
    #     return any(d.get('barcode') == barcode for d in self.data)
    
    # def ingredients_from_barcode(self, barcode):
    #     for dict in self.data:
    #         if dict['barcode'] == barcode:
    #             return dict['ingredients']
        
    # def product_from_barcode(self, barcode):
    #     for dict in self.data:
    #         if dict['barcode'] == barcode:
    #             return dict['product']

