# ----- Inheritance exercise ----
# 1. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 


class Person:
    def __init__(self,name,residence) -> None:
        self.name=name
        self.residence=residence
    
    def display_attr(self):
        print("Person Name : ",self.name)
        print("Residence : ",self.residence)
        

class Sister(Person):
    def __init__(self,name,residence,subs) -> None:
        super().__init__(name,residence)
        self.exam_subs=[]
        self.exam_subs.append(subs)
        
    def display_attr(self):
        super().display_attr()
        print("Exam Subjects : " ,self.exam_subs)
    
class Uncle(Person):
    def __init__(self,name,residence,business) -> None:
        super().__init__(name,residence)
        self.business = business
        
    def display_attr(self):
        super().display_attr()
        print("Business : ",self.business)
        #Sister.display_attr()


def main():
    
    u=Uncle("Vikas","Delhi","XYZ")
    s=Sister("payal","Pune",["python","Java"])
    u.display_attr()
    s.display_attr()

main()


# -------------------------------------------
# Exercise 01 : Classes and objects -- try creating this in oops world
# -------------------------------------------
# Employee
#   # instance variables 
#    emp_id
#    emp_salary
#    mgr_id
#   # class variable 
#   department_name
  
#   # instance methods
#   get_emp_salary()-> emp_salary
#   set_emp_salary(rcv_salary)-> emp_salary
#   display() --> displays all the values of the attributes of the class

#   # class method 
#   get_department_name() --> department_name
  
#   # static method
#   field_expertise() --> just displays some expertise for all my employees
  
# main:
# main

# 1) create an object employee(100,1000,1) 
# 2) display the employee object


class Employee:
    
    dept_name = "ABC"
    
    @classmethod
    def get_department_name(cls):
        return cls.dept_name
        
    def __init__(self,id,mg_id):
        self.emp_id=id
        self.mgr_id=mg_id
        
    def set_emp_sal(self,sal):
        self.emp_sal = sal
    
    def get_emp_sal(self):
       return self.emp_sal
     
    @staticmethod
    def field_expertise():
        print("employees are expert in the Python programming")
    

def main():
    id, mg_id =input("Employee id : "),input("Manager id: ")
    o1=Employee(id,mg_id)
    sal=input("Employee salary : ")
    o1.set_emp_sal(sal)
    #dept_name=input("Department :")
    
    print("EMP ID :" ,o1.emp_id)
    print("EMP SALARY : ",o1.get_emp_sal())
    
    print("MANAGER ID :",o1.mgr_id)
    print("DEPARTMENT :", Employee.get_department_name())
    
    print("EXPERTIES :",end="")
    o1.field_expertise()
    
main()