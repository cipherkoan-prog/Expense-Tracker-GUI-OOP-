import tkinter as tk
from tkinter import messagebox

from expense import Expense
from data_handler import load_expenses, save_expenses 

from datetime import datetime

class ExpensesGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("expenses Tracker")
        self.root.geometry("450x450")
        icon = tk.PhotoImage(file="assets/logo.png")
        self.root.iconphoto(True, icon)
        self.root.config(bg="#1e1e2f")

        self.input_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.input_frame.pack(pady=20)

        self.amount_label = tk.Label(self.input_frame, text="Amount:", bg="#1e1e2f", fg="white")
        self.amount_entry = tk.Entry(self.input_frame)
        self.amount_label.grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        self.category_label = tk.Label(self.input_frame, text="Category:", bg="#1e1e2f", fg="white")
        self.category_entry = tk.Entry(self.input_frame)
        self.category_label.grid(row=1, column=0, padx=5, pady=5)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        self.date_label = tk.Label(self.input_frame, text="Date:", bg="#1e1e2f", fg="white")
        self.date_entry = tk.Entry(self.input_frame)
        self.date_label.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)
        today = datetime.now().strftime("%d-%m-%Y")
        self.date_entry.insert(0, today)

        self.button_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.button_frame.pack(pady=20)

        self.add_button = tk.Button(self.button_frame, text="Add Expenses", command=self.add_expenses)
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.button_frame, text="View Expense", command=self.view_expenses)
        self.view_button.pack(pady=10)

        text_frame = tk.Frame(self.root)
        text_frame.pack(pady=10)

        scrollbar = tk.Scrollbar(text_frame)


        self.text_area = tk.Text(
            text_frame,
            width=50,
            height=10,
            yscrollcommand=scrollbar.set
        )

        scrollbar.config(command=self.text_area.yview)

        self.text_area.pack(side=tk.LEFT)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

    
    def add_expenses(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        date = self.date_entry.get()

        if not amount or not category:
            messagebox.showerror(
                "Error",
                "All fields are required"
            )
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Amount must be number"
            )
            return
        
        expense = Expense(
            amount,
            category,
            date
        )

        expenses = load_expenses()

        expenses.append(expense.to_dict())
        save_expenses(expenses)

        messagebox.showinfo(
            "Info",
            "expenses addad successfully"
        )

        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

        today = datetime.now().strftime("%d-%m-%Y")
        self.date_entry.insert(0, today)

    def view_expenses(self):
        expenses = load_expenses()

        self.text_area.delete(1.0, tk.END)

        if not expenses:
            self.text_area.insert(
                tk.END,
                "No expenses found."
            )
            return

        for expense in expenses:
            self.text_area.insert(
                tk.END,
                f"Amount: {expense['amount']}\n"
                f"Category: {expense['category']}\n"
                f"Date: {expense['date']}\n\n"
            )

    def run(self):
        self.root.mainloop()





        

