from datetime import datetime

from database.db import DB
from database.generate import Generate
from time_helpers import Time

# Tables involved

# ingredients
# products
# product_ingredients
# product_ingredient_times


class Foods:
    def store(**data):
        product_provided = False
        product_id: int
        
        if data['barcode'] or data['product']: 
            product_provided = True

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
                if not DB.Query.value_exists('products', 'product', data['product']):
                    DB.Query.insert_into('products', ['product'], [data['product']])
                product_id = DB.Query.fetch_id('products', 'product', data['product'])
            
        for ingredient in data['ingredients']:
            
            # Insert into ingredients table
            if not DB.Query.value_exists('ingredients', 'ingredient', ingredient):
                DB.Query.insert_into('ingredients', ['ingredient'], [ingredient])

            # Insert into product_ingredient_times table
            ingredient_id = DB.Query.fetch_id('ingredients', 'ingredient', ingredient)
            if product_provided:
                DB.Query.insert_into('product_ingredient_times', ['ingredient_id', 'product_id', 'date', 'time', 'datetime'], [ingredient_id, product_id, data['date'], data['time'], Time.format_datetime(data['date'], data['time'])])
                if not DB.Query.composite_key_exists('product_ingredients', 'product_id', product_id, 'ingredient_id', ingredient_id):
                    DB.Query.insert_into('product_ingredients', ['product_id', 'ingredient_id'], [product_id, ingredient_id])
            else:
                DB.Query.insert_into('product_ingredient_times', ['ingredient_id', 'date', 'time', 'datetime'], [ingredient_id, data['date'], data['time'], Time.format_datetime(data['date'], data['time'])])

    def update():
        pass

    def delete(product_id: int, datetime: str):
        if product_id == None:
            DB.Query.query_operation(f"DELETE FROM product_ingredient_times WHERE datetime = '{datetime}' AND product_id IS NULL")
        else:
            # Delete from product_ingredient_times table
            DB.Query.delete_by_column('product_ingredient_times', 'product_id', product_id)
            
            # Delete from products table
            DB.Query.delete_by_column('products', 'id', product_id)

    def fetch():
        pass

    
    def fetch_by_date(date: str):
        # check date format
        try:
            datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            raise ValueError

        # get product info and ingredients
        query = f"""
                SELECT DISTINCT products.product, products.barcode, product_ingredient_times.date, product_ingredient_times.time, product_ingredient_times.datetime, products.id
                FROM products 
                LEFT JOIN product_ingredient_times ON products.id = product_ingredient_times.product_id
                WHERE product_ingredient_times.date = '{date}'
                ORDER BY product_ingredient_times.datetime
                """
        product_results = DB.Query.query_results(query)

        dictArr = []
        for product in product_results:
            dict = {
                'product': product[0],
                'barcode': product[1],
                'date': product[2],
                'time': product[3],
                'datetime': product[4],
                'ingredients': [],
                'product_id': product[5],
            }
            
            query = f"""
                    SELECT ingredients.ingredient
                    FROM product_ingredient_times
                    JOIN ingredients ON product_ingredient_times.ingredient_id = ingredients.id
                    WHERE product_ingredient_times.product_id = {dict['product_id']}
                        AND product_ingredient_times.datetime = '{dict['datetime']}'
                    """
            ingredient_results = DB.Query.query_results(query)
            dict['ingredients'] = [ingredient[0] for ingredient in ingredient_results]
            dictArr.append(dict)

        # get ingredient info when there is no product
        query = f"""
                SELECT DISTINCT date, time, datetime
                FROM product_ingredient_times
                WHERE product_id IS NULL AND date = '{date}'
                ORDER BY product_ingredient_times.datetime
                """
        product_results = DB.Query.query_results(query)
        
        for product in product_results: 
            #product[0] = datetime
            #product[1] = time
            #product[2] = datetime
            
            query = f"""
                    SELECT DISTINCT ingredients.ingredient
                    FROM ingredients
                    JOIN product_ingredient_times ON ingredients.id = product_ingredient_times.ingredient_id
                    WHERE product_ingredient_times.datetime = '{product[2]}'
                    """
            ingredient_results = DB.Query.query_results(query)

            dict = {
                'product': '',
                'barcode': '',
                'date': product[0],
                'time': product[1],
                'datetime': product[2],
                'ingredients': [ingredient[0] for ingredient in ingredient_results],
                'product_id': None,
            }
            dictArr.append(dict)
            
        return dictArr
    
    def fetch_product_ingredients(pb):
        # pb is either a product name or barcode
        
        query = f"""
                SELECT ingredient
                FROM ingredients
                JOIN product_ingredients ON ingredients.id = product_ingredients.ingredient_id
                JOIN products ON product_ingredients.product_id = products.id
                WHERE product = '{pb}' OR barcode = '{pb}'
                """
        
        return [ingredient[0] for ingredient in DB.Query.query_results(query)]


    def factory(amount):
        for i in range(amount):
            barcode = Generate.barcode()
            ingredients = Generate.ingredients()
            date = Generate.date()
            time = Generate.time()

            Foods.store(product='', barcode=barcode, ingredients=ingredients, date=date, time=time)

    def product_exists(product):
        return DB.Query.value_exists('products', 'product', product)

    def barcode_exists(barcode):
        return DB.Query.value_exists('products', 'barcode', barcode)

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

