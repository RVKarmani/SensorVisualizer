###Working Script


import serial

from datetime import datetime
import sqlite3
import os

status = True
###########
import sqlite3
database_file = "sensor5.db"

sqliteConnection = sqlite3.connect(database_file)
cursor1 = sqliteConnection.cursor()
print("Connected to Database {}".format(database_file))

cursor1.executescript("""
                    DROP TABLE IF EXISTS data;
                    CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, methane TEXT,co TEXT, smoke TEXT)
                    """)

def insertVaribleIntoTable(id, methane, co,smoke):
	try:
		cursor = sqliteConnection.cursor()
		
		sqlite_insert_with_param = """INSERT INTO 'data'
                          ('id', 'methane', 'co','smoke') 
                          VALUES (?, ?, ?,?);"""
		
		data_tuple = (id, methane, co,smoke)
		cursor.execute(sqlite_insert_with_param, data_tuple)
		sqliteConnection.commit()
		print("Python Variables inserted successfully into data table")
		cursor.close()
		
	except sqlite3.Error as error:
		print("Failed to insert Python variable into sqlite table", error)
	


while(True):
	try:
		ser = serial.Serial('COM2',9600)
		break
	except serial.SerialException:
		print('ARDUINO Not connected')
		time.sleep(3)
		status=False

records = 0
while records < 25:
	element = ser.readline().split(",")
	methane = (element[0])
	co =(element[1])
	smoke = (element[2])
	#datestamp = datetime.now()
	print('Record {} received with values methane: {}ppm co: {}ppm smoke: {}ppm'.format(records+1,methane,co,smoke))
	insertVaribleIntoTable(records,methane,co,smoke)
	records = records + 1

sqliteConnection.close()
