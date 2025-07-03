# travel_functions.py
import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="travel"
    )

def add_package_window():
    win = tk.Toplevel()
    win.title("Add Package")

    tk.Label(win, text="Package ID").grid(row=0, column=0)
    tk.Label(win, text="Package Name").grid(row=1, column=0)
    tk.Label(win, text="Source-Destination").grid(row=2, column=0)
    tk.Label(win, text="Day-Night").grid(row=3, column=0)
    tk.Label(win, text="Charges").grid(row=4, column=0)

    e1, e2, e3, e4, e5 = (tk.Entry(win) for _ in range(5))
    for i, e in enumerate([e1, e2, e3, e4, e5]):
        e.grid(row=i, column=1)

    def submit():
        con = connect_db()
        cur = con.cursor()
        cur.execute("INSERT INTO package VALUES (%s, %s, %s, %s, %s)",
                    (e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Package Added")

    tk.Button(win, text="Submit", command=submit).grid(row=6, columnspan=2)

def enquire_package_window():
    win = tk.Toplevel()
    win.title("Enquire Package")

    tk.Label(win, text="Enter Package ID").pack()
    e = tk.Entry(win)
    e.pack()

    def search():
        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM package WHERE id=%s", (e.get(),))
        data = cur.fetchone()
        con.close()
        if data:
            msg = f"Name: {data[1]}\nSrc-Dest: {data[2]}\nDay-Night: {data[3]}\nCharges: {data[4]}"
        else:
            msg = "Package not found"
        messagebox.showinfo("Result", msg)

    tk.Button(win, text="Search", command=search).pack()

def modify_package_window():
    win = tk.Toplevel()
    win.title("Modify Package")

    tk.Label(win, text="Package ID").pack()
    id_entry = tk.Entry(win)
    id_entry.pack()
    tk.Label(win, text="New Package Name").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    def update():
        con = connect_db()
        cur = con.cursor()
        cur.execute("UPDATE package SET pname=%s WHERE id=%s", (name_entry.get(), id_entry.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Updated", "Package Updated")

    tk.Button(win, text="Update", command=update).pack()

def display_all_packages_window():
    win = tk.Toplevel()
    win.title("All Packages")
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM package")
    data = cur.fetchall()
    con.close()

    for i, row in enumerate(data):
        tk.Label(win, text=str(row)).pack()

def remove_package_window():
    win = tk.Toplevel()
    win.title("Remove Package")
    tk.Label(win, text="Enter Package ID to delete").pack()
    e = tk.Entry(win)
    e.pack()

    def delete():
        con = connect_db()
        cur = con.cursor()
        cur.execute("DELETE FROM package WHERE id=%s", (e.get(),))
        con.commit()
        con.close()
        messagebox.showinfo("Deleted", "Package Deleted")

    tk.Button(win, text="Delete", command=delete).pack()

def add_customer_window():
    win = tk.Toplevel()
    win.title("Add Customer")

    tk.Label(win, text="Customer ID").grid(row=0, column=0)
    tk.Label(win, text="Name").grid(row=1, column=0)
    tk.Label(win, text="Address").grid(row=2, column=0)
    tk.Label(win, text="Contact No").grid(row=3, column=0)

    e1, e2, e3, e4 = (tk.Entry(win) for _ in range(4))
    for i, e in enumerate([e1, e2, e3, e4]):
        e.grid(row=i, column=1)

    def submit():
        con = connect_db()
        cur = con.cursor()
        cur.execute("INSERT INTO customer VALUES (%s, %s, %s, %s)",
                    (e1.get(), e2.get(), e3.get(), e4.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Customer Added")

    tk.Button(win, text="Submit", command=submit).grid(row=4, columnspan=2)

def customer_list_window():
    win = tk.Toplevel()
    win.title("Customer List")

    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM customer")
    data = cur.fetchall()
    con.close()

    for row in data:
        tk.Label(win, text=str(row)).pack()

def book_package_window():
    win = tk.Toplevel()
    win.title("Book Package")

    tk.Label(win, text="Customer ID").grid(row=0, column=0)
    tk.Label(win, text="Package ID").grid(row=1, column=0)
    tk.Label(win, text="No. of Persons").grid(row=2, column=0)

    cid, pid, persons = (tk.Entry(win) for _ in range(3))
    cid.grid(row=0, column=1)
    pid.grid(row=1, column=1)
    persons.grid(row=2, column=1)

    def book():
        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT cname FROM customer WHERE cid=%s", (cid.get(),))
        cname = cur.fetchone()
        cur.execute("SELECT pname, pamt FROM package WHERE id=%s", (pid.get(),))
        pdata = cur.fetchone()

        if cname and pdata:
            try:
                total = int(pdata[1]) * int(persons.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter valid number of persons")
                con.close()
                return
            cur.execute("INSERT INTO booking (cid, cname, pid, pbname, person, tamt) VALUES (%s,%s,%s,%s,%s,%s)",
                        (cid.get(), cname[0], pid.get(), pdata[0], persons.get(), total))
            con.commit()
            messagebox.showinfo("Booked", f"Package booked! Total: {total}")
        else:
            messagebox.showerror("Error", "Invalid Customer or Package ID")

        con.close()

    tk.Button(win, text="Book Now", command=book).grid(row=3, columnspan=2)

def booking_details_window():
    win = tk.Toplevel()
    win.title("Booking Details")

    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM booking")
    data = cur.fetchall()
    con.close()

    for row in data:
        tk.Label(win, text=str(row)).pack()
def cancel_booking_window():
    win = tk.Toplevel()
    win.title("Cancel Booking")

    tk.Label(win, text="Enter Booking ID to cancel").pack()
    e = tk.Entry(win)
    e.pack()

    def cancel():
        con = connect_db()
        cur = con.cursor()
        cur.execute("DELETE FROM booking WHERE bid=%s", (e.get(),))
        con.commit()
        con.close()
        messagebox.showinfo("Cancelled", "Booking Cancelled")

    tk.Button(win, text="Cancel", command=cancel).pack()
def main_menu():
    root = tk.Tk()
    root.title("Travel Management System")

    tk.Button(root, text="Add Customer", command=add_customer_window).pack()
    tk.Button(root, text="Customer List", command=customer_list_window).pack()
    tk.Button(root, text="Book Package", command=book_package_window).pack()
    tk.Button(root, text="Booking Details", command=booking_details_window).pack()
    tk.Button(root, text="Cancel Booking", command=cancel_booking_window).pack()

    root.mainloop()
if __name__ == "__main__":
    main_menu()
    
# This code is a complete travel management system using Tkinter and MySQL.
# It allows users to add, modify, enquire, and remove travel packages,  
# as well as manage customers and bookings. The GUI is built using Tkinter,
# and MySQL is used for database operations. The system includes functions
# for connecting to the database, adding packages and customers, booking packages,
# displaying booking details, and cancelling bookings. Each function creates a new
# window for the respective operation, allowing for a user-friendly interface.
# The main menu provides buttons to access different functionalities of the system.
# Ensure you have the MySQL server running and the database 'travel' with the required tables




