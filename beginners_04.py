operator = input("Please enter the symbol + - * or / here -> ")
num_one = input("Please enter the first number here -> ")
num_two = input("Please enter the second number here -> ")

try:
    if operator == "+":
      print(float(num_one) + float(num_two))
    elif operator == "-":
        print(float(num_one) - float(num_two))
    elif operator == "*":
        print(float(num_one) * float(num_two))
    elif operator == "/":
        print(float(num_one) / float(num_two))
    else:
        print("We can't use that!")
except:
    print("We can't use that!")