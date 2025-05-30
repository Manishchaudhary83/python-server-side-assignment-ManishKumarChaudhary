# Write python code to read from a CSV file of student marks and calculate average marks.
import csv

filename='student.csv'

rows = []

with open(filename, 'r') as file:
    data = csv.reader(file)
    total_marks=0
    student_count=0

    header = next(data)

    for row in data:
        name = row[0]
        marks = float(row[1])  # integer marks to float
        rows.append((name, marks)) # Store name, marks as tuple 
        total_marks += marks
        student_count += 1


    # Display student data
    print("Student Marks:\n")
    print(f"{header[0]:<10}{header[1]:<10}")
    print('-' * 20)
    for name, marks in rows:
        print(f"{name:<10}{marks:<10}")

 # Calculate and display average
    if student_count > 0:
        average_marks = total_marks / student_count
        print("\nTotal Students:", student_count)
        print(f"Average Marks: {average_marks:.2f}")
    else:
        print("No student data found.")