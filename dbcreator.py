import sqlite3
database_file = "sensor.db"

sqliteConnection = sqlite3.connect(database_file)
cursor1 = sqliteConnection.cursor()
print("Connected to Database {}".format(database_file))

cursor1.executescript("""
                    DROP TABLE IF EXISTS data;
                    CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, methane INTEGER,co INTEGER, smoke INTEGER,timestamp DATETIME)
                    """)
sqliteConnection.close()