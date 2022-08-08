stolice = {'USA':'Washington',
           'India':'New Delhi',
           'China':'Beijing',
           'Russia':'Moscow'}
#print(stolice['Russia'])
#print(stolice.get('Germany'))
#print(stolice.keys())

for key,value in stolice.items():
   print(key, value)

stolice.update({'Polska':'Warszawa'})