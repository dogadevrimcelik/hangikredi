from grade_operations import grade_summary
'''
In the main function, create a dictionary called student_grades where the keys are the names of the
students (strings) and the values are lists of their grades (integers or floats). The dictionary should
contain at least 3 students, and each student should have at least 5 grades.
'''
student_grades = {
    "Esra": [80, 75, 90, 85, 92],
    "Suna": [70, 65, 80, 75, 78],
    "Levent": [90, 92, 88, 85, 95],
    "Bora" : [0, 100, 45, 60 ,80],
    "Sinem" : [90, 80, 75, 100, 95]
}

'''
Write a function called student_summary that takes the student_grades dictionary as input and prints
the following information for each student:
• Student name
• Average grade
• Highest grade
• Lowest grade
• Grade spread
Call the student_summary function with the student_grades dictionary as an argument to display the
summary information for each student.
Note: You can assume that the input will always be a valid dictionary of student grades.
'''
def student_summary(student_grades):
    for i in student_grades:
        print(f'Student Name: {i}')
        grade_summary(student_grades[i])

student_summary(student_grades)
