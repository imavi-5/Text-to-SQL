import sqlite3

## connect to sqlite3
connection = sqlite3.connect("student.db")

## creating cursor object to insert record, create table, retrieve
cursor = connection.cursor()

## create the table
table_info="""
Create table STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);

"""

cursor.execute(table_info)

## insert some more records

cursor.execute('''Insert Into STUDENT values('Aditya', 'Data Science', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Anshul', 'Data Science', 'B', 100)''')
cursor.execute('''Insert Into STUDENT values('Harsh', 'Data', 'A', 80)''')
cursor.execute('''Insert Into STUDENT values('Durgesh', 'Data Analyst', 'C', 40)''')
cursor.execute('''Insert Into STUDENT values('Vivek', 'Data Analyst', 'D', 60)''')

## Disaply all the records
print("The inserted records are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

## close connection
connection.commit()
connection.close()