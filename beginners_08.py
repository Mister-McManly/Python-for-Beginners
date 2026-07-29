password = input("Please enter a safe password with 8 characters and at least one number. ")
numbers = set("0123456789")
if len(password) >= 8 and (set(password) & numbers):
    print("This is a usable password!")
else:
    print("Unnacepptable password, either shorter than 8 characters or has no number.")
 