#Write a function called average_grade that takes a list of student grades (integers or floats) as input and
#returns the average grade. Round the result to two decimal places.

def average_grade(grade_list):
    grade_sum = sum(grade_list)
    average = grade_sum / len(grade_list)
    return round(average, 2)

#Write a function called highest_grade that takes a list of grades as input and returns the highest grade

def highest_grade(grade_list):
    highest = max(grade_list)
    return highest

#Write a function called lowest_grade that takes a list of grades as input and returns the lowest grade.

def lowest_grade(grade_list):
    lowest = min(grade_list)
    return lowest

#Write a function called grade_spread that takes a list of grades as input and returns the difference
#between the highest and lowest grades.

def grade_spread(grade_list):
    return highest_grade(grade_list) - lowest_grade(grade_list)

'''
Write a function called grade_summary that takes a list of grades as input and prints the following
summary information:
• Average grade
• Highest grade
• Lowest grade
• Grade spread
'''
def grade_summary(grade_list):
    return print(f'Average Grade: {average_grade(grade_list)} \n'
                 f'Highest Grade: {highest_grade(grade_list)} \n'
                 f'Lowest Grade: {lowest_grade(grade_list)} \n'
                 f'Grade Spread: {grade_spread(grade_list)}')

