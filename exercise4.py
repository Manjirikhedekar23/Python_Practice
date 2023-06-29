def list_display_members(members):
    for i in range (len(members)):
        print(members)

def list_add_elements(members):
    add = input("enter the variable:")
    members.append(add)
    print(members)
    
def list_remove_elements(members):
    i=int(input("enter the index to remove"))
    members.pop(i)
    print(members)
    
def remove_last_elements(members):
    members.pop(len(members)-1)
    print(members)
    
def display_elements(members):
    print(members[2:5])
    
def my_list_store():
        print("/n welcome to our list store!!!")
        print("please enter comma seperated operation")
        
members=input("for ex: paul,kevin,john,sonu \n").split(",")
    
while(True):
    print("/n***************Menu******************")
    print("operation supported by our programs are")
    print("1.Display number of element in list")
    print("2.Add element to list like 'manu'")
    print("3.Add element to list like['David','david']")
    print("4.Remove last element of list")
    print("5.Remove last element of list")
    print("6.Display third,fourth and fifth element from list")
    print("7.Exit the program")
    
    choice = int(input("please enter the choice: "))

    if choice == 1:
        list_display_members(members)
    elif choice == 2:
        list_add_elements(members)
    elif choice == 3:
        list_add_elements(members)
    elif choice == 4:
        remove_last_elements(members)
    elif choice == 5:
        remove_last_elements(members)
    elif choice == 6:
        display_elements(members)
    elif choice == 7:
        break
    else:
        print("invalid")

my_list_store()

    