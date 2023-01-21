## r read, w  escritura con sobrescritura , a apilando
def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["A", "B", "C", "D", "E", "F", "á", "O"]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    print(names)


def run():
    read()
    write()


if __name__ == '__main__':
    run()
