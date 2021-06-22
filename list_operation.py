list = ['jamal', 'kamal', 'rahim', 'kamal']
list1 = ['ami', 'amra', 'tmi', 'tmra']
num = [12, 45, 71, 3, 7, 20, 50, 22, 11, 19, 12]

#list access
a = list[1]
# print(a)

#append by last element
b = list.append('sufian')
#print(list)

#linsert any place
c = list.insert(1, 'onion')
#print(list)

#list reverse
d = list.reverse()
#print(list)

#list count
e = list.count('kamal')
# print(e)

#list remove
f = list.remove('kamal')
# print(list)

#pop last element
g = list.pop()
# print(list)

#del list
del list[0]
# print(list)

#join list
h = list + list1
# print(h)

#check index
#i = list.index('kamal') # we know index value
#i = 'manush' in list #bool return.
if 'kamal' in list :
    i = list.index('kamal')
# print(i)

#sort
j = num.sort()
# print(num)

#sort + reverse
k = num.sort(reverse=True)
# print(num)

#slice
l = num[1:5:2] #starting index : end index : which gap
# print(l)