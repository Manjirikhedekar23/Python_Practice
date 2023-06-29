# a=input("enter a string: ")
# rep_char=[]
# for char in a:
#     if a.count(char)>1:
#         rep_char.append(char)
#         print("repeated char",rep_char)

# valid_num=(1,2,3,4,5,6,7,8,9,10)
# numb=int(input("enter the number in between 1 to 10: "))

# if numb not in valid_num:
#     print("invalid number")
# else:
#     data =(numb)
    
# try:
#     data[1]=5
# except TypeError:
#     print("tuple not allowed")
    
#     try:
#         data.append(5)
#     except AttributeError:
#         print("tuple not allow")

det={}
while True:
    key =input("enter a key: ")
    if key == "":
        break
    value =input("enter a value: ")
    det[key]=value
    
print("details",det)
        

