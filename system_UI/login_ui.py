import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from system_logic.login_logic import verify_login, on_login

def create_login_ui(root):
    # Configure the main window layout
    root.title("Maama Jimmy Retail System - Login")
    # root.geometry("800x400")

    # Create the left frame for the image and business title
    left_frame = ctk.CTkFrame(root, width=400, height=400)
    left_frame.pack(side="left", fill="both", expand=True)

    # Load and place the image
    image = Image.open("assets/images/login_image.jpg")
    image = image.resize((500, 400), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(image)
    image_label = ctk.CTkLabel(left_frame, image=image, text="")
    image_label.image = image  # Keep a reference to avoid garbage collection
    image_label.pack(fill="both", expand=True)

    # Add the business title on top of the image
    business_title_header = ctk.CTkLabel(left_frame, text="Maama Jimmy Retail System", font=("Arial", 34, "bold"))
    business_title_header.place(relx=0.5, rely=0.05, anchor="n")

    # Add message for users without an account
    contact_message = ctk.CTkLabel(left_frame, text="Please note: If you don't have an account, please contact the Admin/Technical team to create one.", font=("Arial", 12))
    contact_message.place(relx=0.5, rely=0.85, anchor="n")

    # Create the right frame for the login form
    right_frame = ctk.CTkFrame(root, width=500, height=400)
    right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=60)

    # Add the "Login" title to the form
    login_title = ctk.CTkLabel(right_frame, text="Login", font=("Arial", 20, "bold"))
    login_title.pack(pady=20)

    # Username Label and Entry
    username_label = ctk.CTkLabel(right_frame, text="Username", font=("Arial", 14))
    username_label.pack(pady=(0, 10))
    username_entry = ctk.CTkEntry(right_frame, font=("Arial", 14))
    username_entry.pack(pady=(0, 20))

    # Password Label and Entry
    password_label = ctk.CTkLabel(right_frame, text="Password", font=("Arial", 14))
    password_label.pack(pady=(0, 10))
    password_entry = ctk.CTkEntry(right_frame, font=("Arial", 14), show="*")
    password_entry.pack(pady=(0, 20))

    # Login Button
    login_button = ctk.CTkButton(right_frame, text="Login", font=("Arial", 14), command=lambda: on_login(username_entry, password_entry, root))
    login_button.pack(pady=(20, 10))

    # Forgot Password Link
    forgot_password_link = ctk.CTkLabel(right_frame, text="Forgot Password?", font=("Arial", 12), fg_color="transparent", text_color="blue")
    forgot_password_link.pack(pady=(10, 10))

    root.mainloop()