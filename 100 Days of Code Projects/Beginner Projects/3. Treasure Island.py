"""
Simple Choose your own Adventure
If/Else Statements
Beginner Project: 
There are no try/except
Assume correct inputs
"""

print("Welcome to Tresure Island!")
print("__________________________")
print("Your task is to find the mysterious tresure!\n")

print("You have landed in the middle of desert where there is no clear path.")
print("However your gut is telling you to make a choice. You must either go left or right.")
choice = input("\nWhich do you choose?:\n")

if choice.lower() == 'left':
    print("\nYou arrive at a a river, it looks deep but you are certain you can cross it.")
    print("In the distance, you see a pyramid, it looks promising. You need to make a decision.")
    choice = input("\nDo you choose to swim or wait?:\n")
    if choice.lower() == "swim":
        print("\nThe current swept you off your feet and you were carried under, leading to your demise. The End.")
    elif choice.lower() == "wait":
        print("\nYou wait and waited. Eventually a mysterious man in a boat comes and offers you a ride. Relunctantly you accept.")
        print("He brings you over, thankfully unscaved and you get out the boat.")
        print("You walk into the the pyramid where you are met with three passage ways.")
        print("\nYou need to find the tresure, which way do you go?")

        choice = input("Left, right or middle?: \n")
        if choice.lower() == "left":
            print("\nYou walk into a room full of quicksand where you began to sink as you cry out for help. The End")
        elif choice.lower() == "right":
            print("\nYou step into the room and the door slams shut. As you scream and pound on the door, the room beings to fill with a mysterious gas. The End.")
        elif choice.lower() == "middle":
            print("\nYou walk into the room and you see the treasure. You walk up to it and grab it, but everything goes dark and all the doors slam shut.")
            print("You collapse to the floor as you hear the soft whisper of someone saying 'No one ever wins' ")
            print("\nTrue Ending. The End.")

elif choice.lower() == 'right':
    print("You traveled for days without water and collapsed. The End.")