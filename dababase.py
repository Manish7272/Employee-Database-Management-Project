import sqlite3 as sqlight3

def create_table():
    conn = sqlight3.connect("Employees.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   role TEXT,
                   gender TEXT,
                   status TEXT)''')
    conn.commit()
    conn.close()

def fetch_employees():
    conn = sqlight3.connect("Employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    conn.close()
    return employees

def insert_employees(id, name, role, gender,status):
    conn = sqlight3.connect("Employees.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Employees (id, name, role, gender, status) VALUES (?, ?, ?, ?, ?)",
                   (id, name, role, gender, status))
    conn.commit()
    conn.close()

def delete_employee(id):
    conn = sqlight3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Employees WHERE id = ?", (id,))
    conn.commit()
    conn.close()
                   
def update_employee(new_name, new_role, new_gender, new_status, id):
    conn = sqlight3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Employees SET name = ?, role = ?, gender=?, status = ? WHERE id = ?",
                   (new_name, new_role, new_gender, new_status, id))
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlight3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Count(*) FROM Employees WHERE id = ?", (id,))
    result = cursor.fatchone()    
    conn.close()
    return result[0] >0
create_table()