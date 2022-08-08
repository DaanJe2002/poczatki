number1 = int(input('Podaj nr 1:'))
number2 = int(input('podaj nr 2:'))

def multiply(number1,number2):
    result = number1 * number2
    return result

wynik = multiply(number1,number2)
print('wynik to: '+str(wynik))