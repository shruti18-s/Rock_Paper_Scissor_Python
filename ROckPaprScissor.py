import random
import tkinter as tk

# Define possible choices
choices = ["Rock", "Paper", "Scissors"]

# Define initial scores
human_score = 0
computer_score = 0

# Define function to update scores
def update_scores(winner):
    global human_score, computer_score
    if winner == "human":
        human_score += 1
    elif winner == "computer":
        computer_score += 1
    human_score_label.config(text="Human: " + str(human_score))
    computer_score_label.config(text="Computer: " + str(computer_score))

# Define function to handle game logic
def play_game(human_choice):
    # Get computer choice
    computer_choice = random.choice(choices)
    # Determine winner
    if human_choice == computer_choice:
        result = "tie"
    elif human_choice == "Rock" and computer_choice == "Scissors":
        result = "human"
    elif human_choice == "Paper" and computer_choice == "Rock":
        result = "human"
    elif human_choice == "Scissors" and computer_choice == "Paper":
        result = "human"
    else:
        result = "computer"
    # Update scores
    update_scores(result)
    # Update labels to show choices
    human_choice_label.config(text="Your choice: " + human_choice)
    computer_choice_label.config(text="Computer's choice: " + computer_choice)
    # Display result
    if result == "tie":
        result_label.config(text="It's a tie!", fg="blue")
    elif result == "human":
        result_label.config(text="You win!", fg="green")
    else:
        result_label.config(text="Computer wins!", fg="red")

# Create window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create labels
human_choice_label = tk.Label(window, text="Your choice: ")
computer_choice_label = tk.Label(window, text="Computer's choice: ")
result_label = tk.Label(window, text="")
human_score_label = tk.Label(window, text="Human: 0")
computer_score_label = tk.Label(window, text="Computer: 0")

# Create buttons
rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"), fg="blue")
paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"),  fg="blue")
scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"), fg="blue")

# Add labels and buttons to window
human_choice_label.pack()
computer_choice_label.pack()
result_label.pack()
human_score_label.pack()
computer_score_label.pack()
rock_button.pack(side="left")
paper_button.pack(side="left")
scissors_button.pack(side="left")

# Start window
window.mainloop()
