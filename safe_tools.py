def safe_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "cannot divide by zero"


def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "not a number"


def get_field(learner , key):
    try:
        return learner[key]
    except KeyError:
        return "field not found"



print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))


learner = {"name": "habii", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))


#the terminal run result
5.0
cannot divide by zero
42
not a number
82
field not found
