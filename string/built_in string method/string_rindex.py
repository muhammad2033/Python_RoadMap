string = "i am a python programmer, i have been working here for a year ,i wanna get much experty in it "

right = "m"



# it is used to find out the letter of the indices

# if it is present , so returns the index number ,otherwise it returns exceptional error

print("string.rfind(right):",string.rindex(right)) #there is m at index 75

print("string.rfind(right):",string.rindex(right,33,44)) #there is no m between 33 and 44 , so it returns exceptional error
