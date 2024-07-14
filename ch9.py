
#Factorial can be calculated using the following recursive formula. 
# n! = n * (n – 1)!
# n! = 1 if n = 0 or n = 1


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1) 

resultado = factorial(5)
print(resultado)