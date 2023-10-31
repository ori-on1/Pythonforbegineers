def is_positive(n):
  """Returns True if n is a positive number, False otherwise."""
  return n > 0


def is_negative(n):
  """Returns True if n is a negative number, False otherwise."""
  return n < 0

n= float(input("Enter  number: "))
if is_positive(n):
  print(f"{n} is a positive number.")
elif is_negative(n):
  print(f"{n} is a negative number.")
else:
  print(f"{n} is zero.")