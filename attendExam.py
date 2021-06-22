totalClass = int(input('Enter the total class :'))
attendClass = int(input('Enter the total Attend class :'))
per = (attendClass / totalClass) * 100

if per >= 75 :
    print('student can attend the exam')
else :
    print('student can not attend the exam')

print('student total attend percentage :', per, '%')