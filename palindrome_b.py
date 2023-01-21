# palindromos
def run():
    palindromo_wo = lambda string: string == string[::-1]


    try:
        print(palindromo_wo(1))
    except TypeError:
        print("solo se permite strings")

if __name__ == '__main__':
    run()
