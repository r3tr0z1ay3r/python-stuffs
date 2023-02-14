import sqlite3

con = sqlite3.Connection('Student1.db')
cur = con.cursor()
test = '''Select * from Quaterly'''
print(cur.execute(test).fetchall())
con.commit()
con.close()