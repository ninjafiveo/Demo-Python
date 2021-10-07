import os
import os.path

file_path = "./mydoc.txt"

if(os.path.exists(file_path) == True):
    print("File Exists")
else:
    print("File DOES NOT exist.")
    open("./mydoc.txt","+w")


def Random_Function():
    questions = input("Please ask question to be recorded: ")
    print(f"You asked: {questions}")
    print("Your question has been logged.")
    with open(file_path, 'a') as file:
        file.write(f"{questions}\n")
    What_Next_Yo()

def What_Next_Yo():
    next_choice = input("What would you like to do next? \n A = enter another question. B = Read Back all your notes. C = Exit: \n").lower()

    if(next_choice == "a"):
        Random_Function()
    elif(next_choice == "b"):
        with open(file_path, "r") as file:
            for line in file:
                print(line)
        What_Next_Yo()
    elif(next_choice == "c"):
        print("Thanks for publishing your questions. Good day human.")
        input("")

Random_Function()