import requests
import json

from pyhidden import fdc_api_key
from data.init import foods

def get_product_ingredients(barcode):
    if foods.check_barcode(barcode):
        return foods.product_from_barcode(barcode), foods.ingredients_from_barcode(barcode) 
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
                return f"{brandname} {description}", ingredients
            except (IndexError, AttributeError):
                return None, None
        else:
            return None, None
   
        

