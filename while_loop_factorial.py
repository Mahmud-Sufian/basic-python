num = int(input('enter a factorial number : '))
i = 1
fact = 1
while i < num :
    fact = fact * i
    i = i + 1
    print(i, fact)