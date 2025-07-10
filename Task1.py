def factorial(c):
    if c < 2:
        return 1
    else:
        return c * factorial(c-1)
n = int(input("Enter a number:"))
print("The factorial of", n, "is", factorial(n))
