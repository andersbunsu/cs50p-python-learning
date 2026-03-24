amountDue = 50

while amountDue > 0:
    print("Amount Due: ", amountDue)
    insertCoin = int(input("Insert Coin: "))
    if insertCoin == 5 or insertCoin == 25 or insertCoin == 10: # will only accept 5,10,25
        amountDue = amountDue - insertCoin
else:
    if amountDue >= 0:
        print("Change Owned:", amountDue)
    else:
        amountDue = amountDue*-1
        print("Change Owned:", amountDue) # print positive number