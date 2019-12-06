def userInput():
    name = input("Please enter your name. ")
    return name

def loop():
    a = 3
    while a:
        guest_book.append(userInput())
        a -= 1
    return

guest_book = []
loop()
print(guest_book)