import random

lista = ['kamien','papier','nozyce']
gracz1 = random.choice(lista)
gracz2 = random.choice(lista)
print('Gracz numer 1 wybral: '+ gracz1)
print('Gracz numer 2 wybral: '+gracz2)
while True:
    if gracz1 == 'nozyce' and gracz2 == 'papier':
        print('Wygral gracz numer 1')
        break
    elif gracz1 == 'kamien' and gracz2 == 'nozyce':
        print('wygral gracz numer 1 ')
        break
    elif gracz1 == 'papier' and gracz2 == 'kamien':
        print('wygral gracz numer 1')
        break
    else:
        print('Wygral gracz numer 2')
        break

#karty = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']
#g = random.shuffle(karty)
#print(karty)