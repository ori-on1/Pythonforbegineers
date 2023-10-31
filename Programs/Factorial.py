
def factorial(n):
  """Returns the factorial of n."""
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial

n = float(input("Enter first number: "))
factorial = factorial(n)

print(f"The factorial of {n} is {factorial}.")