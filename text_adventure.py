character = input("Welcome to Commaville. Let's see what quests are available, but before we begin, what is your name young traveller?")

def intro():
    print(f"Welcome {character}.")
    
    def quest_choice():
        quest_path = input("Which path would you like to take, north, south east or west? ")
        if(quest_path == "north"):
            print("You chose North")
        elif(quest_path == "south"):
            print("Watch out down there.")
        elif(quest_path == "east"):
            print("Easterino")
        elif(quest_path == "west"):
            print("You chose west")
        else:
            print("hmmm... I didn't catch the direction.")
            quest_choice()
    quest_choice()

intro()