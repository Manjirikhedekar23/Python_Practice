def dict_display(cap):
    a=cap.keys()
    print("no of element: ",len(a))
    
def dict_add(cap):
    b=input("enter key: ")
    a=input("enter element to add: ")
    cap[b]=a
    print(cap)
    
def dict_add_elements(cap):
    a=input("enter the values: ").split(",")
    list(a)
    for i in (len(a)):
        cap.update({i:a[i]})
        print(cap)
        
def dict_rem(cap):
    cap.pop(input("delete two values: "))
    print(cap)
    
def my_store():
    
    cap={}
    
    for dict_ele in input("for ex: india:pune"):
        temp_list=dict_ele.split(":")
        cap[temp_list[0].replace('"','').strip()]=temp_list[1].replace('"','').strip()
        
    while True():
            
        ch=int(input("enter choice: ")).split(",")
            
        if ch==1:
            dict_display(cap)
        elif ch==2:
            dict_add(cap)
        elif ch==3:
            dict_add_elements(cap)
        elif ch==4:
            dict_rem(cap)
        elif ch==5:
            break
        else:
            print("invalid")
                
my_store()