#name = "daawid jessa"
#first_name = name[:6]
#last_name = name[7:]
#fajne_imie = name[0:15:2]
#print(first_name)
#print(last_name)
#print(fajne_imie)

imie = input("podaj imie:")
drugie_imie = input('podaj drugie imie:')
nazwisko = input('podaj swoje naziwsko:')
jeden = imie[0:2]
dwa = drugie_imie[-2:]
trzy = nazwisko[0:2]

print('twoj nickname to:'+jeden + dwa + trzy)

slice = slice(0,-3)
website="pornhub.pl"
website2 = 'wikipedia.pl'
print(website2[slice])
print(website[slice])