read_from_file = open("/Users/dale_nelson/Documents/Python/Lab07/\
learning_python.txt","r")
#print(read_from_file.read())

for line in read_from_file:
    print(line.strip())

lines = open("/Users/dale_nelson/Documents/Python/Lab07/\
learning_python.txt","r")
listOfLines = lines.readlines()
for i in listOfLines:
    print(i.strip())