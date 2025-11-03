import tkinter as tk
from tkinter import ttk


#Creates a student data list
data = [
    ["1345", "John Curry", 8, 15, 7, 45],
    ["2345", "Sam Sturtivant", 14, 15, 14, 77],
    ["9876", "Lee Scott", 17, 11, 16, 99],
    ["3724", "Matt Thompson", 19, 11, 15, 81],
    ["1212", "Ron Herrema", 14, 17, 18, 66],
    ["8439", "Jake Hobbs", 10, 11, 10, 43],
    ["2344", "Jo Hyde", 6, 15, 10, 55],
    ["9384", "Gareth Southgate", 5, 6, 8, 33],
    ["8327", "Alan Shearer", 20, 20, 20, 100],
    ["2983", "Les Ferdinand", 15, 17, 18, 92]
]


#Function to calculate student marks
def calculate(student):
    cw_total = student[2] + student[3] + student[4]
    exam = student[5]
    total = cw_total + exam
    percent = (total / 160) * 100
    if percent >= 70:
        grade = "A"
    elif percent >= 60:
        grade = "B"
    elif percent >= 50:
        grade = "C"
    elif percent >= 40:
        grade = "D"
    else:
        grade = "F"
    return cw_total, exam, total, percent, grade


#Displays all of the students data and marks
def view_all():
    text_box.delete(1.0, tk.END)
    total_percent = 0
    for s in data:
        cw, exam, total, percent, grade = calculate(s)
        total_percent += percent
        text_box.insert(tk.END, f"Name: {s[1]}  |  ID: {s[0]}\n")
        text_box.insert(tk.END, f"Coursework: {cw}, Exam: {exam}, Total: {total}/160\n")
        text_box.insert(tk.END, f"Percentage: {percent:.2f}%  Grade: {grade}\n\n")
    avg = total_percent / len(data)
    text_box.insert(tk.END, f"Total Students: {len(data)} | Average: {avg:.2f}%")


#Displays the student with the highest marks
def show_highest():
    best = max(data, key=lambda s: calculate(s)[2])
    display_student(best)


#Displays the student with the lowest marks
def show_lowest():
    worst = min(data, key=lambda s: calculate(s)[2])
    display_student(worst)


#Displays the data of selected student
def view_one():
    selected_name = combo.get()
    for s in data:
        if s[1] == selected_name:
            display_student(s)
            return
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, "No student selected.")


#Displays the student/s data
def display_student(s):
    cw, exam, total, percent, grade = calculate(s)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, f"Name: {s[1]}\n")
    text_box.insert(tk.END, f"Number: {s[0]}\n")
    text_box.insert(tk.END, f"Coursework Total: {cw}\n")
    text_box.insert(tk.END, f"Exam Mark: {exam}\n")
    text_box.insert(tk.END, f"Overall Percentage: {percent:.2f}%\n")
    text_box.insert(tk.END, f"Grade: {grade}\n")

#Main Program
root = tk.Tk()
root.title("Student Manager")
root.geometry("600x400")
root.config(bg="#ECF0F1")

title = tk.Label(root, text="Student Manager", font=("Arial", 16, "bold"), bg="#ECF0F1")
title.pack(pady=10)

#All the buttons in the program
btn_frame = tk.Frame(root, bg="#ECF0F1")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="View All Student Records", width=20, command=view_all).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Show Highest Score", width=20, command=show_highest).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Show Lowest Score", width=20, command=show_lowest).grid(row=0, column=2, padx=5)


label = tk.Label(root, text="View Individual Student Record:", bg="#ECF0F1", font=("Arial", 11))
label.pack(pady=10)

select_frame = tk.Frame(root, bg="#ECF0F1")
select_frame.pack()

#Select the individual student data
combo = ttk.Combobox(select_frame, values=[s[1] for s in data], width=25)
combo.grid(row=0, column=0, padx=5)

tk.Button(select_frame, text="View Record", command=view_one, width=15).grid(row=0, column=1, padx=5)


text_box = tk.Text(root, width=70, height=12, font=("Courier", 10))
text_box.pack(pady=15)

root.mainloop()
