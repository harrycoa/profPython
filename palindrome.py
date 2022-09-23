# palindromos
def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


def run():
    print(is_palindrome("anitalavalatina"))


num = round(10.3456, 2)
print(num)

print(10 / 2 + 5 * 7)

if __name__ == '__main__':
    run()
