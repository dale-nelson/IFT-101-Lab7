def textReading():
    #read_file = open("C:\\Users\\piano\\OneDrive\\Documents\\Python\\Lab07\\learning_python.txt")
    read_file = open("/Users/dale_nelson/Documents/Python/Lab07/learning_python.txt","r")
    return read_file

def forLoopReading():
    for line in textReading():
        print(line.strip())
    return

def listReading():
    read_list = textReading().readlines()
    return read_list

def reverseList():
    tmp_var = listReading()
    backwards_list = tmp_var[::-1]
    return backwards_list

def multiplyList():
    return listReading() * 3

def printEverything():
    print(textReading().read())
    forLoopReading()
    print(str(reverseList()) + "\n")
    print(multiplyList())
    return

printEverything()