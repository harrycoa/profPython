def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("string must not be empty")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrome("ana"))
except TypeError:
    print("solo se puede ingresar strings")
