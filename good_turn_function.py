def one_good_turn(n):
    print("I passed here")
    return n + 1


def deserves_another(m):
    return one_good_turn(m + 2)


print(deserves_another(5))
