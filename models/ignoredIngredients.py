from database.db import DB
from database.tables import Tables

class IgnoredIngredients:
    def store(ingredient):
        if not DB.Query.value_exists('ignored_ingredients', 'ingredient', ingredient):
            DB.Query.insert_into('ignored_ingredients', ['ingredient'], [ingredient])

    def update(old_ingredient, new_ingredient):
        DB.Query.update_by_column('ignored_ingredients', ['ingredient'], [old_ingredient], 'ingredient', new_ingredient)

    def delete(ingredient):
        DB.Query.delete_by_column('ignored_ingredients', 'ingredient', ingredient)

    def fetch():
        return DB.Query.fetch_columns('ignored_ingredients', ['ingredient'])
    
    def reset():
        DB.Query.drop_table('ignored_ingredients')
        Tables.create_ignored_ingredients_table()