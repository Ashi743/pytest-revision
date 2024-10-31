import pytest
from datetime import datetime
from fixture_factory.myapp.students import Student

def test_student_get_age(dummy_student):
    # Calculating the exact age in years
    current_date = datetime.now()
    dob = dummy_student.dob
    dummy_student_age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
    assert dummy_student.get_age() == dummy_student_age

def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 20

def get_topper(students):
    # Finding the "topper" based on maximum age in this case
    return max(students, key=lambda student: student.get_age(), default=None)

def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("ram", 21),
        make_dummy_student("shyam", 19),
        make_dummy_student("ravi", 22)
    ]

    topper = get_topper(students)
    assert topper == students[2]  # Assuming "topper" is the oldest student
