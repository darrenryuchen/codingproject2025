import tkinter as tk

# --------- Quiz Data ---------
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Rome", "Madrid", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which of these words are closest to the meaning of'Look'?",
        "options": ["Interrogate", "Welt", "Gaze", "Flourish"],
        "answer": "Gaze"
    },
    {
        "question": "What is 156 divided by 13?",
        "options": ["10", "12", "14", "13"],
        "answer": "12"
    },
    {
        "question": "Who was the first person to step on the moon?",
        "options": ["Buzz Aldrin", "Neil Armstrong", "Joshua Herring", "Gordon Freeman"],
        "answer": "Neil Armstrong"
    },
    {
        "question": "How many bones are in an adult human?",
        "options": ["102", "718", "218", "206"],
        "answer": "206"
    }
]

# --------- Setup Window ---------
window = tk.Tk()
window.title("Beginner Quiz Game")
window.geometry("600x400")

question_label = tk.Label(window, text="", font=("Arial", 16))
question_label.pack(pady=20)

# Option buttons
option1 = tk.Button(window, text="", font=("Arial", 14))
option2 = tk.Button(window, text="", font=("Arial", 14))
option3 = tk.Button(window, text="", font=("Arial", 14))
option4 = tk.Button(window, text="", font=("Arial", 14))

option1.pack(pady=5)
option2.pack(pady=5)
option3.pack(pady=5)
option4.pack(pady=5)

feedback_label = tk.Label(window, text="", font=("Arial", 14))
feedback_label.pack(pady=10)

next_button = tk.Button(window, text="Next", font=("Arial", 14))
next_button.pack(pady=10)

# --------- Game Logic ---------
current_question = 0
score = 0
answer_clicked = False

def show_question():
    global answer_clicked
    answer_clicked = False
    feedback_label.config(text="")
    next_button.config(state="disabled")

    q = quiz_data[current_question]
    question_label.config(text="Q" + str(current_question + 1) + ": " + q["question"])
    
    option1.config(text=q["options"][0], command=lambda: check_answer(q["options"][0]))
    option2.config(text=q["options"][1], command=lambda: check_answer(q["options"][1]))
    option3.config(text=q["options"][2], command=lambda: check_answer(q["options"][2]))
    option4.config(text=q["options"][3], command=lambda: check_answer(q["options"][3]))

def check_answer(selected):
    global score
    global answer_clicked

    if not answer_clicked:
        correct = quiz_data[current_question]["answer"]
        if selected == correct:
            feedback_label.config(text="Correct!", fg="green")
            score += 1
        else:
            feedback_label.config(text="Wrong! Correct: " + correct, fg="red")
        answer_clicked = True
        next_button.config(state="normal")

def next_question():
    global current_question
    current_question += 1
    if current_question < len(quiz_data):
        show_question()
    else:
        question_label.config(text="Quiz finished!")
        option1.pack_forget()
        option2.pack_forget()
        option3.pack_forget()
        option4.pack_forget()
        next_button.pack_forget()
        feedback_label.config(text="Your score: " + str(score) + "/" + str(len(quiz_data)))

next_button.config(command=next_question)

show_question()
window.mainloop()
