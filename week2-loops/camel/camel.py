camelCase = input("camelCase: ")
print("snake_case: ", end="")
for c in camelCase: # iterate the str 
    if c.islower(): # checking if the char is lower, if lowercase then print
        print(c,end="")
    else: # else print "_" andconvert the case to lowercase
        print("_",c.lower(),sep="",end="")