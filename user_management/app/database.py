import sqlite3
from .config import DATABASE_PATH

def get_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def create_user_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            user_id INTEGER PRIMARY KEY,
            full_name TEXT,
            contact_email TEXT,
            street_address TEXT,
            apt_number TEXT,
            town TEXT,
            postal_code TEXT,
            phone_number TEXT,
            employer TEXT
        )
    ''')
    connection.commit()
    connection.close()

def insert_users(users):
    connection = get_db_connection()
    cursor = connection.cursor()
    for user in users:
        cursor.execute('''
            INSERT INTO user_data (user_id, full_name, contact_email, street_address, apt_number, town, postal_code, phone_number, employer)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user['id'], user['name'], user['email'], user['address']['street'], user['address']['suite'],
              user['address']['city'], user['address']['zipcode'], user['phone'], user['company']['name']))
    connection.commit()
    connection.close()