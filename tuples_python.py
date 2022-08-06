
student = ('dawid',21,'chlop')
print(student.count("dawid"))
print(student.index('chlop'))

for x in student:
    print(x)

if 'dawid' in student:
    print('dawid jest studentem')