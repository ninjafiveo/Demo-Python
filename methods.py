pick_a_number = input("Pick a number: ")

x = 0

def character_name():
    global x
    char_name = input("Please enter your name: ")
    print(f"Hello {char_name}. Welcome to the game.")
    while(x < 3):
        x+=1
        print(x)
        character_name()

    
    # character_name()

if(pick_a_number == "5"):
    character_name()
else:
    print("You did not pick the right number.")



















# def directions_to_timesSq():
#   print("Walk 4 mins to 34th St Herald Square train station.")
#   print("Take the Northbound N, Q, R, or W train 1 stop.")
#   print("Get off the Times Square 42nd Street stop.")
#   print("Take lots of pictures!")

# directions_to_timesSq()



### Passing through Parameters

# def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate , trip_time):
#   car_rental_total = car_rental_rate * trip_time
#   hotel_total = hotel_rate * trip_time - 10
#   print(car_rental_total + hotel_total + plane_ticket_price)

# calculate_expenses(200, 100, 100, 5)