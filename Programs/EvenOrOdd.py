def is_even(n):
  return n % 2 == 0

n = float(input("Enter number: "))
if is_even(n):
  print(f"{n} is an even number.")
else:
  print(f"{n} is an odd number.")