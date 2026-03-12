# defining hello function
# apply methods strip() and title() to the string "to" 
def hello(to):
    print("Hello,", to.strip().title())


def main():
    # Ask for user name
    name = input("What's your name? ")
    hello(name)

main()