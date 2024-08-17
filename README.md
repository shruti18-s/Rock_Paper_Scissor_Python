# Rock, Paper, Scissors Game

This is a simple Rock, Paper, Scissors game implemented in Python using the Tkinter library for the graphical user interface (GUI). The game allows a user to play against the computer, and it keeps track of the scores.

## How the Game Works

- The game presents three buttons: **Rock**, **Paper**, and **Scissors**.
- The player selects one of these options by clicking on the respective button.
- The computer randomly selects one of the three choices.
- The game then determines the winner based on the standard rules of Rock, Paper, Scissors:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- The scores are updated after each round, and the result of each round is displayed.

## Code Explanation

The core of the game is implemented using the following components:

- **Choices**: The three possible choices (Rock, Paper, Scissors) are stored in a list.
- **Score Tracking**: The game keeps track of both the human and computer scores.
- **Game Logic**: The function `play_game()` determines the winner of each round by comparing the player’s choice with the computer’s random choice.
- **GUI**: Tkinter is used to create the GUI, including buttons for each choice, labels to display choices and results, and labels to show the current scores.

### Main Functions:

1. **`update_scores(winner)`**: Updates the score based on who won the round (human or computer).
2. **`play_game(human_choice)`**: Handles the game logic, updates the GUI with the choices and the result, and calls `update_scores()`.

### GUI Components:

- **Labels**: Display the player's choice, the computer's choice, and the result of the round.
- **Buttons**: Allow the player to select Rock, Paper, or Scissors.

## How to Download and Run the Code

### Prerequisites

- **Python 3.x**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Run

1. **Clone the Repository**:
    ```bash
    git clone https://https://github.com/shruti18-s/Rock_Paper_Scissor_Python.git
    cd rock-paper-scissors
    ```

2. **Run the Game**:
    - Open a terminal or command prompt.
    - Navigate to the directory where you cloned the repository.
    - Run the following command to start the game:
    ```bash
    python rock_paper_scissors.py
    ```

    The game window will appear, and you can start playing by clicking on one of the buttons.
