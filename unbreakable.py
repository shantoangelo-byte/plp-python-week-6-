def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


print(safe_number("25"))
print(safe_number("abc"))


#the terminal run result
25
Not a number
