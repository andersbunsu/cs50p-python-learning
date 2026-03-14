def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$","") # replace $ with empty space in order to convert to float
    d = float(d) # convert to float
    return d # return the value of d


def percent_to_float(p):
    p = p.replace("%","") # replace % with empty space in order to convert to float
    p = float(p) # convert to float
    p = p/100 # turn percentage into number
    return p

main()