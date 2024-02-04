num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1*n2, num1, num2)
print(list(result))


# for multiplication 

num1 = [4, 5, 6]
num2 = [5, 6, 7]
num3 = [1, 2, 3]

result = map(lambda n1,n2,n3: n1*n2*3, num1, num2 ,num3)
print(list(result))

