def is_prime(n):
  """Returns True if n is a prime number, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


def is_composite(n):
  """Returns True if n is a composite number, False otherwise."""
  return not is_prime(n)