# x = int(input("Please enter your first number: "))
# y = int(input("Second number please: "))
# print(x + y)

height = int(input('Enter your height in inches: '))
weight = int(input('Enter your weight in lbs.: '))

bmi = (weight/(height**2))*703
print('Your BMI is: ' + str(bmi))

if(bmi < 20):
    print("Awesome.")
elif(bmi <30):
    print("Need some working out there.")
elif(bmi < 40):
    print("Uh Oh... better see a doctor.")
else:
    print("Seriously comma need some help. You, might, be, in, a, commmmmmmmmma, soon.")




