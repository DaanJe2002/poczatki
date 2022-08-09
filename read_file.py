
try:
    with open('cos2.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('plik nie zostal znaleziony')
