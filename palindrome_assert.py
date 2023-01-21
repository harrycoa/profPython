def palindrome(string):
    try:
        assert len(string) > 0, "No puedes ingresar una cadena vacia"
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrome(""))
except TypeError:
    print("solo se puede ingresar strings")
