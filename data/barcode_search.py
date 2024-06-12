import requests
import json

from pyhidden import fdc_api_key
from models.foods import Foods
from commandline.print import Print

def get_product_ingredients(barcode):
    if Foods.barcode_exists(barcode):
        return Foods.fetch_product_from_barcode(barcode), Foods.fetch_ingredients_from_barcode(barcode)
    
    else:
        url = 'https://api.nal.usda.gov/fdc/v1/foods/search'
        params = {
            'api_key': fdc_api_key,
            'query': barcode,
            'dataType': 'Branded'
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            try: 
                data = json.loads(response.text)
                ingredients = data['foods'][0]['ingredients']
                brandname = data['foods'][0]['brandName']
                description = data['foods'][0]['description']
                return f"{brandname}, {description}", ingredients
            except (IndexError, AttributeError):
                Print.red("Product information could not be found.")
                return None, None
        else:
            Print.red("Response failed.")
            return None, None
   
        

