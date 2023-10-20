# Random number generator
import random

x = random.randint(1, 100)  # int
y = random.random()  # float

options = ["rock", "paper", "scissors"]
z = random.choice(options)


print(f"random option: {z}")

cards = list(range(1, 10))
print("Before shuffle:", cards)

random.shuffle(cards)
print("After shuffle:", cards)
