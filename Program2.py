# python program Give two list representing students names and  their correspoding exam scores and find the highest 
# and lowest exam score, determine the no of students who passed

# Lists of student names and exam scores
student_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
exam_scores = [85, 76, 90, 58, 88]
d1 = {"Abc":90, "pqr":40, "qwe":550, "xyz":98, "qaz":79}

# Find the highest and lowest exam scores
highest_score = max(exam_scores)
lowest_score = min(exam_scores)

# assuming passing score is 60
passing_score = 60
students_passed = sum(score >= passing_score for score in exam_scores)

# Output the results
print(f"\nStudent List : {student_names}\n")
print(f"Highest Exam Score: {highest_score}")
print(f"Lowest Exam Score: {lowest_score}")
print(f"Number of Students Who Passed: {students_passed}")
