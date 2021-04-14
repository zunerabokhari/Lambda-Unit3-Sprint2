"""Examples of PostGreSQL Connection"""
from os import getenv
import psycopg2
import create_queries as create

dbname = getenv("DBNAME")
user = getenv("PG_USER")
password = getenv("PG_PASSWORD")
host = getenv("PG_HOST")

# Step 1: connect to DB
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                            password=password, host=host)

# Step 2: make a cursor to traverse DB
pg_curs = pg_conn.cursor()

# Step 3: make a query (queries.py files)


# Step 4: execute query 
# creating 
pg_curs.execute(create.CREATE_TEST)
pg_curs.execute(create.INSERT_TEST)

# reading
pg_curs.execute("SELECT * FROM test_table;")

# Step 5: Fetch data 
results = pg_curs.fetchall()
if __name__ == "__main__":
    print(results)