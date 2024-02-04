import random

random.seed()

print("the random number with default seed :", random.random())

random.seed(15)

print("the random number with default seed :", random.random())

random.seed("maaz")

print("the random number with default seed :", random.random())
