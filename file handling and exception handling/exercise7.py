#------------------------------
# Create File and write to file
#------------------------------

# a=open("a1.txt",'w')
# a.write("hey say something")

#---------------------------------------------------------
'''Program to read from one file and write 
to another file'''
#----------------------------------------------------------

# oup_file=open('b1.txt','w+')
# for inp_line in open('a1.txt'):
#     oup_file.write('hpcsa '+inp_line)
#     oup_file.seek(0)
#     print(oup_file.read())
#     oup_file.close()
    
#--------------------------------------------------
'''Program to read from one file and write to the 
same file'''
#---------------------------------------------------

# inp_file=open('a1.txt')
# data=inp_file.readlines()
# inp_file.close()

# oup_file=open('a1.txt','w+')
# for inp_file in data:
#     oup_file.write('dhpcsa '+inp_file)

# oup_file.seek(0)
# print(oup_file.read())

#-------------------------------------------------------------
'''Read a content if file is present if file is not present 
then create blank fileand write "i created file"'''
#-------------------------------------------------------------

# try:
#     file=open('c1.txt','r+')
#     print(file.read())
    
# except FileNotFoundError:
#     print("file not present so create new file ")
#     file=open('c1.txt','w+')
#     file.write("New file")
#     file.seek(0)
#     print(file.read())
#     file.close

################################################################
"""
1) Write a program that creates a dictionary like this 
{
    1: "red" , 2: "Blue" , 3: "Orange"
}
Now take the key as input from the user and print its corresponding colour 
(Exception handle the code to terminate gracefully by printing 
Colour not found if the key doesnot exists )
"""
###################################################################

# try:
#     a={1: "red" , 2: "Blue" , 3: "Orange"}
#     print(a[int(input("please enter the key: "))])
    
# except KeyError:
#     print("key does not exit")

###################################################################
"""
2) Write a program that creates a list of 5 elements of your choice 
Now take the index that the user want the data of and print the value at that 
location 
Exception handle the code to  terminate gracefully by printing 
Value not found if the index doesnot exists 
"""
##############################################################

# try:
#     b=[1,2,3,4,5]
#     print(b[int(input("please enter index no: "))])
# except:
#     print("index does not exit")
    
##########################################################
"""
3) Create program that takes age of the user as input 
and prints number of days that user has lived for 
Exception handle the code such that if the user has lived for more than 
100001 days then user should get the message
, you lived for so long , may be you will die soon:)
"""
#############################################################

# class my_exp(Exception):
#     pass

# try:
#     new=int(input("please enter the age: "))*365
#     if (new>10001):
#         raise my_exp
#     else:
#         print(f"lived for {new} days")

# except my_exp:
#     print(f"lived for {new} days, may will be die soon")
  
'''--------------------------------------------------------------
--------------------------------------------------------------
--------------------------------------------------------------  '''   

class Negative_num_err(Exception):
    pass
class Positive_num_err(Exception):
    pass

def pos_no(my_ls_1):
    pos_no=int(input("enter the number: "))
    if pos_no>0:
        my_ls_1.append(pos_no)
        print(my_ls_1)
    else:
        raise Negative_num_err
    
def neg_no(my_ls_2):
    neg_no=int(input("enter the number: "))
    if neg_no>0:
        my_ls_2.append(neg_no)
        print(my_ls_2)
    else:
        raise Positive_num_err

def my_store():
    my_ls_1=[]
    my_ls_2=[]
    
    while True:
        
        try:
            print("menu")
            print("1: positive number ")
            print("2: negative number ")
            print("3:display all lists ")
            print("4:refresh all lists ")
            print("5:exit ")
            
            choice=int(input("enter the choice: "))
            
            if (choice==1):
                pos_no(my_ls_1)     
            elif(choice==2):
                neg_no(my_ls_2)
            elif(choice==3):
                print("1: {my_ls_1}") 
                print("2: {my_ls_2}")    
            elif(choice==4):
                my_ls_1.clear()
                my_ls_2.clear()
                print("my store")
            elif(choice==5):
                break
        
        except Positive_num_err:
            print(" ")
            my_ls_1.clear()
            
        except Negative_num_err:
            print(" ")
            my_ls_2.clear()
            
my_store()
            