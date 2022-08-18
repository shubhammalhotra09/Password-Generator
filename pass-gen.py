import random


char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&'()"

while 1:
    password_len = int(input("How long would you like to set the password?"))
    password_count = int(input("How many would you like to have : "))

    for x in range (0, password_count):
        password = ""
        for x in range(0, password_len):
            password_charr = random.choice(char)
            password = password + password_charr
        print("Your new password :",password)
