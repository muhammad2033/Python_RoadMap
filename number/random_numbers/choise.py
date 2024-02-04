import random

print(" choice any value randomly from  range(200) :", random.choice(range(0,200,2)))

print(" choice any value randomly from  list[1,2,3,4,5,6,11,12,13,14,15,22,222,223,444,555,567]      :", random.choice([1,2,3,4,5,6,11,12,13,14,15,22,222,223,444,555,567]))

print(" choice any value randomly from  tuple(1,2,3,4,5,6,11,12,13,14,15,22,222,223,444,555,567)      :", random.choice((1,2,3,4,5,6,11,12,13,14,15,22,222,223,444,555,567)))

print("choice any letter from the given string 'my name is maaz '   : ", random.choice("my name is maaz"))