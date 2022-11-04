import sqlite3
from pathlib import Path
import os
root_path = Path(__file__).parent.parent

connection = sqlite3.connect(os.path.join(root_path, 'database.db'))

cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS posts;")

cur.execute('''
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    );''')

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