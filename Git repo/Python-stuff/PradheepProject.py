import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('students.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
#Commented out since table has been created

# cursor.execute("""CREATE TABLE STUDENTS(
#                 FIRST_NAME CHAR(20) NOT NULL,
#                 LAST_NAME CHAR(20),
#                 AGE INT,
#                 SEX CHAR(1),
#                 YEAR INT)
#                 """)

# #Commenting out since they are already inserted into the database

# cursor.execute('''INSERT INTO STUDENTS(
#     FIRST_NAME, LAST_NAME, AGE, SEX, YEAR) VALUES 
#     ('Ramya', 'Rama Priya', 17, 'F', 2020)''')

# cursor.execute('''INSERT INTO STUDENTS(
#     FIRST_NAME, LAST_NAME, AGE, SEX, YEAR) VALUES 
#     ('Vinay', 'Battacharya', 17, 'M', 2020)''')

# cursor.execute('''INSERT INTO STUDENTS(
#     FIRST_NAME, LAST_NAME, AGE, SEX, YEAR) VALUES 
#     ('Sharukh', 'Sheik', 17, 'M', 2020)''')

# cursor.execute('''INSERT INTO STUDENTS(
#     FIRST_NAME, LAST_NAME, AGE, SEX, YEAR) VALUES 
#     ('Sarmista', 'Sharma', 17, 'F', 2020)''')

# cursor.execute('''INSERT INTO STUDENTS(
#     FIRST_NAME, LAST_NAME, AGE, SEX, YEAR) VALUES 
#     ('Tripthi', 'Mishra', 17, 'F', 2020)''')

# cursor.execute('''INSERT INTO STUDENTS(
#     FIRST_NAME, LAST_NAME, AGE, SEX, YEAR) VALUES 
#     ('Vinal', 'Mishra', 17, 'M', 2020)''')
# #Commiting changes
# conn.commit()

#Showing resulting table
cursor.execute("SELECT * FROM STUDENTS")
all_results = cursor.fetchall()

for i in all_results:
    print(i)

# Closing the connection
conn.close()