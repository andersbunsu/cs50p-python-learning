greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"): #use startwith to case the first few letter
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")