tweet = input("Input: ")
print("Output: ", end="")

for c in tweet:
    if c.lower() in "aeiou": # to check each character if vowel, if yes then print nothing.
        print("", sep="", end="")
    else:
        print(c, sep="", end="")