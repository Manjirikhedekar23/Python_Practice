# ----- Inheritance exercise ----
# 1. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 

class Person():
    def __init__(self,in_name,in_place) -> None:
        self.name=in_name
        self.place=in_place
        
    def display_attributes(self):
        print(f"Name: {self.name}\nPlace: {self.place}")
        
class Sister(Person):
    def __init__(self, in_name, in_place,in_examsub) -> None:
        super().__init__(in_name, in_place)
        self.exam_sub=[]
        self.exam_sub.append(in_examsub)
        
    def display_attributes(self):
        super().display_attributes()
        print(f"Exam suject: {self.exam_sub}")
        
    def add_skill(self,new_sub):
        self.exam_sub.append(new_sub)
        
class Uncle(Person):
    def __init__(self, in_name, in_place,in_business) -> None:
        super().__init__(in_name, in_place)
        self.bus=[]
        self.bus.append(in_business)
        
    def display_attributes(self):
        super().display_attributes()
        print(f"Business: {self.bus}")

def main():
    boil1=Person("Manjiri","Dapoli")
    boil1.display_attributes()
    print(" ")
    
    boil2=Uncle("manu","patna","mango")
    boil2.display_attributes()
    print(" ")
    
    boil3=Sister("Sonu","London","bio")
    boil3.add_skill("java")
    boil3.display_attributes()
    
main()   
        