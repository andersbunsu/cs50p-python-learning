def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # length check
    if not (2 <= len(s) <=6):
        return False
    
    # first two must be letters
    if not(s[0].isalpha() and s[1].isalpha()):
        return False
    
    # must be alphanumeric 
    if not s.isalnum():
        return False
    
    # assign number checked to false 
    numberChecked = False

    for c in s:
        # check if the char is digit
        if c.isdigit():
            if not numberChecked:
                if c == "0":
                    return False
                numberChecked = True
        else:
            if numberChecked:
                return False

    return True
    
main()