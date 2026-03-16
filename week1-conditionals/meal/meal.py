def main():
    x = input("What time is it? ")
    convert(x)

def convert(time):
    # split it into 2 seperate by ":"
    # it will return 
    time = time.split(":") 
    
    # assign the first value of time as hour and convert into int for addition
    hour = int(time[0])

    # split the last value in the list by " "
    # this will split the minutes and the 12 hours system

    hoursFormat = time[1].split(" ")

    if len(hoursFormat) == 2: # to check if there's pm/am in the input
        if hour!=12 and hoursFormat[1] == "p.m":
            hour = hour + 12  # if it is pm then add another 12 hours

    if hour > 24:
        print("Invalid time")
    if hour >= 7 and hour <=8:
        print("breakfast time")
    elif hour >= 12 and hour <= 13:
        print("lunch time")
    elif hour >= 18 and hour <= 19:
        print("dinner time")

main()