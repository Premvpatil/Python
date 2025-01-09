# Python Program Read data text file containing students name and their scores, read data from file 
# and store it into the list and dict, and calculate average exam score

# Function to write student data to a file
def write_student_data(file_path, student_data):
    with open(file_path, 'w') as file:
        for name, score in student_data.items():
            file.write(f"{name},{score}\n")

# Function to read student data from a file
def read_student_data(file_path):
    students = []
    scores_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            students.append(name)
            scores_dict[name] = int(score)
    
    return students, scores_dict

# Example student data
student_data = {
    "Alice": 85,
    "Bob": 76,
    "Charlie": 90,
    "Diana": 58,
    "Ethan": 88
}

# File path
file_path = 'students.txt'

# Write student data to file
write_student_data(file_path, student_data)
print(f"Data written to {file_path}")

# Read student data from file
students, scores_dict = read_student_data(file_path)

# Output results
print("Students:", students)
print("Scores Dictionary:", scores_dict)
print("\n\n")
