import tkinter as tk
from tkinter import messagebox
from system_logic.hash import verify_password, hash_password
from system_logic.database_manager import connect_to_db, disconnect_from_db
import psycopg2
from psycopg2 import sql
from system_UI.dashboard_ui import create_dashboard_ui

def get_user_credentials(username:str) -> tuple:
    conn = None

    try:
        conn = connect_to_db()
        with conn.cursor() as cur:
            query = sql.SQL("SELECT username, hashed_password FROM users WHERE username = %s")
            cur.execute(query, (username,))
            result = cur.fetchone()

            if result:
                return result
            else:
                return None
    except psycopg2.Error as e:
        print(f"Error querying the database: {e}")
    finally:
        if conn is not None:
            disconnect_from_db(conn)

def verify_login(username, password):
    # Placeholder logic, replace with actual database verification
    if username == "admin" and password == "password":
        return True
    return False

def on_login(username_entry, password_entry, login_window):
    username = username_entry.get()
    password = password_entry.get()

    credentials = get_user_credentials(username)

    if credentials:
        db_username, db_hashed_password = credentials

        if verify_password(password, db_hashed_password):
            # Login successful
            # Redirect to the dashboard
            login_window.destroy()
            root = tk.Tk()
            create_dashboard_ui(root)
            root.mainloop()

        else:
            # Login failed
            messagebox.showerror("Login Failed", "Invalid username or password.")
    else:
        # Login failed
        messagebox.showerror("Login Failed", "Invalid username or password.")

    
    # Clear the entry fields
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)