from tkinter import ttk
import tkinter as tk

blow = [("january", "2013"), ("february", "2014"), ("march", "2015"), ("april",
                                                                       "2016"), ("may", "2017")]


def append_select():
    for my in tree.selection():
        tree2.insert("", tk.END, values=my)
        # tree2.insert("", tk.END, values=n) # this insert last content in the list


root = tk.Tk()
root.geometry("500x500")

tree = ttk.Treeview(columns=("columns1", "columns"), show="headings",
                    selectmode="browse")
tree.heading("#1", text="Month")
tree.heading("#2", text="Year")

for n in blow:
    tree.insert("", tk.END, values=(n))

tree.pack()

b1 = tk.Button(text="append", command=append_select)
b1.pack()

tree2 = ttk.Treeview(columns=("Month", "Year"), show="headings")
tree2.heading("#1", text="First name")
tree2.heading("#2", text="Surname")
tree2.pack()

root.mainloop()
