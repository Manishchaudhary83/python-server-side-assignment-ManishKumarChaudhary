# Develop a simple OOP-based python class Student with attributes like name, roll number, and marks. Implement methods to input and display details.
class student:
    def __init__(self):
        self.name=""
        self.roll_number=""
        self.marks=""
 

    def input_data(self):
        print("\n Students Details")
        self.name=str(input("Enter student name"))
        self.roll_number=int(input("Enter roll number"))
        self.marks=int(input("Enter marks"))
        print("Data stored in file successfully")

    #Display student details
    def display(self):
        print("\n Student details")
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll_number}")
        print(f"Marks:{self.marks}")
a=student()
a.input_data()
a.display()
