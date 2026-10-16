# Python program to collect details for multiple students and 3 course marks

# Ask how many students to process
num_students = int(input("How many students do you want to enter? "))

# Outer loop: Iterates through each student
for student_id in range(1, num_students + 1):
    print(f"\n--- Entering Details for Student {student_id} ---")
    
    # Get basic student details
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    
    total_marks = 0
    max_marks_per_course = 100
    
    # Inner loop: Iterates 3 times to get marks for 3 courses
    for course_id in range(1, 4):
        mark = float(input(f"  Enter marks for Course {course_id} (out of 100): "))
        total_marks += mark
        
    # Calculate performance metrics
    total_max_marks = 3 * max_marks_per_course
    percentage = (total_marks / total_max_marks) * 100
    
    # Display the final report card for the student
    print("\n==============================")
    print(f"    REPORT CARD: {name.upper()} ")
    print("==============================")
    print(f"Roll Number : {roll_no}")
    print(f"Total Marks : {total_marks} / {total_max_marks}")
    print(f"Percentage  : {percentage:.2f}%")
    print("==============================\n")

print("All student data processing complete!")
