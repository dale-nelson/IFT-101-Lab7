def newFile():
    guest_book = open("guest_book.txt","w")
    return guest_book

def userInput():
    name = input("Please enter your name. ")
    return name

def greeting(a):
    greet = "Hi {0}, thanks for coming!".format(a.title())
    return greet

def loop():
    tmp_var = ""
    guests = newFile()
    while tmp_var != 'quit':
        tmp_var = userInput()
        if tmp_var != 'quit':
            guests.write(tmp_var + "\n")
            print(greeting(tmp_var))
    return guests

print("This program enters names like a guest book and stores them in a file.")
loop()