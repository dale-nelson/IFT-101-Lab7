def textReading():
    read_file = open("C:\\Users\\piano\\OneDrive\\Documents\\Python\\Lab07\\learning_python.txt")
    return read_file

def forLoopReading():
    for line in textReading():
        print(line.strip())
    return

def listReading():
    read_list = textReading().readlines()
    return read_list

def printEverything():
    print(textReading().read())
    forLoopReading()
    test_list = listReading()
    print(test_list[:2])
    return

printEverything()