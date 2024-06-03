from database.db import DB
from database.generate import Generate
from time_helpers import Time

# Tables involved

# ingredients
# products
# product_ingredients
# product_times
# symptom_times


class Foods:
    def store(**data):
        product_provided = False
        
        if data['barcode'] or data['product']: 
            product_provided = True
            product_id: int

            # Insert into products table
            if data['barcode'] and data['product']:
                if not DB.Query.value_exists('products', 'product', data['product']) and not DB.Query.value_exists('products', 'barcode', data['barcode']):
                    DB.Query.insert_into('products', ['product', 'barcode'], [data['product'], data['barcode']])
                    product_id = DB.Query.fetch_id('products', 'barcode', data['barcode'])
            elif data['barcode']:
                if not DB.Query.value_exists('products', 'barcode', data['barcode']):
                    DB.Query.insert_into('products', ['barcode'], [data['barcode']])
                    product_id = DB.Query.fetch_id('products', 'barcode', data['barcode'])
            elif data['product']:
                if not DB.Query.value_exists('products', 'barcode', data['product']):
                    DB.Query.insert_into('products', ['product'], [data['product']])
                    product_id = DB.Query.fetch_id('products', 'product', data['product'])

            # Insert into product_times table
            DB.Query.insert_into('product_times', ['product_id', 'date', 'time', 'datetime'], [product_id, data['date'], data['time'], Time.format_datetime(data['date'], data['time'])])
            
        for ingredient in data['ingredients']:
            
            # Insert into ingredients table
            if not DB.Query.value_exists('ingredients', 'ingredient', ingredient):
                DB.Query.insert_into('ingredients', ['ingredient'], [ingredient])

            # Insert into product_ingredients table
            if product_provided:
                ingredient_id = DB.Query.fetch_id('ingredients', 'ingredient', ingredient)
                if not DB.Query.composite_key_exists('product_ingredients', 'product_id', product_id, 'ingredient_id', ingredient_id):
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

    def factory(amount):
        for i in range(amount):
            barcode = Generate.barcode()
            ingredients = Generate.ingredients()
            date = Generate.date()
            time = Generate.time()

            Foods.store(product='', barcode=barcode, ingredients=ingredients, date=date, time=time)

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

