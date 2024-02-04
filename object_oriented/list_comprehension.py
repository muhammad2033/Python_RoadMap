list = [1,2,34,44,55,66,46,48,68,70,72,32,42,12,14,15,15,5,7,19,23,25,27,35,33,38]

b = [i for i  in list if i%2 ==0  ] # print all even numbers from list in list
print("list:",b)


b = [i for i  in list if i%2 !=0  ] ## print all odd numbers from list in list
print("list:",b)


b = [i for i  in list if i>42  ] # all values greater than 42
print("list:",b)


b = [i for i  in list if i<42  ] # all values less than 42
print("list:",b)


b = [i for i  in list if i<42 and i%2==0  ] # all values less than 42, but even
print("list:",b)