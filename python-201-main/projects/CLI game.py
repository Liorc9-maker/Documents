#Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
#Create an inventory for your player, where they can add and remove items.
#Players should be able to collect items they find in rooms and add them to their inventory.
#If they lose a fight against the dragon, then they should lose their inventory items.
#Add more rooms to your game and allow your player to explore.
#Some rooms can be empty, others can contain items, and yet others can contain an opponent.
#Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
#Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an 
# effect on whether your player wins or loses when battling an opponent.


player = input("Please type your name: ")
print(f"Hello {player}. \nWelcome to the game world!")
door = (input("choose between the left or the right door. \nType right/left: ").lower())
while door == "left":
    left_door_coise = (input("You see an empty room. \nType return/look around: ").lower())
    if left_door_coise == "look around":
        print("You look around the empty room and find a sword")
        sword_choise = (input("Take the sword or leave is? \nType yes/no: ").lower())
        if sword_choise == "yes":
            print("You returned and entered the right door \nYou see a dragon in the room.")
            dragon_choise = (input("Fight the dragon or return \nType fight/return: ").lower())
            if dragon_choise == "fight":
                print("You won!!!")    
            break
    else:
        if left_door_coise == "return":
            print("You returned and entered the right door \nYou see a dragon in the room.")
            dragon_choise = input("Fight the dragon or return \nType fight/return: ")
            if dragon_choise == "fight":
                 print("You've been eaten by the dragon! \nYou lost.") 
                 break
        else:
            if dragon_choise == "return":
                print("You went back and entered the left room, you look around and find a sword")
                sword_choise = (input("Take the sworr or leave is? \nType yes/no: ").lower())
                if sword_choise == "yes":
                        print("You returned and entered the right door \nYou see a dragon in the room.")
                        dragon_choise = (input("Fight the dragon or return \nType fight/return: ").lower())
                        if dragon_choise == "fight":
                                print("You won!!!")
                                break    
else: 
    while door == "right":
        print("You returned and entered the right door \nYou see a dragon in the room.")
        dragon_choise = input("Fight the dragon or return \nType fight/return: ")
        if dragon_choise == "fight":
             print("You've been eaten by the dragon! \nYou lost.") 
             break
        else:
            if dragon_choise == "return":
                print("You went back and entered the left room")
                left_door_coise = (input("You see an empty room. \nType return/look around: ").lower())
                if left_door_coise == "look around":
                    print("You've looked around the left room and found a sword.")
                    sword_choise = (input("Take the sword or leave it? \nType yes/no: ").lower())
                    if sword_choise == "yes":
                        print("You returned and entered the right door \nYou see a dragon in the room.")
                        dragon_choise = (input("Fight the dragon or return \nType fight/return: ").lower())
                        if dragon_choise == "fight":
                            print("You won!!!")
                        break
                    elif sword_choise == "no":
                        print("You look around the empty room and find a sword")
                        sword_choise = (input("Take the sword or leave it? \nType yes/no: ").lower())
                        if sword_choise == "yes":
                            print("You returned and entered the right door \nYou see a dragon in the room.")  
                            dragon_choise = (input("Fight the dragon or return \nType fighe/return: ").lower())
                            if dragon_choise == "fight":
                                print("You Won!")
                                break         