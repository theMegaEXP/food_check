import commandline.debug as debug
import database.tables as tables
from database.db import DB


def main():
    tables.create_tables()
    debug.debug()
    

if __name__ == "__main__":
    main()