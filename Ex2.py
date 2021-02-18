#--------------------------------
#EXERCICE 2
#LEONIDAS PASTRAS
#P20155
#18-2-2021
#--------------------------------
import random

n = int(input("Enter a number (anything over 30 might or might not crash your computer): "))
i = 1
num = [0, 1]
p = num[1]
def Fibonacci(i, p):
    if i < n:
        i = i + 1
        tempNum = num[1]
        num[1] = num[1] + num[0]
        num[0] = tempNum
        Fibonacci(i, p)
    else:
        CheckIfPrime(num[1])
def CheckIfPrime(p):
    isPrime = True
    j = 0
    while isPrime and j < 20:
        a = random.randint(0, 1000000) #1 million
        isPrime = (a ** p) % p == (a % p)
        UnnecessaryMessage(a, isPrime)
        j = j + 1
    if isPrime:
        print("The term", n, "of the Fibonacci sequence is", p, "and it is a Prime number! :D")
    else:
        print("The term", n, "of the Fibonacci sequence is", p, "and it is NOT a Prime number! :(")
def UnnecessaryMessage(a, isPrime):
    if isPrime:
        print("The random number", a, "does satisfy the equation")
    else:
        print("The random number", a, "does NOT satisfy the equation")
Fibonacci(i, p)
