import math


def shors_classical_simulation(N, a):
  if math.gcd(a, N) > 1:
    return math.gcd(a, N)

  r = 1
  while pow(a, r, N) != 1:
    r += 1

  if r % 2 == 0:
    factor1 = math.gcd(pow(a, r // 2) - 1, N)
    factor2 = math.gcd(pow(a, r // 2) + 1, N)
    if factor1 not in [1, N] and factor2 not in [1, N]:
      return factor1, factor2

  return "Try a different value for 'a'"


print(shors_classical_simulation(15, 7))
