#single condition 
x = input('enter a number :' )
if float(x) > 5:
    print('yes')
else:
    print('no')



#multiple condition
a = input('enter your result :')
a = int(a)

if a >= 80 :
    print('A+') 
elif a >= 70 :
    print('A')
elif a >= 60 :
    print('A-')
elif a >= 50 :
    print('B')
elif a >= 40 :
    print('C')
else:
    print('F')
