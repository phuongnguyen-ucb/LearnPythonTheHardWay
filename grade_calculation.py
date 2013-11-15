# This function calculates the numerical grades and letter grades of each student in the class.

# Below is a dictionary associated with each student in the class.
lloyd = {
    "name": "Lloyd",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
}
alice = {
    "name": "Alice",
    "homework": [100, 92, 98, 100],
    "quizzes": [82, 83, 91],
    "tests": [89, 97]
}
tyler = {
    "name": "Tyler",
    "homework": [0, 87, 75, 22],
    "quizzes": [0, 75, 78],
    "tests": [100, 100]
}

students = [lloyd, alice, tyler] # a list of all students in the class

# Calculate average in general:
def average(x):
	avg = sum(x)/len(x)
	return avg
	
# Calculate weighted average grade of a student:
def get_average(student_name):
		score = average(student_name['homework']) * 0.1 + average(student_name['quizzes']) * 0.3 + average(student_name['tests']) * 0.6
		return score

# Calculate letter grade associated with a student's score:
def get_letter_grade(score):
    score = round(score)
    if score >= 90:
        return "A"
    elif 80 <=score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

# Calculate average grade for the whole class:
def get_class_average(students):
    sum_avg = 0 # initial condition 
    for name in students:
        sum_avg += get_average(name) # total of average grades of all students in class
    class_avg = sum_avg/len(students) # total grades / total number of students = class average grade
    return class_avg

# Display average grade and letter grade for the class:
print "Class average: ", get_class_average(students)
print "Class letter grade: ", get_letter_grade(get_class_average(students))

# Display grade and letter grade for each student in the class:
for name in students:
	print name["name"]
	print get_average(name)
	print get_letter_grade(get_average(name))