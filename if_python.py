wiek = int(input('ile masz lat:'))
if  wiek == 100:
    print("jestes naprawde stary")
elif wiek < 0:
    print('jeszcze sie nie urodziles ')
elif wiek <=17:
    print('jestes niepelnoletni')
else:
    print('jestes pelnoletni')