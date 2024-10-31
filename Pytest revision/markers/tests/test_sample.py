from markers.app.sample import add_two

import  pytest
import sys
# to skip some test using markers
@pytest.mark.skip(reason= "not this time")
def test_add():
    assert add_two(1, 2) == 3
    assert add_two(1, 1) == 2
    assert add_two(1, 3) == 4


@pytest.mark.skipif(sys.version_info > (3, 0), reason= "use python 3.0 or less")
def test_add_str():
    assert add_two('a', 'b')  == 'ab'
    assert add_two('a', 'd')  == 'ad'

@pytest.mark.xfail
def test_add_str():
    assert add_two('a', 'b')  == 'ab'
    raise Exception("expected fail")

@pytest.mark.xfail(sys.platform == 'linux', reason= "linux not supported")
def test_add_str():
    assert add_two('a', 'b')  == 'ab' # all igonred du xfail



