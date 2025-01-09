# python file handling progaram to read and write data to txt file

# Function to read data from a file and store it in a list and a dictionary
def read_student_data(file_path):
    students = []
    scores_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            students.append(name)
            scores_dict[name] = int(score)
    
    return students, scores_dict

# Function to calculate the average score
def calculate_average(scores_dict):
    total_score = sum(scores_dict.values())
    num_students = len(scores_dict)
    average_score = total_score / num_students if num_students > 0 else 0
    return average_score

# Main execution
file_path = 'students.txt'  # Change this to your file path
students, scores_dict = read_student_data(file_path)

# Calculate average score
average_score = calculate_average(scores_dict)

# Output results
print("Students:", students)
print("Scores Dictionary:", scores_dict)
print(f"Average Exam Score: {average_score:.2f}")
