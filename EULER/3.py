import math


def isPrime(num):

    for i in range(2, math.ceil(math.sqrt(num)+1)):
        if num % i == 0:
            return False

    return True


def pFactors(num):
    pf = []
    for i in range(2, math.ceil(math.sqrt(num)+1)):
        if num % i == 0 and isPrime(i):
            pf.append(i)
    return pf


print(pFactors(600851475143)[-1])
