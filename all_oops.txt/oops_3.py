
'''-------------------------------------------
Exercise 01 : Classes and objects -- try creating this in oops world
-------------------------------------------
Employee
  # instance variables 
   emp_id
   emp_salary
   mgr_id
  # class variable 
  department_name
  
  # instance methods
  get_emp_salary()-> emp_salary
  set_emp_salary(rcv_salary)-> emp_salary
  display() --> displays all the values of the attributes of the class

  # class method 
  get_department_name() --> department_name
  
  # static method
  field_expertise() --> just displays some expertise for all my employees
  
main:
main

1) create an object employee(100,1000,1) 
2) display the employee object'''

class Employee():
    department_name="Electrical"
    
    @classmethod
    def new_department_name(cls,in_dep):
        cls.department_name=in_dep
        
    def __init__(self,in_id,in_sal,in_mgr_id) -> None:
        self.empid=in_id
        self.emp_sal=in_sal
        self.manager_id=in_mgr_id
        
    def display_instances(self):
        print(f"employee id: {self.empid}\nemployee's salary: {self.emp_sal}\nmanager id: {self.manager_id}")
        
    def set_emp_salary(self,newsal):
        self.emp_sal=newsal
        
    def get_emp_salary(self):
        print(f"Promoted salary: {self.emp_sal}")
        
    @staticmethod
    def field_expertise():
        print("employees are expert in the Python programming")
        
def main():
    
    emp1=Employee("33","4000","1")
    emp1.display_instances()
    emp1.set_emp_salary("2000")
    emp1.get_emp_salary()
    emp1.field_expertise()
    
main()
        