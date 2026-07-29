import time

countdown = input("Please enter how long you want to count down from in seconds. ")

try:
    countdown = int(countdown)
    while countdown >= 1:
        print(countdown)
        countdown -= 1
        time.sleep(1)
    print("Blastoff!")
except:
    print("That's not a poitive interger!")