# 2. Create a program that takes a list of student names and stores them in a file. Then, read the file and display the contents.
student=[]
with open ("student.txt","w")as file:
    n=int(input("\nEnter number of students:"))
    file.write("Students Name\n")
    for i in range(n):
        name=str(input(f"Enter student name {i+1} : "))
        file.write(name+"\n")
print("Data stored in file successfully")

with open("student.txt","r") as file:
    content=file.read()
    print(content)
    