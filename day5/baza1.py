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
