def set_u(A,B):
    set_display(A)
    set_display(B)
    print("union",A.union(B))

def set_int(A,B):
    set_display(A)
    set_display(B)
    print("intersection",A.intersection(B))
 
def set_minus(A,B):
    set_display(A)
    set_display(B)
    print("difference",A.difference(B))
    
def is_memofset(rcv_set):
    element=input("Please enter element") 
    print(f"element {element} is present (true/false): {element in rcv_set}") 
    set_display(rcv_set) 
       
def set_display(rcv_s):
    print(rcv_s)
    
def set_add(rcv_set):
    rcv_set.add(input("please enter element to add: "))
    set_display(rcv_set)
    
def set_add_elements(rcv_set):
    rcv_set.update(input("please enter elements to add: ").split(","))
    set_display(rcv_set)
    
def set_rem(rcv_set):
    rcv_set.discard(input("please enter element to remove: "))
    set_display(rcv_set)
    
def my_store():
    print("____Welcome___")
    
    A=set()
    B=set()
    
    for set_ele in input("please enter element").split(","):
        A.add(set_ele.strip())
    
    for set_ele in input("please enter element").split(","):
        B.add(set_ele.strip())

    while (True):
        
        choice=int(input("please enter the choice: "))
        
        if choice ==1:
            set_u(A,B)
        
        elif choice ==2:
            set_int(A,B)
            
        elif choice ==3:
            set_minus(A,B)
            
        elif choice ==4:
            set_minus(B,A)
            
        elif choice ==5:
            is_memofset(B)
            
        elif choice ==6:
            set_display(A)
        
        elif choice ==7:
            set_display(B)
        
        elif choice ==8:
            set_add(A)
            
        elif choice ==9:
            set_add_elements(A) 
            
        elif choice ==10:
            set_rem(A)
            
        elif choice ==11:
            break
        
        else:
            print("invalid")
            
my_store()
        