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


