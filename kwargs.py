
def siema(**kwargs):
    #print('siema '+ kwargs['first'] + ' ' + kwargs['last'])
    print('siema',end=' ')
    for key,value in kwargs.items():
        print(value,end=' ')
siema(title='technik',first='Dawid',middle='Adrian',last='Jessa')