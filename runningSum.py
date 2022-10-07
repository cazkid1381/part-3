running_sum =  0
myVar = int(input("enter your numbers: "))
print(myVar)
while True:
    if(myVar < 0):
        break
    else:
        running_sum = running_sum + 1
        print("you entered a negative sum "  + running_sum)
        
     
