from database.init import cursor as c, conn
from commandline.print import Print

class DB:
    class Query:
        def query_print(query: str):
            c.execute(query)
            print(c.fetchall())

        def query_results(query: str):
            c.execute(query)
            return c.fetchall()
        
        def query_operation(query: str):
            c.execute(query)
            conn.commit()
    
        def create_table(table: str, columns: list[str]):
            columns_str = ', '.join(columns)
            
            c.execute(f"CREATE TABLE IF NOT EXISTS {table} ({columns_str});")
            conn.commit()

        def drop_table(table: str):
            c.execute(f"DROP TABLE IF EXISTS {table};")
            conn.commit()

        def insert_into(table: str, columns: list, values: list):
            columns_str = ", ".join(columns)
            values_str = ", ".join([f"'{value}'" for value in values])

            c.execute(f"INSERT INTO {table} ({columns_str}) VALUES ({values_str});")
            conn.commit()

        def fetch_table(table: str):
            c.execute(f"SELECT * FROM {table};")
            return c.fetchall()

        def fetch_columns(table: str, columns: list[str]):
            columns_str = ', '.join(columns)
            c.execute(f"SELECT {columns_str} FROM {table}")
            return c.fetchall()
        
        def fetch_id(table: str, column: str, name: str):
            c.execute(f"SELECT id FROM {table} WHERE {column} = '{name}'")
            return c.fetchone()[0]
        
        def value_exists(table: str, column: str, value: str):
            c.execute(f"SELECT COUNT(*) FROM {table} WHERE {column} = '{value}'")
            return c.fetchone()[0] > 0
        
        def composite_key_exists(table: str, column1: str, value1: str, column2: str, value2: str):
            c.execute(f"SELECT COUNT(*) FROM {table} WHERE {column1} = ? AND {column2} = ?", (value1, value2))
            return c.fetchone()[0] > 0
        
        def delete_by_column(table: str, column: str, value: str):
            c.execute(f"DELETE FROM {table} WHERE {column} = {value}")
            conn.commit()

        def update_by_column(table: str, columns: list[str], values: list[str], column: str, value: str):
            if len(columns) != len(values):
                raise "Columns and values are not the same lenght."
            
            set = ', '.join([f"{columns[i]} = '{values[i]}'" for i in range(len(columns))])
            c.execute(f"UPDATE {table} SET {set} WHERE {column} = {value}")
            
    class View:
        def show_tables():
            DB.Query.query_print("SELECT name FROM sqlite_master WHERE type='table';")

        def table(table: str):
            c.execute(f"PRAGMA table_info({table});")
            columns = c.fetchall()
            column_names = [column[1] for column in columns]

            c.execute(f"SELECT * FROM {table};")
            data = c.fetchall()

            print(table)

            columns_joined = ''.join([f"| {column_name} |" for column_name in column_names])
            print(columns_joined)
            
            underline = '' + ''.join(['=' for _ in range(len(columns_joined))])
            print(underline)

            for row in data:
                row_joined = ''.join([f"| {cell} |" for cell in row])
                print(row_joined)

    class Operations:
        def close():
            Print.green("DB connection closed.")
            conn.close()

        def reset():
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = c.fetchall()

            for table in tables:
                table_name = table[0]
                DB.Query.drop_table(table_name)
            
            Print.green("Database tables dropped.")
    