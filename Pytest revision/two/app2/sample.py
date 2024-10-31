# assert exceptions
def validate_age(age):
    if age < 0 :
        raise ValueError("Age cannot be negative")