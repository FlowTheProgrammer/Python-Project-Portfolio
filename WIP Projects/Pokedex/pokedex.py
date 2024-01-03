import requests
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen

ID = 0;

def createDex(window):
    """Creates the pokedex layout"""

    def getPokemon():
        """Retrieves pokemon by name"""

        #Gets data for the pokemon
        name = searchBar.get()
        res = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{name.lower()}/")

        #Error Code Check
        if res.status_code == 200:

            myPokemon = res.json()

            #Stores ID in global
            global ID
            ID = int(myPokemon['id'])

            #Output for data
            data = f"Name: {myPokemon['name'].capitalize()} \nID: {myPokemon['id']}\nSpecies: {myPokemon['genera'][7]['genus']}"

            #Deletes old output and outputs the new data
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, data)
            createSprite(ID)

        #Outputs and error if pokemon not found
        else:
            data = "Invalid Pokemon. Please try again."
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, data)
            
    def getNextPokemonRight():
        """Gets data for next pokemon in the dex"""

        global ID

        #Gets data for the previous pokemon
        res = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{ID + 1}/")

        
        if res.status_code == 200:

            myPokemon = res.json()

            #Stores ID in global
            ID = int(myPokemon['id'])

            #Output for data
            data = f"Name: {myPokemon['name'].capitalize()} \nID: {myPokemon['id']}\nSpecies: {myPokemon['genera'][7]['genus']}"

            #Deletes old output and outputs the new data
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, data)
            createSprite(ID)

    def getNextPokemonLeft():
        """Gets data for previous pokemon in the dex"""

        global ID

        #Gets data for the previous pokemon
        res = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{ID - 1}/")

        #Error Code Check
        if res.status_code == 200:

            myPokemon = res.json()

            #Stores ID in global
            ID = int(myPokemon['id'])

            #Output for data
            data = f"Name: {myPokemon['name'].capitalize()} \nID: {myPokemon['id']}\nSpecies: {myPokemon['genera'][7]['genus']}"

            #Deletes old output and outputs the new data
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, data)
            createSprite(ID)

    def createSprite(sprite):
        """Function to get sprite from api"""

        #Gets pokemon
        res = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{sprite}/")

        #Gets link for sprite
        myPokemon = res.json()
        sprite = myPokemon["sprites"]["front_default"]

        #Reads the data from the api link
        u = urlopen(sprite)
        raw_data = u.read()
        u.close()

        #Sets sprite to the sprite_label
        photo = ImageTk.PhotoImage(data = raw_data)
        sprite_label.config(image=photo)
        sprite_label.image = photo


    #Creates outline for the Dex
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

    #Creats a right arrow button for navigation
    right_arrow_button = tk.Button(red_frame, text="->", command=getNextPokemonRight)
    right_arrow_button.grid(row = 5, column = 1, columnspan = 1, padx = 5, pady = 10)

    #Creats a left arrow button for navigation
    left_arrow_button = tk.Button(red_frame, text="<-", command=getNextPokemonLeft)
    left_arrow_button.grid(row = 5, column = 0, columnspan = 1, padx = 5, pady = 10)

    #Creats an image box to view sprite
    sprite_label =  tk.Label(red_frame)
    sprite_label.grid(row=2, column=0, columnspan=2, pady=10)


#Main Code - Creates Pokedex
window = tk.Tk()
createDex(window)
window.mainloop()