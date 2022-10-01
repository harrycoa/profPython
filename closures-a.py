def make_multiplayer(x):
    def multiplier(n):
        return x * n
    return multiplier

times10 = make_multiplayer(10)
times4 = make_multiplayer(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))
