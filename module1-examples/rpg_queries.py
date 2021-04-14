"""Module 1 Project"""
import sqlite3
import queries as q


# Step 1: Make conn object to your DB
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


# Step 2: Make cursor through conn object
# Step 3: Execute query 
# Step 4: Pull results 
def execute_q(con, query):
    curs = con.cursor()
    curs.execute(query)
    results = curs.fetchall()
    curs.close()
    return results


if __name__ == "__main__":
    con = connect_to_db()   
    results = execute_q(con, q.select_all)
    
    """Using execute_q to execute queries from queries.py """
    select_all = execute_q(con, q.select_all)
    total_characters = execute_q(con, q.total_characters)
    total_items = execute_q(con, q.total_items)
    weapons = execute_q(con, q.weapons)
    non_weapons = execute_q(con, q.non_weapons)
    character_items = execute_q(con, q.character_items)

    print('Total Character:', total_characters)
    print('Total Items:', total_items)
    print('Total Weapons:', weapons)
    print('Non Weapons:', non_weapons)
    print('Character Items:', character_items[:5])
    print('Select All:', select_all[:5])
