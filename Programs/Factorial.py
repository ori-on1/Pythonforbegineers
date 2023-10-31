
def factorial(n):
  """Returns the factorial of n."""
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial