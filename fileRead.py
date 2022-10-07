from encodings import utf_8


reaFile = r"C:\Users\Apple\Downloads\archive\Fake.csv"
with open(reaFile, "r", encoding= "utf_8" ) as f:
    myObj = f.readlines()
    print(myObj)