import tkinter as tk
from tkinter import messagebox
import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Scissors" and computer_choice == "Paper") or \
            (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, computer_choice)
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")
    play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if not play_again:
        window.quit()
    else:
        reset_game()
def reset_game():
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    result_label.config(text="Result: ")
    play_again_button.config(state="disabled")
user_score = 0
computer_score = 0
window = tk.Tk()
window.title('Rock-Paper-Scissors')
window.geometry('400x400')
tk.Label(window, text='Rock-Paper-Scissors', font=('Arial', 25)).pack(pady=20)
instructions_label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=('Arial', 15))
instructions_label.pack(pady=5)
user_choice_label = tk.Label(window, text="Your choice: ", font=('Arial', 15))
user_choice_label.pack(pady=5)
computer_choice_label = tk.Label(window, text="Computer's choice: ", font=('Arial', 15))
computer_choice_label.pack(pady=5)
result_label = tk.Label(window, text="Result: ", font=('Arial', 15))
result_label.pack(pady=20)
user_score_label = tk.Label(window, text="Your Score: 0", font=('Arial', 15))
user_score_label.pack(pady=5)
computer_score_label = tk.Label(window, text="Computer's Score: 0", font=('Arial', 15))
computer_score_label.pack(pady=5)
button_frame = tk.Frame(window)
button_frame.pack(pady=20)
tk.Button(button_frame, text='Rock', bg='lightblue', font=('Arial', 14), command=lambda: play('Rock')).grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=10)
tk.Button(button_frame, text='Paper', bg='lightgreen', font=('Arial', 14), command=lambda: play('Paper')).grid(row=0,
                                                                                                               column=1,
                                                                                                               padx=10)
tk.Button(button_frame, text='Scissors', bg='lightcoral', font=('Arial', 14), command=lambda: play('Scissors')).grid(
    row=0, column=2, padx=10)
play_again_button = tk.Button(window, text='Play Again', bg='yellow', font=('Arial', 14), command=reset_game,
                              state='disabled')
play_again_button.pack(pady=10)
window.mainloop()