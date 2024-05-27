import sqlite3

conn = sqlite3.connect('voting_database.db')
cursor = conn.cursor()


def reset():
    cursor.execute('''CREATE TABLE IF NOT EXISTS vot (
                        id INTEGER PRIMARY KEY,
                        candidate TEXT,
                        votes INTEGER DEFAULT 0
                    )''')

    candidates = ['ADMK', 'DMK', 'BJP', 'CONGRESS']
    for candidate in candidates:
        cursor.execute("INSERT INTO vot (candidate, votes) VALUES (?, ?)", (candidate, 0))

    conn.commit()

def vote(candidate_name):
    cursor.execute("UPDATE vot SET votes = votes + 1 WHERE candidate = ?", (str(candidate_name),))
    conn.commit()
    print(f"Vote for {candidate_name} has been successfully cast.")

#vote('ADMK')
#reset()