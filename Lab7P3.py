def openFile():
    opened_file = open("C:\\Users\\piano\\Downloads\\HP5.txt","r")
    return opened_file

def wc():
    read_file = openFile().read()
    total_words = read_file.split()
    return len(total_words)

def lc():
    list_of_lines = openFile().readlines()
    return len(list_of_lines)

def charCount():
    num_chars = 0
    for line in openFile():
        num_chars += len(line)
    return num_chars

print(lc())
print(wc())
print(charCount())

