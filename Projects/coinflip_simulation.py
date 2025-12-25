##this program simulates a coin toss: ≈ 50% of the time, it's "Heads", ≈ 50% of the time, it's "Tails"

import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')
