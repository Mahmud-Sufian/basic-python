x = int(input('enter a year '))

if x % 100 == 0 :
   x = x / 100
if x % 4 == 0 :
    print('leap Year')
else :
    print('no leap Year')