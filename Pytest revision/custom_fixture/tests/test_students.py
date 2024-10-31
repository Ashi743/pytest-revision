
import  pytest
from datetime import datetime

from custom_fixture.myapp.students import students

@pytest.fixture(scope= "module")
def dummy_student():
    return students("Ashi", datetime(1997, 8,6), 'civil')

def test_student_details(dummy_student):
    dummy_age= (datetime.now() - dummy_student.dob).days// 365
    assert dummy_student.get_age() == dummy_age

def test_dummy_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5

def test_dummy_get_credits(dummy_student):
    assert dummy_student.get_credits() == 0