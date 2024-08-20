import tkinter as tk
import customtkinter as ctk

def create_dashboard_ui(root):
    # Create the dashboard window
    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("1000x600")  # Set size as needed

    # Create the sidebar frame
    sidebar_frame = ctk.CTkFrame(dashboard_window, width=200, corner_radius=0)
    sidebar_frame.pack(side="left", fill="y")

    # Add buttons to the sidebar
    sidebar_button1 = ctk.CTkButton(sidebar_frame, text="Sales Summary", font=("Arial", 12), height=40)
    sidebar_button1.pack(pady=10, padx=10, fill="x")
    
    sidebar_button2 = ctk.CTkButton(sidebar_frame, text="Debts Summary", font=("Arial", 12), height=40)
    sidebar_button2.pack(pady=10, padx=10, fill="x")
    
    sidebar_button3 = ctk.CTkButton(sidebar_frame, text="Supplies Summary", font=("Arial", 12), height=40)
    sidebar_button3.pack(pady=10, padx=10, fill="x")

    # Create the content frame
    content_frame = ctk.CTkFrame(dashboard_window)
    content_frame.pack(side="right", fill="both", expand=True)

    # Create a frame for summary
    summary_frame = ctk.CTkFrame(content_frame, corner_radius=10)
    summary_frame.pack(pady=20, padx=20, expand=True)

    # Create a canvas and a scrollbar for better scrolling
    canvas = tk.Canvas(summary_frame, bg="white")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(summary_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas for placing widgets
    inner_frame = ctk.CTkFrame(canvas, corner_radius=10)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Update the canvas scroll region
    inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Add dummy data to the summary frame
    sales_label = ctk.CTkLabel(inner_frame, text="Sales Summary", font=("Arial", 20, "bold"))
    sales_label.pack(pady=10)

    sales_amount_label = ctk.CTkLabel(inner_frame, text="Total Sales: $10,000", font=("Arial", 16))
    sales_amount_label.pack(pady=10)

    debts_label = ctk.CTkLabel(inner_frame, text="Debts Summary", font=("Arial", 20, "bold"))
    debts_label.pack(pady=10)

    debts_amount_label = ctk.CTkLabel(inner_frame, text="Total Debts: $2,000", font=("Arial", 16))
    debts_amount_label.pack(pady=10)

    supplies_label = ctk.CTkLabel(inner_frame, text="Supplies Summary", font=("Arial", 20, "bold"))
    supplies_label.pack(pady=10)

    supplies_amount_label = ctk.CTkLabel(inner_frame, text="Total Supplies: $5,000", font=("Arial", 16))
    supplies_amount_label.pack(pady=10)

    # Ensure the dashboard window is shown
    dashboard_window.mainloop()
