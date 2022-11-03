from pathlib import Path
import os
root_path = Path(__file__).parent.parent

import sqlite3

connection = sqlite3.connect(os.path.join(root_path,'database.db'))


with open(os.path.join(root_path,'schema.sql')) as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )
cur.execute('SELECT * FROM posts')
print(cur.fetchall())


connection.commit()
connection.close()