import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('voting_database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()
cursor.execute("""SELECT * FROM vot""")

result = cursor.fetchall()
for i in result:
    print(i)