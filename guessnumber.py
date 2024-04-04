import numpy as np # type: ignore

def numbername():
    
    while True:
        num = np.random(1,100)
        print(num)
        user_num = input("Enter the number you have guessed..")
        
        if(num==user_num):
            print("Absolutely!You are correct")
        elif(num>user_num):
            print("It's too high from the correct answer")
        else:
            print("It's too low from the correct answer")   
numbername()     