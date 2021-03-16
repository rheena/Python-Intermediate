'''
Recursion is the technique of a function calling itself.
Non-recursive way to get a factorial would be 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
Recursive way to get a factorial would be 9! = 9 * 8!
'''

#Non-recursive way to get a factorial
n = 7
fact = 1
while n > 0:
    fact = fact * n
    n -= 1

print(fact)

#Recursive way to get a factorial
def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(7))

#Fibonacci sequence in an iterative way
def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

print(fibonacci(2))

#Fibonacci sequence in a recursive way
def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return (fibonacci2(n-1) + fibonacci2(n - 2))

print(fibonacci2(2))