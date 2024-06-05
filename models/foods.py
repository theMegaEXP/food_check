from datetime import datetime

from database.db import DB
from database.generate import Generate
from time_helpers import Time

# Tables involved

# ingredients
# products
# product_ingredients
# product_times
# ingredient_times


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
                if not DB.Query.value_exists('products', 'barcode', data['product']):
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
            else:
                DB.Query.insert_into('product_ingredient_times', ['ingredient_id', 'date', 'time', 'datetime'], [ingredient_id, data['date'], data['time'], Time.format_datetime(data['date'], data['time'])])

    def update():
        pass

    def delete(product_id: int, date: str, time: str):
        if product_id == None:
            pass
        else:
            # Delete ingredients
            query = f"""
                    DELETE FROM ingredient_times
                    WHERE ingredient_id IN (SELECT ingredient_id FROM product_ingredients WHERE product_id = {product_id})
                    """
            DB.Query.query_operation(query)

            # Delete from product_times table
            DB.Query.delete_by_column('product_times', 'product_id', product_id)

            # Delete from product_ingredients table
            DB.Query.delete_by_column('product_ingredients', 'product_id', product_id)
            
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
                SELECT products.product, products.barcode, product_times.date, product_times.time , products.id
                FROM products 
                JOIN product_times ON products.id = product_times.product_id
                WHERE product_times.date = '{date}'
                ORDER BY product_times.datetime
                """
        product_results = DB.Query.query_results(query)

        dictArr = []
        for product in product_results:
            dict = {
                'product': product[0],
                'barcode': product[1],
                'date': product[2],
                'time': product[3],
                'ingredients': [],
                'product_id': product[4],
            }
            
            query = f"""
                    SELECT ingredients.ingredient
                    FROM products
                    JOIN product_ingredients ON products.id = product_ingredients.product_id
                    JOIN ingredients ON product_ingredients.ingredient_id = ingredients.id
                    WHERE products.id = {dict['product_id']}
                    """
            ingredient_results = DB.Query.query_results(query)
            dict['ingredients'] = [ingredient[0] for ingredient in ingredient_results]
            dictArr.append(dict)

        # get ingredient info when there is no product
        query = f"""
                SELECT DISTINCT ingredient_times.date, ingredient_times.time, ingredient_times.datetime
                FROM ingredient_times
                WHERE ingredient_times.date = '{date}'
                    AND NOT EXISTS (
                        SELECT 1
                        FROM product_times
                        JOIN product_ingredients ON product_times.product_id = product_ingredients.product_id
                        WHERE product_ingredients.ingredient_id = ingredient_times.ingredient_id
                            AND ingredient_times.datetime = product_times.datetime
                    )
                """
        product_results = DB.Query.query_results(query)
        
        for product in product_results: 
            #product[0] = datetime
            #product[1] = time
            #product[2] = datetime
            
            query = f"""
                    SELECT DISTINCT ingredients.ingredient
                    FROM ingredients
                    JOIN ingredient_times ON ingredients.id = ingredient_times.ingredient_id
                    WHERE ingredient_times.datetime = '{product[2]}'
                    """
            ingredient_results = DB.Query.query_results(query)

            dict = {
                'product': '',
                'barcode': '',
                'date': product[0],
                'time': product[1],
                'ingredients': [ingredient[0] for ingredient in ingredient_results],
                'product_id': None,
            }
            dictArr.append(dict)
            
        return dictArr


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

