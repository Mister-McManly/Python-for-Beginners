unfinished_num = input("Please type your integer here -> ")
try:
    result = abs(int(unfinished_num) % 2)
except:
    print("Thats not an integer!")

try:
    if result == 0:
        print("Even.")
    else:
        print("Odd.")
except:
    pass