import psycopg2
from psycopg2 import DatabaseError
import sys

def check_db_connection(host, dbname, user, password, port):
    """Connect to the PostgreSQL database server and check the connection status."""
    conn = None
    try:
        print(f"Connecting to the PostgreSQL database at {host}:{port}...")
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        # If the connection is successful, a connection object is returned
        print("Connection successful!")
        
        # Optional: execute a simple query to confirm the database is fully accessible
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(f"PostgreSQL database version: {db_version}")
        cur.close()

    except DatabaseError as e:
        # Catches any database connection errors (e.g., wrong credentials, server down)
        print(f"An error occurred: {e}")
        print("Failed to connect to the PostgreSQL database.")
        sys.exit(1)
    finally:
        # Ensures the connection is closed even if an error occurs
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    # Replace with your actual database credentials
    DB_HOST = 'localhost'
    DB_NAME = 'dnaiconsole'
    DB_USER = 'user'
    DB_PASSWORD = 'password'
    DB_PORT = 5432

    check_db_connection(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
