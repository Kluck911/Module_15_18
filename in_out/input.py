myFile = open('filename.txt', 'rt', encoding="utf8")

myFile = open('filename.txt')
print(myFile.read())


myFile = open('filename.txt')
print(myFile.readlines())

myFile = open('filename.txt')
for line in myFile:
    print(line)



with open("filename.txt") as myFile:
    for line in myFile:
        print(line)

'-----------------------------------------'


myFile = open('namefile.txt', 'w')
myFile.write('tttt')
print('zzzz', file=myFile)