import tkinter as tk
from tkinter import messagebox
import random

#CONSTANT VARS
BG_COLOR = '#121213'
WRONG_COLOR = '#403c3c'
IN_WORD_COLOR = '#b89c3c'
RIGHT_COLOR = '#588c4c'

#List of letters
alphabet = ['q', 'w', 'e', 'r', 't', 'y', 
            'u', 'i','o', 'p', 'a', 's', 
            'd', 'f', 'g', 'h', 'j', 'k', 
            'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

#Keyboard Layout
qwerty_layout = [
    'QWERTYUIOP',
    'ASDFGHJKL',
    'ZXCVBNM'
]

keyboard_dict = {
    'q': 0, 'w': 1, 'e': 2, 'r': 3, 't': 4, 'y': 5, 'u': 6, 'i': 7, 'o': 8, 'p': 9,
    'a': 10, 's': 11, 'd': 12, 'f': 13, 'g': 14, 'h': 15, 'j': 16, 'k': 17, 'l': 18,
    'z': 19, 'x': 20, 'c': 21, 'v': 22, 'b': 23, 'n': 24, 'm': 25
}


class GameBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wordle Game")
        self.geometry("1920x1080")

        #Variables
        self.boxes = []
        self.buttons = []
        self.current_row = 0
        self.current_col = 0
        self.current_letters = 0
        self.word = ''
        self.cpy_word = self.word
        self.answer = self.get_random_word()
        self.check_answer = self.answer
        self.game_end = False
        print(self.answer)



        #Background color for game
        background_color = tk.Frame(self, bg=BG_COLOR, padx=10, pady=10)
        background_color.pack(fill=tk.BOTH, expand=True)

        #Title Creation
        self.title = tk.Label(background_color, text="WORDLE", font=("comic-sans", 16, "bold"), fg = 'white', bg =BG_COLOR )
        self.title.pack(pady=100)

         #Text Box Layout

        for i in range(6):
            frame = tk.Frame(background_color, bg='black')
            frame.pack(side=tk.TOP, pady=1)

            box_in_row = []

            for j in range(5):
                box = tk.Text(frame, width=8, height = 4, 
                              font=("Helvetica", 13, "bold"), fg = 'white', background=BG_COLOR)
                box.grid(row=i, column=j, padx=1, pady=1)
                box_in_row.append(box)
                
            self.boxes.append(box_in_row)

        #Keyboard Layout 
        for row in qwerty_layout:
            frame = tk.Frame(background_color, bg = BG_COLOR)
            frame.pack(side=tk.TOP, pady=5)
    
            for letter in row:
                button = tk.Button(frame, text=letter, width=5, height=2, 
                                   command=lambda l=letter: self.add_Letter(l) ,
                                   bg='grey', fg = 'white', font = ('bold'))
                button.pack(side=tk.LEFT, padx=2)
                self.buttons.append(button)
        

        #Frame for Backspace and Enter
        frame = tk.Frame(background_color, bg = BG_COLOR)
        frame.pack(side=tk.TOP, pady=1)

        backspace_button = tk.Button(frame, text="Backspace", width=10, height=2, bg='grey', fg = 'white', font = ('bold'), command=self.del_letter)
        backspace_button.pack(side=tk.LEFT, padx=2, pady=1)

        enter_button = tk.Button(frame, text="Enter", width=5, height=2, bg='grey', fg = 'white', font = ('bold'), command=self.submit_answer)
        enter_button.pack(side=tk.LEFT, padx=2, pady=1)


    #METHODS
            
    def add_Letter(self,letter):
        """Function to add letters to a box in the gameboard"""
        if not self.game_end:
            if self. current_col < 5:

                self.boxes[self.current_row][self.current_col].tag_configure("center", justify='center')
                self.boxes[self.current_row][self.current_col].insert(tk.END, f'\n\n{letter}')
                self.boxes[self.current_row][self.current_col].tag_add("center", "1.0", "end")
                self.current_col +=1
                self.current_letters += 1
                self.word += letter

    def del_letter(self):
        """Function to delete a letter from the word"""
        if not self.game_end:
            if self.current_col > 0:
                self.current_col -= 1
                self.current_letters -= 1
                self.boxes[self.current_row][self.current_col].delete(1.0, tk.END)
                self.word = self.word[:-1]
            else:
                if self.current_letters == 1:
                    self.current_letters -= 1
                    self.word = self.word[:-1]
                self.boxes[self.current_row][self.current_col].delete(1.0, tk.END)

    def get_random_word(self):
        with open('WIP Projects\Wordle/word-list.txt', 'r') as file:
                content = file.read().split()
                return random.choice(content)

    def in_word_list(self):
        with open('WIP Projects\Wordle\word-list.txt', 'r') as file:
                content = file.read()
                return self.word.lower() in content

    def submit_answer(self):

        if not self.game_end:
            #Checks to see if word is unfinished
            if self.current_letters != 5:
                messagebox.showerror('Error', 'Not Enough Letters in Words!')

            #Checks if the  user guessed the right word
            elif self.word.lower() == self.answer.lower():
                self.change_box_layout()
                messagebox.showerror('Winner!', 'You Won!')
                self.game_end = True

            #Checks if user's word is in the word list
            elif self.in_word_list():
                self.change_box_layout()
                self.current_row += 1
                self.current_col = 0
                self.current_letters = 0
                self.word = ''
                self.checkLoss()
            else:
                messagebox.showerror('Sorry!', 'Word not in word list')

    def change_box_layout(self):
        self.cpy_word = self.word
        for index, letter in enumerate(self.word.lower()):
            if self.word.lower()[index] == self.check_answer[index]:
                    self.buttons[keyboard_dict[letter]].config(bg=RIGHT_COLOR)
                    self.check_answer = self.check_answer[:index] + '?' + self.check_answer[index + 1:]
                    self.cpy_word = self.cpy_word[:index] + '!' + self.cpy_word[index + 1:]
                    self.boxes[self.current_row][index].config(bg=RIGHT_COLOR)


        for index, letter in enumerate(self.word.lower()):
            pos = self.where_in_position(index)
            if pos == 'none':
                if self.boxes[self.current_row][index].cget("bg") == RIGHT_COLOR:
                    pass
                else:
                    self.boxes[self.current_row][index].config(bg=WRONG_COLOR)

            elif pos == 'in':
                self.boxes[self.current_row][index].config(bg=IN_WORD_COLOR)

            elif pos == 'correct':
                self.boxes[self.current_row][index].config(bg=RIGHT_COLOR)


        self.check_answer = self.answer
        self.cpy_word = self.word


    def where_in_position(self,index):
        print(self.check_answer)
        if self.cpy_word.lower()[index] not in self.check_answer:
            if self.cpy_word.lower()[index] != "!":
                self.buttons[keyboard_dict[self.cpy_word.lower()[index]]].config(bg = WRONG_COLOR)
            return "none"
        
        elif self.cpy_word.lower()[index] in self.check_answer:
            self.check_answer = self.check_answer.replace(self.cpy_word.lower()[index],'?',1)
            self.buttons[keyboard_dict[self.cpy_word.lower()[index]]].config(bg = IN_WORD_COLOR)
            return 'in'
        

    def checkLoss(self):
        if self.current_row >= 6:
            messagebox.showerror('Oops!', f'You lost! The answer was {self.answer}')
            self.game_end = True
            
        

#Game Creation
myBoard = GameBoard()
myBoard.mainloop()