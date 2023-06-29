
from definations import *

# a = lambda num1,num2 : addition(num1,num2)
# b = lambda num1,num2=None : sqr(num1,num2)
# c = lambda num1,num2 : exp(num1,num2)

op = {1:a,2:b,3:c,4:"bye"}
while True:
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    print("4 : Exit")
    ch = int(input ("Please select your choice: "))
    if ch != 4 :
        num1 = int(input("Please enter First number: "))
        if ch != 2 :
            num2 = int(input("Please enter Second number: "))
        print("Addition :" if ch==1 else  "Square" if ch==2 else "exponention" if ch==3 else exit(),end=" ")
    
        print(op.get(ch)(num1,num2))
        ch = input("\n Do you want to continue (Y/N)").lower()     
        if ch == 'n':
            break
    else:
        break 