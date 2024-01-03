import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def createDex(window):

    def getPokemon():
        """Retrieves pokemon by name"""

        name = searchBar.get()

        res = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{name.lower()}/")

        if res.status_code == 200:
            myPokemon = res.json()
            name = name.capitalize()
            data = f"Name: {name} \nID: {myPokemon['id']}\nSpecies: {myPokemon['genera'][7]['genus']}"
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, data)
        else:
            data = "Invalid Pokemon. Please try again."
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, data)
    def getNextPokemon():
        pass

    """Function to create pokedex"""
    window.title("PokeDex")
    window.geometry("365x500")

    #Creates Red Frame
    red_frame = tk.Frame(window, bg="#FF0000", padx=10, pady=10)
    red_frame.pack(fill=tk.BOTH, expand=True)

    #Creates Yellow Textbox 
    text_box = tk.Text(red_frame, wrap=tk.WORD, width=40, height=10, bg="#FFD700")
    text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    #Creats search bar
    searchBar = tk.Entry(red_frame)
    searchBar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    #Creats button for submissions
    clickButton = tk.Button(red_frame, text = "Submit", command = getPokemon)
    clickButton.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10)

    right_arrow_button = tk.Button(red_frame, text="->", command=getNextPokemon)
    right_arrow_button.grid(row = 5, column = 1, columnspan = 1, padx = 5, pady = 10)

    left_arrow_button = tk.Button(red_frame, text="<-", command=getNextPokemon)
    left_arrow_button.grid(row = 5, column = 0, columnspan = 1, padx = 5, pady = 10)


window = tk.Tk()
createDex(window)
window.mainloop()



