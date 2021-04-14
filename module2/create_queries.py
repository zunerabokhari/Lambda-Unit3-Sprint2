# for ./postgresql_examples.py
CREATE_TEST = """
    CREATE TABLE test_table(
        id SERIAL PRIMARY KEY,
        name varchar(40) NOT NULL,
        fav_num INT NOT NULL
    );
"""

INSERT_TEST = """
    INSERT INTO test_table (name, fav_num) VALUES
    (
        'Nick',
        45
    ),
    (
        'Jack',
        42
    ),
    (
        'Steven',
        56
    );
"""

# for ./sqlite_2_postgresql.py
