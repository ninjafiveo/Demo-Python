import random



user_question = input("Ask the Magic 8-Ball a question: ")

def eight_ball_replies():
    rand_number = random.randint(1, 9)
    print(rand_number)
    if(rand_number == 1):
        print("First random response")
    elif(rand_number == 2):
        print("2222222222The likelihood is no.")
    elif(rand_number == 3):
        print("3333333333333333The likelihood is no.")
    elif(rand_number == 4):
        print("4444444444444The likelihood is no.")
    elif(rand_number == 5):
        print("555555555555The likelihood is no.")
    elif(rand_number == 6):
        print("6666666666666The likelihood is no.")
    elif(rand_number == 7):
        print("77777777777The likelihood is no.")
    else:
        print("This is the default statement.")


eight_ball_replies()
