question = "What is the Answer to the Great Question of Life, the Universe, and Everything? "
answer = input(question).lower().replace(" ","") # user lower & replace for case- and space-insensitively

if answer == "42"  or answer == "fortytwo" or answer == "forty-two":
    print("Yes")
else:
    print("No")