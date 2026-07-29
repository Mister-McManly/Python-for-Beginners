import random

number = random.randint(0, 100)
guess = int(input("Please guess the positive interger between 1 & 100 i'm thinking of! "))
while  guess != number:
    try:
        if guess < number:
            print("Higher! ")
            guess = int(input("Try again! "))
        elif guess > number:
            print("Lower! ")
            guess = int(input("Try again! "))
        else:
            break            
    except:
        print("Thats not a positive interger! ")
        guess = int(input("Try again this time correctly! "))
print("You got it!")