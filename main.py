from system_UI.login_ui import create_login_ui
import customtkinter as ctk
from system_UI.dashboard_ui import create_dashboard_ui

if __name__ == "__main__":
    root = ctk.CTk()
    # root.title("Oliver Family Retailers Management System")
    root.geometry("900x600")
    create_login_ui(root)
    # create_dashboard_ui(root)
    root.mainloop()