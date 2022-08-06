temp = int(input("jaka jest temperatura na dworze?:"))
if temp >= 0 and temp<= 30:
    print('pogoda jest dzis super')
    print('wyjdz na dwor')
elif not temp < 0 or temp > 30:
    print('pogoda jest dzis okropna')
    print('zostan w domu')
