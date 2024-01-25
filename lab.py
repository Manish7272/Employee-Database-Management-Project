import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk 
from tkinter import messagebox
import dababase

app = customtkinter.CTk()
app.title("Employee Management System")
app.geometry("900x420")
app.config(bg = "#161C25")
app.resizable(False, False)

font1 = ("Arial", 20, "bold")
font2 = ("Arial", 12, "bold")

id_label = customtkinter.CTkLabel(app,   font = font1, text="ID:", text_color="#fff", bg_color="#161C25")
id_label.place(x=20, y=20)

id_entry = customtkinter.CTkEntry(app,   font = font1, text_color="#000", fg_color="#fff", width=180)
id_entry.place(x=100, y=20)

name_label = customtkinter.CTkLabel(app, font = font1, text="Name:", text_color="#fff", bg_color="#161C25")
name_label.place(x=20, y=80)

name_entry = customtkinter.CTkEntry(app, font = font1, text_color="#000", fg_color="#fff", width=180)
name_entry.place(x=100, y=80)

role_label = customtkinter.CTkLabel(app, font = font1, text="Role:", text_color="#fff", bg_color="#161C25")
role_label.place(x=20, y=140)

role_entry = customtkinter.CTkEntry(app, font = font1, text_color="#000", fg_color="#fff", width=180)
role_entry.place(x=100, y=140)

gender_label = customtkinter.CTkLabel(app, font = font1, text="Gender:", text_color="#fff", bg_color="#161C25")
gender_label.place(x=20, y=200)

options = ["Male", "Female"]
Variable1 = StringVar()

gender_options = customtkinter.CTkComboBox(app, font=font1, text_color="#000", fg_color="#fff", width=180, values=options, state="normal")
gender_options.set("Male")
gender_options.place(x=100, y=200)

status_label = customtkinter.CTkLabel(app, font = font1, text="Status:", text_color="#fff", bg_color="#161C25")
status_label.place(x=20, y=260)

status_entry = customtkinter.CTkEntry(app, font = font1, text_color="#000", fg_color="#fff", width=180)
status_entry.place(x=100, y=260)

add_button = customtkinter.CTkButton(app, font=font1, text_color="#fff",text="Add Employee", fg_color="#05A312", bg_color="#161C25", cursor="hand2", corner_radius=15, width=260)
add_button.place(x=20, y=310)

app.mainloop()