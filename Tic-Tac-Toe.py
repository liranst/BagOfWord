import random
from tkinter import *
from tkinter import messagebox

class TIC_TAC_TOE:
    def __init__(self):
       self.yourplay = True
       self.root = Tk()
       self.root.title('Tic-Tac-Toe')
       self.root.iconbitmap()
       self.buttons = self.buttons = [Button(self.root, text=" ", font=("Helvetica", 40), height=3, width=6, bg="SystemButtonFace",
                               command=lambda i=_: self.b_click(i)) for _ in range(9)]
       for i in range(9):
            self.buttons[i].grid(row=i // 3, column=i % 3)

       self.my_menu = Menu(self.root)
       self.root.config(menu=self.my_menu)
       self.options_menu = Menu(self.my_menu, tearoff=0)
       self.my_menu.add_cascade(label="Options", menu=self.options_menu)
       self.options_menu.add_command(label="Reset Game", command=self.reset)
       self.root.mainloop()

    def reset(self):
        self.buttons = [Button(self.root, text=" ", font=("Helvetica", 40), height=3, width=6, bg="SystemButtonFace",
                               command=lambda i=_: self.b_click(i)) for _ in range(9)]
        for i in range(9):
            self.buttons[i].grid(row=i // 3, column=i % 3)

    def children(self,arr, tune=False, H=None):
        if H == None:
            H = []
        marker = "X" if tune else "O"
        for i in range(len(arr)):
            new_arr = arr[:]
            if new_arr[i] != "X" and new_arr[i] != "O":
                new_arr[i] = marker
                H.append(new_arr)
        return H
    def game_over(self,board, marker):
        winning_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
        ]
        for sequence in winning_positions:
            a, b, c = sequence
            if board[a] == board[b] == board[c] == marker:
                return 1 if marker == "X" else -1
        if all(value == "X" or value == "O" for value in board):
            return 0
    def player_MAX(self,start):
        end = self.game_over(board= start, marker= "X")
        if end == 1: return -1
        if end == 0: return 0
        max_eval = -100
        for move in self.children(start, tune=False):
            new_state = move
            eval = self.player_MIN(new_state)
            max_eval = max(max_eval, eval)
        return max_eval
    def player_MIN(self,start):
        end = self.game_over(start, "O")
        if end == -1: return 1
        if end == 0: return 0
        min_eval = 100
        for move in self.children(start, True):
            new_state = move
            eval = self.player_MAX(new_state)
            min_eval = min(min_eval, eval)
        return min_eval
    def minmax_decision(self,initial_state, best_move=None, best_score=-100, player_X=False):
        """
        :param initial_state: starting position
        :return: the *operation* of the highest value
        """
        if best_move is None:
            best_move = []
        for move in self.children(initial_state, player_X):
            new_state = move
            score = self.player_MIN(new_state)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
    def computer(self):
        list_bord = [self.buttons[i]["text"] for i in range(9)]

        board_options = []
        for i in range(len(list_bord)):
            if list_bord[i] != "X" or list_bord[i] != "O":
                board_options.append(i)
        new_board_after_computer_course = self.minmax_decision(list_bord)
        lok = 0
        for i in range(9):
            if list_bord[i] != new_board_after_computer_course[i]:
                lok = i
        self.buttons[lok]["text"] = "O"

    def break_games(self):
        for i in range(9):
            self.buttons[i].config(state=DISABLED)

    def checkifwon(self):
        marker = "X" if  self.yourplay else "O"
        winning_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
        ]
        for sequence in winning_positions:
            a, b, c = sequence
            if self.buttons[a]["text"] == marker and self.buttons[b]["text"] == marker and self.buttons[c]["text"] == marker:
                print("Tic Tac Toe", "you winner!")
                self.buttons[a].config(bg="red" if self.yourplay else "green")
                self.buttons[b].config(bg="red" if self.yourplay else "green")
                self.buttons[c].config(bg="red" if self.yourplay else "green")
                return 1 if marker == "x" else -1

    def b_click(self,i):
        b = self.buttons[i]
        if b["text"] == " " and  self.yourplay:
            b["text"] = "X"
            if self.checkifwon() == 1:
                self.break_games()
            self.yourplay = not self.yourplay

        if not self.yourplay:
            self.computer()
            if  self.checkifwon() == -1:
                self.break_games()
            self.yourplay = not self.yourplay
        else:
            messagebox.showerror("Tic Tac Toe", "Hey!")

x =   TIC_TAC_TOE()