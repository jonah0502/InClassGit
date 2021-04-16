def printDivisors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i)
        i = i + 1

number = int(input("Give me a number to find the divisors of: "))
printDivisors(number)