from parameterize.app.sample import add_two

import pytest
def test_add():
    assert add_two(1, 2) == 3
    assert add_two(1, 1) == 2
    assert add_two(1, 3) == 4

def test_add_str():
    assert add_two('a', 'b')  == 'ab'
    assert add_two('a', 'd')  == 'ad'

class TestSample:
    def test_add_negative(self):
        assert add_two(-1, -2) == -3
        assert add_two(-1, 2) == 1


@pytest.mark.parametrize("a,b,c", [(1,2,3) ,('a', 'b', 'ab'),
                                   ([1,2], [3], [1,2,3])],
                         ids=["int_sum", "str_concat", "list_concat"]   )
def test_add(a,b,c):
    assert add_two(a, b) == c
