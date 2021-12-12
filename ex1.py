Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1
1
>>> 1+2
3
>>> 2+3
5
>>> 8+_
13
>>> 8+_
21
>>> 8+_
29
>>> 8+_
37
>>> 8+_
45
>>> 50-2*2
46
>>> (20-2+3)/3
7.0
>>> 3-2
1
>>> 3-4
-1
>>> 2*3
6
>>> 6/4
1.5
>>> 6/2
3.0

>>> 20//2 #floor divition
10

>>> 20%2 #remainder to the divtion
0

>>> 20%3 #remainder to the divtion
2

>>> 3**7 #3 to the power of 7
2187

>>> width=12
>>> height=23
>>> width*height
276

>>>#================================================================




>>> print('gopi raj is laning python at \n')
gopi raj is laning python at 


>>> print('gopi raj is leaning python at \n morning 5 am')
gopi raj is leaning python at 
 morning 5 am

>>> for i in range(5):
	print('hellow world',i,end=" ")

	
hellow world 0 hellow world 1 hellow world 2 hellow world 3 hellow world 4 

>>> for i in range(5):
	print('hellow world',i,end="")

	
hellow world 0hellow world 1hellow world 2hellow world 3hellow world 4

>>> print('gopi');print('raj')
gopi
raj


>>> print('gopi',end='\n');print('raj')
gopi
raj

>>> print('gopi',end='');print('raj')
gopiraj

>>> print('gopi',end=' ');print('raj')
gopi raj

>>> print('gopi',end='--> ');print('raj')
gopi--> raj


>>> l=[1,2,3,4,5]

>>> reversed(l)
<list_reverseiterator object at 0x0000018BC02DEC70>

>>> for i in reversed(l):
	print(i,end=' ')

	
5 4 3 2 1 

>>> l
[1, 2, 3, 4, 5]

>>> print(reversed(l))
<list_reverseiterator object at 0x0000018BC02DEC70>

>>> reversed(range(5))
<range_iterator object at 0x0000018BC234BE10>

>>> for i in reversed(range(5)):
	print(i,end='')

	
43210

>>> import time

>>> for i in reversed(range(4)):
	if i>0:
		print(i,end='>>>')
		time.sleep(1)
	else:
		print('Start')

		
3>>>2>>>1>>>Start

>>> for i in reversed(range(4)):
	if i>0:
		print(i,end='>>>')
		time.sleep(2)
	else:
		print('Start')

		
3>>>2>>>1>>>Start

>>> import os


>>> print('sathish')
sathish

>>> print('kumar')
kumar

>>> l
[1, 2, 3, 4, 5]

>>> print(*l)
1 2 3 4 5

>>> ord('D')
68

>>> ord('\n')
10




>>> print('%d, -->,%f' %(1,23.345))
1, -->,23.345000



>>> print('%d, -->,%5f' %(1,23.345))
1, -->,23.345000

>>> print('%d, -->,%5.2f' %(1,23.345))
1, -->,23.34


>>> print('%d'%12)
12

>>> print('%d'%12.123)
12

>>> print('%f'%12.123)
12.123000

>>> print('%.3f'%12.123)
12.123

>>> print('%1.3f'%12.123)
12.123

>>> print('%1.3f'%0011232.123)
11232.123

>>> print('%2.3f'%11232.123)
11232.123

>>> print('%2.3f'%11232.123)
11232.123

>>> print('%2.3E'%11232.123)
1.123E+04

>>> print('%2.4E'%11232.123)
1.1232E+04

>>> print('%1.4E'%11232.123)
1.1232E+04


>>> print('%o'%112)
160

>>> oct(112)
'0o160'


>>> print('%x'%112)
70

>>> hex(112)
'0x70'



>>> print('{}{}'.format('gopi','raj'))
gopiraj

>>> print('{} {}'.format('gopi','raj'))
gopi raj

>>> print('{1} {0}'.format('gopi','raj'))
raj gopi

>>> print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
I love Geeks for "Geeks!"

>>> print(f"I love Geeks for \"Geeks!\"")
I love Geeks for "Geeks!"

>>> print(f"I love Geeks for \"Geeks!\"")==print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
I love Geeks for "Geeks!"
I love Geeks for "Geeks!"
True



>>> print('{}{}and{other}'.format('gopi','raj',other='sathish kumar'))
gopirajandsathish kumar

>>> print('{} {} and {other}'.format('gopi','raj',other='sathish kumar'))
gopi raj and sathish kumar

>>> d={'name':'gopi','age':'21'}

>>> d2={'name':'sathish','age':'27'}

>>> print('{0[name]} and {0[age]} and {1[name]}'.format(d,d2))
gopi and 21 and sathish

>>> print('{0[name]:s} and {0[age]} and {1[name]}'.format(d,d2))
gopi and 21 and sathish



>>>#=================================================================


Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=2
>>> b=4
>>> add=a+b
>>> sub=a-b
>>> div=a/b
>>> div2=a//b
>>> 
>>> print(add)
6
>>> print(sub)
-2
>>> print(div)
0.5
>>> print(div2)
0
>>> mul=a*b
>>> print(mal)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(mal)
NameError: name 'mal' is not defined
>>> print(mul)
8
>>> 
>>> 
>>> mod=a%b
>>> mod
2
>>> 
>>> 
>>> a=12
>>> b=13
>>> 
>>> a>b
False
>>> a<b
True
>>> a==b
False
>>> a!=b
True
>>> 
>>> a>=b
False
>>> a<=b
True
>>> 
>>> 
>>> a and b
13
>>> a or b
12
>>> a or b
12
>>> 
>>> 
>>> a=True
>>> b=False
>>> 
>>> a and b
False
>>> a or b
True
>>> a not b
SyntaxError: invalid syntax
>>> not b
True
>>> not a
False
>>> 
>>> 
>>> bin(10)
'0b1010'
>>> 0b10
2

>>> 'gopi' and 'Raj'
'Raj'

>>> 'gopi' or 'Raj'
'gopi'


>>> 2&3
2

>>> bin(2)
'0b10'

>>> bin(3)
'0b11'

>>> 3&8
0

>>> 3&9
1

>>> 3&1
1

>>> 3&5
1

>>> 3&54
2

>>> 3&542
2

>>> 1&1
1

>>> 1&2
0

>>> 1&3
1

>>> 1&4
0

>>> 1&7
1

>>> 1&8
0

>>> 1&9
1

>>> 1&11
1

>>> 1&12
0

>>> 1&20
0

>>> 1&21
1

>>> 1&22
0

>>> 1&23
1

>>> 1&24
0

>>> 1&25
1

>>> 1&26
0

>>> 1&40
0

>>> 1&42
0

>>> 1&60
0

>>> 1&61
1

>>> 34&23
2

>>> 34&24
0

>>> 34&25
0

>>> 34&26
2

>>> 34&27
2

>>> 34&28
0

>>> 34&29
0

>>> 34&30
2

>>> 34&300
32


>>> ~3
-4

>>> ~5
-6

>>> ~9
-10

>>> ~12345
-12346

>>> 1^4
5

>>> 1^5
4

>>> 1^6
7

>>> 1^7
6

>>> class Geek():
    def __init__(self, value):
        self.value = value
 
    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")
 
    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Geek):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class Geek")
 
    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, Geek):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class Geek")
 
    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class Geek")
 
    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")
 
    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value

 
>>> a=Geek(10)

>>> b=Geek(12)

>>> a & b

And operator overloaded
8

>>> 10 &12
8

>>> a | b
Or operator overloaded
14

>>> class myclass:
	def print_mag(self):
		print('helllow world')

		
>>> s=myclass()

>>> isinstance(s,myclass)
True

>>> a << b
lshift operator overloaded
40960

>>> 10 << 12
40960

>>> 10 >> 12
0

>>> a >> b
rshift operator overloaded
8

>>> a & b
And operator overloaded
8

>>> class myclass:
	def __init__(self,value):
		self.value=value
	def __str__(self,obj):
		return self.value + obj.value

	

>>> s=myclass('Gopi')

>>> d=myclass('raj')


>>> print('gopi' in 'gopiraj')
True

>>> print('gopi' in 'gopi raj')
True

>>> print('gopi' not in 'gopi raj')
False

>>> print('gopi' is 'gopi raj')
False

>>> print('gopi' is 'gopi')
True

>>> print('gopi' is 'gopi')
True


>>> name='gopi'

>>> print(name is 'gopi')
True

>>> print(name is 'gopiraj')
False

>>> print(name is not 'gopiraj')
True


>>> x=21

>>> l=[1,2,3,4,5]

>>> if (x not in l):
	print('21 not in list of l')
else:
	print('21 in list of l')

	
21 not in list of l

>>> a=10

>>> b=20

>>> print ("Both a and b are equal" if a == b else "a is greater than b"

        if a > b else "b is greater than a")
b is greater than a


>>> if a==b:
	print('Both a and b are equal')
else:
	if a>b:
		print()

		
>>> if a==b:
	print('Both a and b are equal')
else:
	if a>b:
		print('a is greater than b')
	else:
		print('b is greater than a')

		
b is greater than a


>>> 'Both a and b are equal' if a==b  else 'a is greater than b'if a>b else 'b is greater than a'
'b is greater than a'

>>> a=10

>>> b=10

>>> 'Both a and b are equal' if a==b  else 'a is greater than b'if a>b else 'b is greater than a'
'Both a and b are equal'


>>> ('true','false')[12>123]
'true'

>>> ('gopi','raj')[12>123]
'gopi'

>>> ('gopi','raj')[12>1]
'raj'

>>> (False,True)[12>123]
False

>>> (False,True)[126>123]
True

>>> {True:"gopi",False:'raj'}[12>1]
'gopi'

>>> {True:"gopi",False:'raj'}[0>1]
'raj'

>>> a=12

>>> b=23

>>> print(a,'is greater')if(a>b)else print(b,'is greater')
23 is greater

>>> s=a<b and a or b

>>> s
12

>>> a<b
True


>>> True and a
12

>>> True and a or b
12


>>>#==================================================

>>> class fun():
	def __init__(self,n):
		self.n=n
	def __add__(self,other)	:
		print('adding over loding')
		return self.n + other.n

	
>>> a=fun(3)

>>> b=fun(5)

>>> a+b
adding over loding
8

>>> class complex:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def __add__(self,other):
		print('comlex number added')
		return self.a+other.a,self.b+other.b

	
>>> a=complex(1,1)

>>> b=complex(2,2)

>>> a + b
comlex number added
(3, 3)

>>> a=21

>>> b=12

>>> print((lambda :a,lambda :b)[a>b]())
12

>>> print((lambda :a,lambda :b)[a<b]())
21

>>> a=12

>>> b=21

>>> 'a is greater then' if a>b else 'b is greater then' if a!=b else 'a and b are equals'
'b is greater then'

>>> a,b=12,12

>>> 'a is greater then' if a>b else 'b is greater then' if a!=b else 'a and b are equals'
'a and b are equals'

>>> def fun(a,b):
	return 'a is greater then' if a>b else 'b is greater then' if a!=b else 'a and b are equals'

>>> fun(12,2)
'a is greater then'

>>> fun(12,28)
'b is greater then'

>>> fun(12,12)
'a and b are equals'

>>> fun(12,-1)
'a is greater then'

>>> def funtion(a,b):
	if a!=b:
		if a>b:
			print('a is greater then b')
		else:
			print('b is greater then a')
	else:
		print('a and b are equals')

		
>>> funtion(21,21)
a and b are equals

>>> class fun():
	def __init__(self,a):
		self.a=a
	def __gt__(self,b):
		return self.a>b.a

	

>>> a=fun(2)

>>> b=fun(4)

>>> a>b
False

>>> a<b
True

>>> a>b
False

>>> class fun():
	def __init__(self,a):
		self.a=a
	def __gt__(self,b):
		print('printing')
		return self.a>b.a

	
>>> a=fun(2)


>>> b=fun(4)

>>> a>b
printing
False

>>> a<b
printing
True


>>> class fun():
	def __init__(self,a):
		self.a=a
	def __gt__(self,b):
		print('printing')
		return self.a>b.a
	def __eq__(self,b):
		return self.a==b.a

	
>>> a=fun(2)

>>> b=fun(4)

>>> a==b
False


>>> class fun():
	def __init__(self,a):
		self.a=a
	def __gt__(self,b):
		print('printing')
		return self.a>b.a
	def __eq__(self,b):
		print('cheking equal:')
		return self.a==b.a

	
>>> a=fun(2)

>>> b=fun(4)

>>> a==b
cheking equal:
False

>>> a!=b
cheking equal:
True


>>> a<b
printing
True


>>> l=[]

>>> for i in range(1,11):
	l.append(i*4)
	
>>> l
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40]


>>> l[9]
40

>>> any(l)
True

>>> all(l)
True



>>> import operator


>>> a=12

>>> b=21

>>> operator.add(a,b)
33

>>> operator.mul(a,b)
252

>>> operator.sub(a,b)
-9

>>> operator.truediv(a,b)
0.5714285714285714

>>> operator.floordiv(a,b)
0

>>> operator.mod(a,b)
12

>>> #less then

>>> operator.lt(a,b)
True

>>> operator.le(a,b)
True

>>> operator.gt(a,b)
False

>>> operator.ge(a,b)
False

>>> operator.ne(a,b)
True

>>> operator.abs(12)
12

>>> operator.iadd.__doc__
'Same as a += b.'

>>> operator.iadd(12,3)
15

>>> a
12

>>> b
21

>>> operator.iadd(a,b)
33

>>> a
12

>>> l=[1,4,6,8,5,3]


>>> for i in l:
	print(i,end=' ')

	
1 4 6 8 5 3 

>>> operator.setitem(l,3,5)

>>> l
[1, 4, 6, 5, 5, 3]

>>> operator.delitem(l,3)

>>> l
[1, 4, 6, 5, 3]

>>> operator.getitem(l,1)
4


>>> operator.setitem(l,slice(0,4),[1,2,3,5])

>>> l
[1, 2, 3, 5, 3]

>>> operator.setitem(l,slice(0,4),[7,8,9,0])

>>> l
[7, 8, 9, 0, 3]

>>> operator.delitem(l,slice(0,3))

>>> l
[0, 3]

>>> l=[0,1,2,3,4,5,6,7,8]


>>> operator.getitem(l,4)
4

>>> operator.getitem(l,slice(0,4))
[0, 1, 2, 3]


>>> operator.add('gopi','raj')
'gopiraj'

>>> operator.concat('gopi','raj')
'gopiraj'

>>> operator.contains('gopi','gopiraj')
False

>>> operator.contains('gopiraj','gopi')
True

>>> a
12

>>> b
21

>>> operator.and_(a,b)
4

>>> operator.or_(a,b)
29

>>> b
21

>>> a
12

>>> operator.or_.__doc__
'Same as a | b.'

>>> 12 | 21
29


>>>#==============================================

>>> s='gopiraj'

>>> s[0]
'g'

>>> s[0]='G'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[0]='G'
TypeError: 'str' object does not support item assignment

>>> s
'gopiraj'

>>> l=[1,12.234,'gopi','A']

>>> l.append('Sathish kuamr')

>>> l
[1, 12.234, 'gopi', 'A', 'Sathish kuamr']

>>> l.pop()
'Sathish kuamr'

>>> l
[1, 12.234, 'gopi', 'A']

>>> l[1]
12.234

>>> l[1]='sathish kumar'


>>> l
[1, 'sathish kumar', 'gopi', 'A']

>>> t=('gopi','G',123,123.123)

>>> t
('gopi', 'G', 123, 123.123)

>>> t[1]
'G'

>>> t[4]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t[4]
IndexError: tuple index out of range

>>> t[3]
123.123

>>> t[0]='gopi'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t[0]='gopi'
TypeError: 'tuple' object does not support item assignment


>>> i=0

>>> while i<11:
	print(i)
	i+=1

	
0
1
2
3
4
5
6
7
8
9
10

>>> s='hellow world'

>>> for i in s:
	print(i)

	
h
e
l
l
o
w
 
w
o
r
l
d

>>> l=[1,2,3,4,5,'a','f','gopiraj']


>>> for i in l:
	print(i)

	
1
2
3
4
5
a
f
gopiraj


>>> for i in range(0,10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9

>>> d={}


>>> d['name']='gopi'

>>> d
{'name': 'gopi'}

>>> d['age']=21

>>> d['city']='salem'

>>> d
{'name': 'gopi', 'age': 21, 'city': 'salem'}


>>> s={'gopi':'name'}

>>> s
{'gopi': 'name'}

>>> s['gopi']
'name'

>>> s[1]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s[1]
KeyError: 1

>>> s[0]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s[0]
KeyError: 0




>>> x='name'

>>> y='gopi'

>>> d={}

>>> d[x]=y

>>> d
{'name': 'gopi'}




>>> x,y=input('enter your key and value:').split()
enter your key and value:name gopi

>>> x
'name'

>>> y
'gopi'

>>> def fun():
	d={}
	x,y=input('enter your key and value:').split(',')
	d[x]=y

	
>>> fun()
enter your key and value:name,gopi

>>> d
{'name': 'gopi'}

>>> fun()
enter your key and value:age,21

>>> d
{'name': 'gopi'}

>>> d
{'name': 'gopi'}

>>> s={}

>>> s
{}

>>> def fun():
	x,y=input('enter your key and value:').split(',')
	s[x]=y

	
>>> fun()
enter your key and value:name,gopi

>>> s
{'name': 'gopi'}

>>> fun()
enter your key and value:city,salem

>>> s
{'name': 'gopi', 'city': 'salem'}

>>> fun()
enter your key and value:age,21

>>> s
{'name': 'gopi', 'city': 'salem', 'age': '21'}

>>> s
{'name': 'gopi', 'city': 'salem', 'age': '21'}

>>> for i in s:
	i

	
'name'
'city'
'age'

>>> for i in s:
	print(i,'-->',s[i])

	
name --> gopi
city --> salem
age --> 21

>>> s
{'name': 'gopi', 'city': 'salem', 'age': '21'}



>>> for i in s:
	print('%s  , %s '%(i,s[i]))

	
name  , gopi 
city  , salem 
age  , 21 

>>> enumerate
<class 'enumerate'>

>>> enumerate.__doc__
'Return an enumerate object.\n\n  iterable\n    an object supporting iteration\n\nThe enumerate object yields pairs containing a count (from start, which\ndefaults to zero) and a value yielded by the iterable argument.\n\nenumerate is useful for obtaining an indexed list:\n    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...'



>>> for index,key in enumerate(s):
	print(index,key,s[key])

	
0 name gopi
1 city salem
2 age 21

>>> l=[1,2,3,4,5,6,7,'gopi','satish','kuamr']


>>> for i,j in enumerate(l):
	print(i,j)

	
0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 gopi
8 satish
9 kuamr

>>> l=[1,2,3,4,5,6,7]

>>> def breakTest():
	for i in l:
		if i==5:
			break
		print(i)
	print('')

	
>>> breakTest()
1
2
3
4


>>> def continueTest():
	for i in l:
		if i==5:
			continue
		print(i)
	print('')

	
>>> continueTest()
1
2
3
4
6
7


>>> l
[1, 2, 3, 4, 5, 6, 7]

>>> def breakTest():
	for i in l:
		if i==5:
			print('bresk the loop ')
			break
		print(i)
	print('')

	
>>> breakTest()
1
2
3
4
bresk the loop 

>>> def continueTest():
	for i in l:
		if i==5:
			print('mising elment 5')
			continue
		print(i)
	print('')

	

>>> continueTest()
1
2
3
4
mising elment 5
6
7


>>> def passTest(value):
	pass

>>> passTest(l)

>>> l
[1, 2, 3, 4, 5, 6, 7]

>>> list(map(lambda x:x**3,l))
[1, 8, 27, 64, 125, 216, 343]

>>> s=list(map(lambda x:x**3,l))

>>> s
[1, 8, 27, 64, 125, 216, 343]

>>> (lambda x:x**5)
<function <lambda> at 0x00000140841F2670>

>>> (lambda x:x**5)(3)
243

>>> (lambda x:x**5)(3)
243

>>> def outer(a):
	a+=1
	def inner(b):
		b=a+b
		def final(c):
			c=a+b+c
			print(c)
		return final
	return inner



>>> def outer(a):
	a+=1
	def inner(b):
		b=a+b
		def final(c):
			c=a+b+c
			print(c)
		print('b',b)
		return final
	print('a',a)
	return inner

>>> outer(1)(2)(3)
a 2
b 4
9

>>> m=range(-10,10)

>>> m
range(-10, 10)

>>> print(m)
range(-10, 10)

>>> filter(lambda x:x<9,m)
<filter object at 0x00000140841BEC70>

>>> list(filter(lambda x:x<9,m))
[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

>>> for i in filter(lambda x:x<9,m):
	print(i,end=' ')

	
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 

>>> x=[2,3,4,5,6]

>>> y=[]

>>> for i in x:
	if i%2:
		y+=[i*5]
	print(y)

	
[]
[15]
[15]
[15, 25]
[15, 25]
