import tkinter as tk
from tkinter import messagebox

# -------- LOGIN FUNCTION -------- #
def login():
    user = username_entry.get()
    pw = password_entry.get()
    
    if user == "admin" and pw == "1234":
        messagebox.showinfo("Login Successful", f"Welcome, {user}!")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

# -------- MAIN WINDOW -------- #
root = tk.Tk()
root.title("Beautiful Login Form")
root.geometry("400x500")
root.config(bg="#E8F0FE")
root.resizable(False, False)

# -------- MAIN FRAME -------- #
frame = tk.Frame(root, bg="white", bd=0, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=400)

# -------- TITLE -------- #
tk.Label(frame, text="Welcome", font=("Helvetica", 22, "bold"), bg="white", fg="#333").pack(pady=(30,10))
tk.Label(frame, text="Please login to continue", font=("Helvetica", 10), bg="white", fg="#777").pack()

# -------- USERNAME FIELD -------- #
tk.Label(frame, text="Username", font=("Helvetica", 10), bg="white", anchor="w").pack(padx=30, pady=(30,0), fill="x")
username_entry = tk.Entry(frame, font=("Helvetica", 11), bd=1, relief="solid", highlightthickness=1, highlightcolor="#ccc")
username_entry.pack(padx=30, fill="x", ipady=8)

# -------- PASSWORD FIELD -------- #
tk.Label(frame, text="Password", font=("Helvetica", 10), bg="white", anchor="w").pack(padx=30, pady=(20,0), fill="x")
password_entry = tk.Entry(frame, font=("Helvetica", 11), bd=1, relief="solid", show="*", highlightthickness=1, highlightcolor="#ccc")
password_entry.pack(padx=30, fill="x", ipady=8)

# -------- LOGIN BUTTON -------- #
login_btn = tk.Button(frame, text="Login", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049", bd=0, command=login)
login_btn.pack(pady=30, ipadx=10, ipady=6)

# -------- FOOTER -------- #
tk.Label(frame, text="© 2025 Your App", font=("Helvetica", 8), bg="white", fg="#aaa").pack(side="bottom", pady=10)

root.mainloop()
