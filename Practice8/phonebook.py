import csv
from connect import connect


def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

def upsert(first_name, last_name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    cur.close()
    conn.close()

def bulk_insert(names, phones):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL bulk_upsert_contacts(%s, %s)", (names, phones))
    conn.commit()
    cur.close()
    conn.close()

def delete(first_name=None, last_name=None, phone=None):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    cur.close()
    conn.close()


def menu():
    while True:
        print("\n1 CSV\n2 Add\n3 Update\n4 Query\n5 Delete\n0 Exit")
        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break
        
create_table()
menu()