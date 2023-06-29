# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details

class Flight():
    def __init__(self,in_name,in_arrival,in_dep,in_time,in_flightno,in_seatno) -> None:
        self.name=in_name
        self.arr=in_arrival
        self.dep=in_dep
        self.time=in_time
        self.flightno=in_flightno
        self.seatno=in_seatno
        
    def display_instances(self):
        print(f"Name of passenger: {self.name}")
        print(f"Flight arrival: {self.arr}")
        print(f"Flight departure: {self.dep}")
        print(f"Flight time: {self.time}")
        print(f"Flight number: {self.flightno}")
        print(f"Seat number: {self.seatno}")
        
def main():
    
    passenger1=Flight("manjiri","sri lanka","pune","5.00","465415413","50E-W")
    passenger1.display_instances()
    print(' ')
    passenger2=Flight("sonu","pune","london","13.45","5864184617","20E-W")
    passenger2.display_instances()
    
main()
    