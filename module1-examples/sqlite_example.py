'''SQLite3 - Example of a connection'''
import sqlite3
import queries as q


# Step 1: Make connection to DB
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


# Step 2: Make cursor through conn object
# Step 3: Execute query 
# Step 4: Pull results 
def execute_q(con, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    curs.close()
    return results

if __name__ == "__main__":
    conn = connect_to_db()
    results = execute_q(conn, q.select_all)
    print(results[:5])
    print(len(results))