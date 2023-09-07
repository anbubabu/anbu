def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)
if _name_ == '_main_':
    n = 5
    print(f'The Factorial of {n} is', factorial(n))
  