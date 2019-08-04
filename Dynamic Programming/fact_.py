def fact_(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    fact = n
    print (fact)
    for i in reversed(range(2, n)):
        fact *= i 

    return fact

print(fact_(6))