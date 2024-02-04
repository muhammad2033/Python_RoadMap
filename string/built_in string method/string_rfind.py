string = "i am a python programmer, i have been working here for a year ,i wanna get much experty in it "

right = "m"

# it is used to find out the letter of the indices

# if it is present , so returns the index number ,otherwise it returns -1

print("string.rfind(right):",string.rfind(right)) #there is m at index 75

print("string.rfind(right):",string.rfind(right,0,80)) #there is m at index 75

print("string.rfind(right):",string.rfind(right,0,2)) #-1(btw 0 and 2 there is no m)

print("string.rfind(right):",string.find(right)) #return 3 coz we have 3 m in the string

print("string.rfind(right):",string.find(right,23,44)) #return -1 coz we have no m in the string from 23 to 44
