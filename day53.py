#Tic-Tac-Toe Game
import tkinter as tk
import random

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
score = {"X": 0, "O": 0}

def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

def is_draw(board):
    for row in board:
        if "" in row:
            return False
    return True

def ai_move():
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "O"
                if check_winner(board) == "O":
                    buttons[r][c].config(text="O")
                    end_game("O")
                    return
                board[r][c] = ""

    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "X"
                if check_winner(board) == "X":
                    board[r][c] = "O"
                    buttons[r][c].config(text="O")
                    return
                board[r][c] = ""

    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    r, c = random.choice(empty)
    board[r][c] = "O"
    buttons[r][c].config(text="O")

def on_click(r, c):
    global current_player

    if board[r][c] != "":
        return

    board[r][c] = "X"
    buttons[r][c].config(text="X")

    winner = check_winner(board)
    if winner:
        end_game(winner)
        return

    if is_draw(board):
        result_label.config(text="Beraberlik!")
        return

    ai_move()

    winner = check_winner(board)
    if winner:
        end_game(winner)
        return

    if is_draw(board):
        result_label.config(text="Beraberlik!")


def end_game(winner):
    score[winner] += 1
    score_label.config(text=f"X: {score['X']}  |  O: {score['O']}")
    result_label.config(text=f"{winner} kazandı!")
    disable_buttons()


def disable_buttons():
    for row in buttons:
        for b in row:
            b.config(state=tk.DISABLED)


def reset_game():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    result_label.config(text="X'in sırası")
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", state=tk.NORMAL)

window = tk.Tk()
window.title("Tic Tac Toe - Day 53")
window.geometry("350x450")

result_label = tk.Label(window, text="X'in sırası", font=("Arial", 16))
result_label.grid(row=0, column=0, columnspan=3)

score_label = tk.Label(window, text="X: 0  |  O: 0", font=("Arial", 14))
score_label.grid(row=1, column=0, columnspan=3)

buttons = [[None for _ in range(3)] for _ in range(3)]

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(
            window,
            text="",
            font=("Arial", 24),
            width=5,
            height=2,
            command=lambda r=r, c=c: on_click(r, c)
        )
        buttons[r][c].grid(row=r+2, column=c)

reset_button = tk.Button(window, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3)

window.mainloop()
