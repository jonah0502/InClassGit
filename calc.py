def calc(a,b):
    list = []
    lSum = 0
    addSum = a + b
    difference = a - b
    multiply = a*b
    divide = a / b
    list.append(addSum)
    list.append(difference)
    list.append(multiply)
    list.append(divide)
    lSum = sum(list)
    return lSum

a = int(input("Give me the first number: "))
b = int(input("Give me the second number: "))
while b == 0:
    b = int(input("Cannot divide by 0 enter input 2 again: "))
print("The sum of all basic operations is: {}".format(calc(a,b)))