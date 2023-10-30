 
print("List function")


l1=[1,2,"Hellow",3.4]
print(type(l1))
print(l1)
print(l1[0 : ])
print(l1[ : ])       
print(l1[2 : 4])
print(l1[1 : 4 : 2])
print(l1[-1 ])
print(l1[-3 : -1])

l1 [2] = 10
print(l1)
l1[3:4] = [89,36]
print(l1)


#repetation

l2 = l1*2
print(l2)

# concatinate
l3 = l1+l2
print(l3)
print(len(l3))

#iteration
"""
for(l1 in l3)
print(l3)
"""

# membership
print(1 in l1)

# adding element in list
'''
l4 = []
n = int(input("Enter no of element"))
for i in range(0,n):
    l4.append(input("Enter element"))
    for i in l4:
        print(i,end = '')
    l4.remove(i)
  print(l4)
    print(len(l4))
    print(min(l4))
    print(max(l4))
  '''
# tuple
l5 = (1,2,3,4,5)
print(l5)
print(l5[0])
l5 = l5*3
print(l5)

c = l5.count(2)
print(c)
i=l5.index(4)
print(i)
del l5

#Dictonary
s={'a','b','c'}
s.add('d')
print(s)

s.discard('a')
print(s)

s.remove('c')
print(s)

s.pop()
print(s)

s.clear()
print(s)

#set function
s1= {1,2,3}
s2= {2,3,4}

print(s1.intersection(s2))

print(s1.union(s2))

print(s1.symmetric_difference(s2))

s1.update(s2)
print(s1)

# Dictonary function

d1 = {1:"hello",2:"hi",3:"welcom"}
print(d1.keys())

print(d1.values())

print(d1.items())

print(d1.get('a'))

newd = d1.copy()
print(newd)

print(d1.popitem())
print(d1)

d2 = {4:"welcom"}
d1.update(d2)
print(d1)


d1.update({5:"nemaste"})

d1.clear5()

d4 = dict.fromkeys(d1,1)
print(d4)
