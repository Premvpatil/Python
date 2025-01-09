# read data from csv/xsl file containing student information eg : name, age, grade, 
# store in list datatype and perform single data provessing task

import csv

# Function to read student data from a CSV file and store it in a list
def read_student_data(file_path):
    students = []
    
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_info = {
                'Name': row['Name'],
                'Age': int(row['Age']),
                'Grade': row['Grade']
            }
            students.append(student_info)
    
    return students

# Function to perform a simple data processing task
def count_students_by_grade(students):
    grade_count = {}
    
    for student in students:
        grade = student['Grade']
        if grade in grade_count:
            grade_count[grade] += 1
        else:
            grade_count[grade] = 1
    
    return grade_count

# File path
file_path = 'students.csv'  # Change this to your CSV file path

# Read student data
students = read_student_data(file_path)

# Perform data processing: count students by grade
grade_distribution = count_students_by_grade(students)

# Output results
print("\nStudents List:", students)
print("\n")
print("Grade Distribution:", grade_distribution)
