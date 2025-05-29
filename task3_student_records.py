#Implement a program to store student records (name, roll, marks contact number) using a dictionary
    #a. provide menu options to add,search, and display students.
students={}

def add_student():
    n=int(input("Enter no of students"))
    for i in range(n):
        name=str(input(f"Enter name{i+1}:"))
        roll=int(input("Enter roll no."))
        marks=int(input("Enter marks"))
        contact=str(input("Enter contact number"))

        students[roll]={
            "name":name,
            "marks":marks,
            "contact":contact
        }

def search_student():
    roll=int(input("Enter roll number"))
    if roll in students:
        print(f"student found {roll}")
        student=students[roll]
        print("\n Student found:")
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Contact: {student['contact']}") 
    else:
        print("Student not found")

def display_students():
    if not students:
        print("\n")
        print("No student data available.\n")
    else:
        print("\nAll Students:")
        for roll, info in students.items():
            print(f"Roll Number: {roll}")
            print(f"Name : {info['name']}")
            print(f"Marks : {info['marks']}")
            print(f"Contact: {info['contact']}")
        print("\n")
while True:
    print("\n Students Records Menu")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    choice=input("Enter your choice (1-4)")

    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        display_students()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select (1-4)")
        

