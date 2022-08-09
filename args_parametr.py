
def add(*wartosci):
    sum = 0
    wartosci = list(wartosci)
    wartosci[4] = 0
    for i in wartosci:
        sum += i
    return sum

print(add(1,2,3,4,56))