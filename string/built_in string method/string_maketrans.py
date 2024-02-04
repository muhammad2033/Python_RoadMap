intab = "abcdefghina"
outtab = "12345678910"

string = " i am a python programmer, i have been working here for a year , i wanna get much experty in it "

tab = string.maketrans(intab,outtab)

print("string.maketrans(intab,outtab):",string.translate(tab))

# it is used for secracy 

# we must use the translate()

# they must have the equal length 