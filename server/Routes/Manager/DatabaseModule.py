import sqlite3


# connect to database
def connect_to_db(db_name):
    return sqlite3.connect(db_name)


# insert to database
def insert(list_data):
    conn = connect_to_db('home_test_db.sql')
    c = conn.cursor()
    try:
        c.execute(
            """ CREATE TABLE IF NOT EXISTS downloaded_tree_data ( id INTEGER PRIMARY KEY ,tree_name TEXT NOT NULL,tree_data INTEGER NOT NULL); """)
    except sqlite3.Error as e:
        print(e)
    insert_data = []
    for data in list_data:
        insert_data.append((data['name'], data['size']))
    c.executemany('INSERT INTO downloaded_tree_data(tree_name,tree_data) VALUES (?,?)', insert_data)
    conn.commit()
    conn.close()


# delete all from table
def delete_all():
    conn = connect_to_db('home_test_db.sql')
    c = conn.cursor()
    c.execute("DELETE FROM downloaded_tree_data")
    conn.commit()
    conn.close()

# select all from database
def select_all():
    conn = connect_to_db('home_test_db.sql')
    c = conn.cursor()
    c.execute("SELECT tree_name,tree_data FROM downloaded_tree_data")
    rows = c.fetchall()
    conn.close()
    tree_data = []
    for row in rows:
        tree_data.append({'name': row[0], 'size': row[1]})
    return tree_data


# get searched node
def get_node(node_name, node_size):
    conn = connect_to_db('home_test_db.sql')
    c = conn.cursor()
    if node_size == 'NaN':
        c.execute("SELECT tree_name,tree_data FROM downloaded_tree_data WHERE tree_name LIKE?",
                  ('%' + node_name + '%',))
    else:
        c.execute("SELECT tree_name,tree_data FROM downloaded_tree_data WHERE tree_name LIKE? AND tree_data=?",
                  ('%' + node_name + '%', node_size))
    rows = c.fetchall()
    conn.close()
    tree_data = []
    for row in rows:
        tree_data.append({'name': row[0], 'size': row[1]})
    return tree_data
