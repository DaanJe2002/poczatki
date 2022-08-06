rows = int(input('ile chcesz row?:'))
columns = int(input('ile chcesz kolumn?:'))
symbol = input('jaki chcesz symbol?:')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()