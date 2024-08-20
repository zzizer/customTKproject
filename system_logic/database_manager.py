import psycopg2
from psycopg2 import sql

def connect_to_db() -> psycopg2.extensions.connection:
    try:
        conn = psycopg2.connect(
            dbname="sample",
            user="admin",
            password="abc123ABC.",
            host="localhost",
            port="5432"
        )
        print("Connected to the database")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def disconnect_from_db(conn: psycopg2.extensions.connection):
    try:
        if conn is not None:
            conn.close()
            print("Disconnected from the database")
    except psycopg2.Error as e:
        print(f"Error disconnecting from the database: {e}")
