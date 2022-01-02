import sqlite3
connection = sqlite3.connect("student_details.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
#cursor.execute('''DROP TABLE Student_Info;''')
connection.execute("create table Student_Info (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, RollNo NUMBER NOT NULL, contact NUMBER UNIQUE NOT NULL, Age NUMBER NOT NULL)")
print("Table created successfully")
connection.close()   
