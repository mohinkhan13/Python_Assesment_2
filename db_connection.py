import sqlite3

def create_connection():
    try:
        connection = sqlite3.connect('banking_system.db')
        print("Successfully connected to the SQLite database")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None
