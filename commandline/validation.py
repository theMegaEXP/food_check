import re
from datetime import datetime
from commandline.print import Print

class Validate:
    def integer(num_start, num_end):
        while True:
            int_input = input("Command: ")
            if not int_input.isdigit():
                Print.red("You must enter a number here.")
            elif int(int_input) < num_start or int(int_input) > num_end:
                Print.red("The number you entered does not have a coresponding command.")
            else:
                return int(int_input)
            
    def confirmation(ask = ''):
        while True:
            confirm_input = input(f"{ask} ('yes'/'no'): ")
            if confirm_input == 'yes':
                return True
            elif confirm_input == 'no':
                return False
            else:
                Print.red("Please enter 'yes', or 'no'.")
    
    def barcode(allow_blank):
        while True:
            barcode_input = input("Barcode: ")

            if barcode_input == '' and allow_blank:
                return 'N/A'
            if len(barcode_input) != 12:
                Print.red("This barcode is invalid since it is not 12 digits")
            elif not barcode_input.isdigit():
                Print.red("This barcode is not a number.")
            else:
                return barcode_input

    def product():
        product_input = input("Product name: ")
        if product_input == '':
            return 'N/A'
        return product_input    

    def ingredients():
        while True:
            ingredients_input = input("Ingredients: ")
            ingredients = [elem.lower() for elem in ingredients_input.split(', ')]   

            if len(ingredients) == 1 and len(ingredients[0]) == 0:
                Print.red("You did not enter any ingredients.")
            elif len(ingredients) == 1 and len(ingredients[0]) > 20:
                Print.red("It looks like you didn't seperate your values correctly.")
            else:
                return ingredients, ingredients_input
    
    def date():
        date_format = '%m-%d-%Y'
        while True:
            date_input = input("Enter date (MM-DD-YYYY) [enter nothing for today's date]: ") or datetime.today().strftime(date_format)

            try:
                formatted = datetime.strptime(date_input, date_format)
                if formatted > datetime.now():
                    Print.red("You cannot enter a date into the future.")
                elif formatted.year != datetime.now().year:
                    Print.red("You cannot enter a date form the previous year.")
                else:
                    return formatted.strftime(date_format)
            except ValueError:
                Print.red("The date entered is invalid.")

    def time():
        time_format = '%I:%M%p'
        while True:
            time_input = input("Enter time (like this - 2:05AM) [enter nothing for the current time]: ") or datetime.now().strftime(time_format)
            
            try:
                formatted =  datetime.strptime(time_input, time_format)
                return formatted.strftime(time_format)
            except ValueError:
                Print.red("The time entered is not valid.")

    def severity():
        severity_input = input("Rank from 1-10 how sever this symptom was/is: ")

        if not severity_input.isdigit():
            Print.red("You must enter a number here.")
        elif int(severity_input) < 1 or int(severity_input) > 10:
            Print.red("The number you entered does not have a coresponding command.")
        else:
            return int(severity_input)
        
    def ingredient():
        while True:
            ingredient_input = input("Ingredient: ")
            if ingredient_input == '':
                Print.red("You did not enter anything.")
            elif ingredient_input == 'exit':
                break
            else:
                return ingredient_input

