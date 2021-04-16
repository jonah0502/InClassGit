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
print("The sum of all basic operations is: {}".format(calc(a,b)))