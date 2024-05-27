import sqlite3

#cursor.execute('''CREATE TABLE IF NOT EXISTS user (
#                    id INTEGER PRIMARY KEY,
#                    name TEXT NOT NULL,
#                    address TEXT
#                )''')

def get_id():
    file=open("id.txt",'r')
    id_=file.read()
    file.close()
    file=open("id.txt",'w')
    file.write(str(int(id_)+1))
    file.close()
    return id_

def add_data(data):
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO user (id, name, address) VALUES (?, ?, ?)',data)
    conn.commit()
    conn.close()
    print("Table 'user' created and sample data inserted successfully.")
data = [
        (1, 'John Doe', '123 Main St'),
        (2, 'Jane Smith', '456 Elm St'),
        (3, 'Bob Johnson', '789 Oak St')
    ]