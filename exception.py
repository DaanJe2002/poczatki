try:
    numer = int(input('Podaj numer jaki bedziemt dzielic: '))
    dzielnik = int(input('Podaj numer przez jaki bedziemy dzielic: '))
    wynik = numer / dzielnik
    print(wynik)
except ZeroDivisionError:
    print('nie mozesz dzielic przez zero idioto ')
except ValueError:
    print('Nieprawidlowa wartosc, Podaj numer !!!!!')
#except Exception:
    #print('cos poszlo nie tak :c')
finally:
    print('cos tam na koniec zawsze czy zle czy dobre ')