file = open('input.txt', 'r')
s = 0

for line in file:
    number = line.split()
     
    for n in number:
        s = s + int(n)
    print(s)