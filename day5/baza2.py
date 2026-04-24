# baza danych - system przechowywania danych
# silnik - mechanizm przechowywania, zarządzani i dostępu do danych
# bazy relacyjne, nierelacyjne
# sql, nosql
# mssql, terradata, oracle, postgress, mysql, sqlite

import sqlite3

try:
    conn = sqlite3.connect("baza_danych.db")
    c = conn.cursor()
    print("Baza  danych zostałą podłaczona")

    query = """
            CREATE TABLE IF NOT EXISTS developers
            (
                id
                INTEGER
                PRIMARY
                KEY,
                name
                TEXT
                NOT
                NULL,
                email
                TEXT
                NOT
                NULL
                UNIQUE,
                salary
                REAL
                NOT
                NULL
            ); \
            """

    c.execute(query)
    conn.commit()

    # insert
    # insert = "INSERT INTO developers (id,name,email,salary) VALUES (1,'Radek', 'raj@raj.pl', 10000);"
    # c.execute(insert)
    # conn.commit()

    # insert = "INSERT INTO developers (id,name,email,salary) VALUES (2,'Radek', 'raj1@raj.pl', 10000);"
    # c.execute(insert)
    # conn.commit()

    select = "SELECT * FROM developers;"
    for row in c.execute(select):
        print(row)
    # (1, 'Radek', 'raj@raj.pl', 10000.0)
    # (2, 'Radek', 'raj1@raj.pl', 10000.0)
except sqlite3.Error as e:
    print("Bład podłaczenia danych:", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")
# Baza  danych zostałą podłaczona
# Połaczenie zostało zamknięte

# pgadmin, dbeaver, TablePlus,
# https://sqlitebrowser.org/dl/
