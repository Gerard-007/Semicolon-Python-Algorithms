students_that_passed = 0
students_that_failed = 0


def calculate_students_scores(score):
    if score >= 45:
        print("Student passed the test")
        students_that_passed += 1
    else:
        print("Student failed the test")
        students_that_failed += 1


student_counter = 1

while student_counter <= 15:
    enter_scores = int(input("Enter the score of student {counter}: "))
    calculate_students_scores(enter_scores)
    student_counter += 1
print(f"""
    The number of students that passed the test {students_that_passed}
    The number of students that failed the test {students_that_failed}
""")

