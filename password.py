import random as random

def generatePass(num):
    chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()-=_+"
    print(''.join([random.choice(chars) for i in range(num)]))

num = int(input("Give me the number of chars that you want in your password: "))
generatePass(num)