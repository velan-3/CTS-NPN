import random

def numbergame():
    num = random.randint(1,100)
    print(num)
    while True:
        user = int(input("Enter the number you have guessed.."))

        if(num==user):
            print("Absolutely!You are correct")
            numbergame()
        elif(num>user):
            print("It's too high from the correct answer")
        else:
            print("It's too low from the correct answer")   
numbergame()