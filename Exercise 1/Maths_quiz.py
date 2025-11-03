import tkinter as tk
import random

#Displays the difficulty selection menu
def displayMenu():
    clear_display()
    tk.Label(root, text="Select Difficulty", font=("Arial", 14)).pack(pady=10)
    tk.Radiobutton(root, text="1. Easy ", variable=difficulty, value=1).pack()
    tk.Radiobutton(root, text="2. Moderate ", variable=difficulty, value=2).pack()
    tk.Radiobutton(root, text="3. Advanced ", variable=difficulty, value=3).pack()
    tk.Button(root, text="Click to Start", command=start_quiz).pack(pady=10)


#Returns two random integers depends on selected difficulty
def randomInt():
    if difficulty.get() == 1:
        return random.randint(1,9), random.randint(1,9)
    elif difficulty.get() == 2:
        return random.randint(10,99), random.randint(10,99)
    else:
        return random.randint(1000, 9999), random.randint(1000,9999)


#Decides random operations to use. Wheter to add or to subtract
def decideOperation():
    return random.choice(["+", "-"])


#Displays new problem
def displayProblem():
    global num1, num2, operation, attempts
    num1, num2 = randomInt()
    operation = decideOperation()
    attempts = 0
    clear_display()

    tk.Label(root, text=f"Question {current_question.get()} out of 10.", font=("Arial", 17)).pack(pady=5)
    tk.Label(root, text=f"{num1} {operation} {num2} =", font=("Arial", 16)).pack(pady=10)

    answer_entry.pack()
    submit_button.pack(pady=5)
    feedback_label.pack()


#To check if the user inputted the correct or wrong answer
def IsCorrect():
    global score, attempts
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        feedback_label.config(text="Enter a number.", fg="red")
        return
    
    correct_answer = num1 + num2 if operation == "+" else num1 - num2
    attempts += 1

    if user_answer == correct_answer:
        if attempts == 1:
            score += 10
        else:
            score += 5
        feedback_label.config(text="Correct Answer!")
        next_question()
    else:
        if attempts == 1:
            feedback_label.config(text="Wrong Answer! You have 1 more attempt.")
        else:
            feedback_label.config(text=f"Wrong! The answer was {correct_answer}")
            next_question()


#Go to the next question
def next_question():
    answer_entry.delete(0, tk.END)
    root.after(1000, lambda: continue_quiz())


#Continues to the next question 
def continue_quiz():
    if current_question.get() < 10:
        current_question.set(current_question.get() + 1)
        displayProblem()
    else:
        displayResults()


#Display the final score and grade when finished
def displayResults():
    clear_display()
    grade = get_grade(score)
    tk.Label(root, text=f"Overall Score: {score}/100", font=("Arial", 14)).pack(pady=10)
    tk.Label(root, text=f"Grade: {grade}", font=("Arial", 12)).pack(pady=5)
    tk.Button(root, text="Start Again", command=restart_quiz).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)


#Return grade based on the score gotten
def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"
    

#Initiate quiz variables
def start_quiz():
    global score
    score = 0
    current_question.set(1)
    displayProblem()


#Restarts the quiz to start again
def restart_quiz():
    global score
    score = 0
    current_question.set(1)
    displayMenu()


#remove all widgets
def clear_display():
    for widget in root.winfo_children():
        widget.pack_forget()



root = tk.Tk()
root.title("Maths Quiz Program")
root.geometry("400x400")

difficulty = tk.IntVar()
current_question = tk.IntVar(value=1)
score = 0
attempts = 0
num1 = num2 = 0
operation = ""

answer_entry = tk.Entry(root)
submit_button = tk.Button(root, text="Submit", command=IsCorrect, font=("Arial", 15))
feedback_label = tk.Label(root, text="", font=("Arial", 11))

displayMenu()
root.mainloop()