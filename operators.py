#operators
import operator

a=100
b=20

print('Addition (+)=',operator.add(a,b));
print("substration (-)=",operator.sub(a,b));
print(operator.mul(a,b));
print(operator.pow(a,b));
print(operator.truediv(a,b));
print(operator.floordiv(a,b));
print(operator.mod(a,b));

#comparasion

print(operator.gt(a,b));
print(operator.lt(a,b));
print(operator.ge(a,b));
print(operator.le(a,b));
print(operator.eq(a,b));
print(operator.ne(a,b));


#logical operator

print(a and b);
print(a or b);
print( not b);

#bitwise operator
x=0
y=1
print('(&,and) =',x & y);
print('(|,or) = ',x | y);
print('not,~ =', ~ x); 
print('^ = ',x ^ y);
print('right shift',y >> 10);
print('right shift',y << 3);

# assignment oprtator
m=20
n=10
m+= n
print('',m);

#membership operator

r=5
s=9
l=[10,20,30,40,50]
if(r not in l):
    print('false')
else:
    print('true')

#identity operator
i=1
j=2
k=i
print(i is not j)#true
print(i is k)#true

u = 1+2+3\
    +4+5\
    +6
print(u)

#string
p = 'helloo'
print(p)

#accesing string

st = "hello"
print(st[0])
print(st[3])

#reverce string

stri = "joy"
print(stri[::-1])

#string selling
print(stri[1:3])

#character update
lis1 = list(stri)
lis1[0] = 'o'
str1 = ''.join(lis1)
print(str1)

#delet character

print(stri)
