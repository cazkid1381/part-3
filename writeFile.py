
myFile = open(r"C:\Users\Apple\Desktop\part 3\java1.txt", "w")
myFile.write(" i am happy today")
myFile.close()

myFile = open(r"C:\Users\Apple\Desktop\part 3\java1.txt", "r")
print(myFile.read())