import requests
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from deepfake import getName, getLogin
import io

ID = 0;

def createDex(window):


    def requestPokemon(type):
        global ID
        if type == "submit":
            #Gets data for the pokemon
            name = searchBar.get()
            res = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{name.lower()}/")
        elif type == 'left':
            res = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{ID - 1}/")
        elif type == 'right':
            res = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{ID + 1}/")

        if res.status_code == 200:

            myPokemon = res.json()

            #Stores ID in global
            ID = int(myPokemon['id'])

            Name = myPokemon['name'].capitalize()
            Species = myPokemon['genera'][7]['genus']
            data_entry = getPokemonEntry(myPokemon['flavor_text_entries'])
            
            #Output for data
            data = f"Name: {Name} \nID: {ID}\nSpecies: {Species}\n\n{data_entry}"

            #Deletes old output and outputs the new data
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, data)

            createSprite(ID)
            getName(f"{Name}, The {Species}")
        else:
            data = "Invalid Pokemon. Please try again."
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, data)    

    def getPokemon():
        """Retrieves pokemon by name"""
        requestPokemon('submit')
            
    def getNextPokemon():
        """Gets data for next pokemon in the dex"""
        requestPokemon('right')

    def getPreviousPokemon():
        """Gets data for previous pokemon in the dex"""
        requestPokemon('left')

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

        image = Image.open(io.BytesIO(raw_data))

        resized_image = image.resize((250, 250))

        #Sets sprite to the sprite_label
        photo = ImageTk.PhotoImage(resized_image)
        sprite_label.config(image=photo , bg = '#30fa06')
        sprite_label.image = photo

    def getPokemonEntry(data):
         #Searches for English Pokedex entry in json file
            for index, entry in enumerate(data):
                if entry['language']['name'] == 'en':
                    return data[index]['flavor_text']
                    
    window.title("PokeDex")
    window.geometry("800x600")

    red_frame = tk.Frame(window, bg="black", padx=5, pady=5)
    red_frame.pack(fill=tk.BOTH, expand=True)

    photo = ImageTk.PhotoImage(Image.open('WIP Projects\Pokedex\pokedex.jpg'))
    background_label = tk.Label(red_frame, image=photo)
    background_label.pack(fill=tk.BOTH, expand=True)
    background_label.image = photo

    text_box = tk.Text(red_frame, wrap=tk.WORD, width=41, height=21, bg="#ffffff")
    text_box.place(x=25, y=147)

    #Creats search bar
    searchBar = tk.Entry(red_frame,border=4)
    searchBar.place(x=625,y=40)

    #Creats button for submissions
    clickButton = tk.Button(red_frame, text = "Submit", command = getPokemon)
    clickButton.place(x = 660, y=65)

    #Creats a left arrow button for navigation
    left_arrow_button = tk.Button(red_frame, text="<-", command=getPreviousPokemon)
    left_arrow_button.place(x=125,y=500)

    #Creats a right arrow button for navigation
    right_arrow_button = tk.Button(red_frame, text="->", command=getNextPokemon)
    right_arrow_button.place(x=225,y=500)

    #Creats an image box to view sprite
    sprite_label =  tk.Label(red_frame,bg='#30fa06')
    sprite_label.place(x=485,y=225)

window = tk.Tk()
createDex(window)
window.resizable('False','False')
getLogin()
window.mainloop()