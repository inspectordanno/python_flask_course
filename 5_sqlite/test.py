import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = """
--sql
CREATE TABLE users(id int, username text, password text)
;
"""
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = """
--sql
INSERT INTO users VALUES (?, ?, ?)
;
"""
cursor.execute(insert_query, user)

users = [
    (2, 'anne', 'asdf'),
    (3, 'rolf', 'xyz')
]
cursor.executemany(insert_query, users)

select_query = """
--sql
SELECT * from users
;
"""
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
