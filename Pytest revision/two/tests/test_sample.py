from two.app2.sample import validate_age
import pytest

def test_validate_age_valid_age():
    validate_age(10)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
    #print(str(exc_info.value))
    assert str(exc_info.value) == "Age cannot be negative"


def test_validate_age_invalid():
    with pytest.raises(ValueError, match="Age cannot be negative"):
        validate_age(-1)

