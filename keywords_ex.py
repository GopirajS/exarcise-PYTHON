
>>> s=list()

>>> type(s)
<class 'list'>

>>> s=[1,'gopi','hellow world']

>>> s.append('mark')

>>> s
[1, 'gopi', 'hellow world', 'mark']

>>> s.append(input('enter input:'))
enter input:sathish kumar

>>> s
[1, 'gopi', 'hellow world', 'mark', 'sathish kumar']

>>> s.append(input('enter input:'))
enter input:"gopal"

>>> s
[1, 'gopi', 'hellow world', 'mark', 'sathish kumar', '"gopal"']

>>> str('gopi')
'gopi'

>>> repr('Gopi')
"'Gopi'"

>>> num=10


>>> if num>5:
	print('5 is less then num')
elif num>9:
	print('9 is less then num')
else:
	print('if statement is completed')

	
5 is less then num

>>> def fun():
	print('hellow')
	print('hellow again')

	
>>> fun()
hellow
hellow again

>>> fun()
hellow
hellow again


>>> def getInteger():
	number=int(input('enter anumber'))
	return number


>>> def Main():
	print('starter')
	obj=getInteger()
	print(obj)

	
>>> getInteger()
enter anumber3
3


>>> Main()
starter
enter anumber3
3


>>> import keywords
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'

>>> import keyword


>>> keyword.softkwlist
[]

>>> keyword.softkwlist.__doc__
'Built-in mutable sequence.\n\nIf no argument is given, the constructor creates a new empty list.\nThe argument must be an iterable if specified.'

>>> s
[1, 'gopi', 'hellow world', 'mark', 'sathish kumar', '"gopal"']

>>> keyword.iskeyword('yierd')
False

>>> keyword.iskeyword('and')
True

>>> keyword.iskeyword('yield')
True

>>> keyword.issoftkeyword.__doc__
'x.__contains__(y) <==> y in x.'


>>> keyword.issoftkeyword('and')
False

>>> keyword.issoftkeyword('gopi')
False

>>> keyword.issoftkeyword.__dir__
<built-in method __dir__ of builtin_function_or_method object at 0x0000019C84E8E040>

>>> keyword.issoftkeyword.__dir__()
['__repr__', '__hash__', '__call__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce__', '__module__', '__doc__', '__name__', '__qualname__', '__self__', '__text_signature__', '__str__', '__setattr__', '__delattr__', '__init__', '__new__', '__reduce_ex__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

>>> print('list of keywords :')
list of keywords :

>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

>>> False==0
True

>>> False==1
False

>>> True==1
True



>>> True+True+True
3

>>> True+True+False
2

>>> True+True+False+True
3


>>> None==0
False

>>> None==1
False

>>> None==[]
False


>>> 3 and 0
0

>>> 3 and 10
10

>>> 3 and 2
2

>>> 3 and 1
1

>>> 3 and 1 and 3
3

>>> 3 and 1 or 3
1

>>> 3 and 1 or 3 or 2
1


>>> 3 and 4 or 3 or 2
4

>>> 1 or 2 or 3 or 4
1

>>> 0 or 2 or 3 or 4
2

>>> 0 or 2 or 0 or 4
2

>>> 0 or 2 or 0 or 0
2

>>> 0 or 2 or 0 or 0
2

>>> True and True
True

>>> True and False
False

>>> False and False
False


>>> not True
False

>>> not False
True

>>> not 2
False

>>> not 5
False

>>> not 0
True


>>> 0 is not [1,2,3,0,4]
True

>>> 0 is not [1,2,3,4]
True

>>> 'gopi' is not [1,2,3,4]
True

>>> 'gopi' is  [1,2,3,4]
False


>>> 'gopi' not in  [1,2,3,4]
True

>>> 'gopi' not in  [1,2,3,4]
True

>>> False or True
True

>>> True or False
True

>>> if 's ' in 'Gopirajs':
	print("yes,'s' is here ")

>>> if 's ' in 'Gopirajs':
	print("yes,'s' is here ")

	
>>> if 's ' in 'Gopirajs':
	print("yes,'s' is here ")
else:
	print("no 's' is not here")

	
no 's' is not here

>>> if 's' in 'Gopirajs':
	print("yes,'s' is here ")
else:
	print("no 's' is not here")

	
yes,'s' is here 

>>> print('/r')


>>> print('\r')


>>> print('\r')==print('\n')

True


>>> for i in range(10):
	print(i,end=' ')

	
0 1 2 3 4 5 6 7 8 9 

>>> for i in range(10):
	
	print(i,end=' ')
	if i==6:
		break

	
0 1 2 3 4 5 6 

>>> i=0


>>> while i<10:
	if i==6:
		i+=1
		continue
	else:
		print(i,end=' ')
		i+=1

		
0 1 2 3 4 5 7 8 9 

>>> while i<10:

	if i==6:
		i+=1
		continue
	else:
		print(i,end=' ')
	i+=1

	


>>> i=0

>>> while i<10:
	if i==6:
		i+=1
		continue
	else:
		print(i,end=' ')
	i+=1

	
0 1 2 3 4 5 7 8 9 

>>> i=0


>>> while i<10:
	if i==6:
		i+=1
		continue
	else:
		print(i,end=' ')
		i+=1

		
0 1 2 3 4 5 7 8 9 

>>> name='gopiraj'



>>> if name=='gopiraj':
	print('yes if condition is true')
elif name=='gopiraj':
	print('elif condtion is true')
else:
	print('else condiiton is true')

	
yes if condition is true


>>> def fucntion():
	print('hellow world')

	
>>> fucntion()
hellow world


>>> def fun():
	s=0
	for i in range(10):
		s+=i
	return s

>>> fun()
45

>>> def fun(x):
	s=0
	for i in range(x):
		s+=i
	return s

>>> fun(3)
3

>>> fun(10)
45

>>> fun(1)
0

>>> fun(2)
1

>>> fun(3)
3

>>> for i in range(1):
	print(i)

	
0

>>> for i in range(2):
	print(i)

	
0
1

>>> for i in range(3):
	print(i)

	
0
1
2

>>> def fun(x):
	s=0
	for i in range(x):
		s+=i
	return s

>>> fun(6)
15


>>> def fun(x):
	s=0
	for i in range(x):
		s+=i
		return s

	
>>> fun(5)
0

>>> fun(5)
0

>>> def fun(x):
	s=0
	for i in range(x):
		s+=i
		yield s

		
>>> fun(5)
<generator object fun at 0x0000019C872E2A50>

>>> for i in fun(5):
	print(i)

	
0
1
3
6
10

>>> fun(5)()
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    fun(5)()
TypeError: 'generator' object is not callable

>>> fun(5)
<generator object fun at 0x0000019C872E2BA0>


>>> class myclass(object):
	attr1='dog'
	attr2='rabit'
	def mymethod(self):
		print('first attr1 is :',self.attr1)
		print('second attr2 is :',myclss.attr2)

		
>>> s=myclass()

>>> s.mymethod
<bound method myclass.mymethod of <__main__.myclass object at 0x0000019C86E6E5E0>>

>>> s.mymethod()
first attr1 is : dog
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    s.mymethod()
  File "<pyshell#275>", line 6, in mymethod
    print('second attr2 is :',myclss.attr2)
NameError: name 'myclss' is not defined


>>> class myclass(object):
	attr1='dog'
	attr2='rabit'
	def mymethod(self):
		print('first attr1 is :',self.attr1)
		print('second attr2 is :',myclass.attr2)

		
>>> s=myclass()


>>> s.mymethod()
first attr1 is : dog
second attr2 is : rabit

>>> s.attr1
'dog'

>>> s.attr2
'rabit'


>>> for i in range(10):
	pass


>>> g=lambda x:x+x

>>> g(3)
6

>>> g(31)
62

>>> lambda x:x+x
<function <lambda> at 0x0000019C872E45E0>

>>> (lambda x:x+x)
<function <lambda> at 0x0000019C872E4700>

>>> (lambda x:x+x)(3)
6

>>> (lambda x:x+x)(3)
6
>>> (lambda x:x+x)(32)
64


>>> try:
	a=1
	b=0
	c=a/b
except ZeroDivisionError as E:
	print(E)
else:
	print('result is:',c)
finally:
	print('consept is runed')

	
division by zero
consept is runed


>>> try:
	a=1
	b=2
	c=a/b
except ZeroDivisionError as E:
	print(E)
else:
	print('result is:',c)
finally:
	print('consept is runed')

	
result is: 0.5
consept is runed


>>> name='Gopiraj'

>>> age=21

>>> name
'Gopiraj'

>>> age
21

>>> print('hellow mr.',name)
hellow mr. Gopiraj

>>> print('his age is:',age)
his age is: 21


>>> print(name)
Gopiraj

>>> del name

>>> print(name)
Traceback (most recent call last):
  File "<pyshell#338>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined

>>> n=10

>>> def fun():
	a=n+10
	print(a)

	
>>> fun()
20

>>> def fun():
	n=n+10
	print(a)

	
>>> def fun():
	n=n+10
	print(n)

	
>>> fun()
Traceback (most recent call last):
  File "<pyshell#356>", line 1, in <module>
    fun()
  File "<pyshell#355>", line 2, in fun
    n=n+10
UnboundLocalError: local variable 'n' referenced before assignment

>>> def fun():
	a=n+12
	print(a)

	
>>> fun()
22

>>> def fun():
	value=10
	def get():
		value=value+10
		print(value)
	get()

	
>>> fun()
Traceback (most recent call last):
  File "<pyshell#371>", line 1, in <module>
    fun()
  File "<pyshell#370>", line 6, in fun
    get()
  File "<pyshell#370>", line 4, in get
    value=value+10
UnboundLocalError: local variable 'value' referenced before assignment

>>> def fun():
	value=10
	def get():
		nonlocal value
		value=value+10
		print(value)
	get()

	

>>> fun()
20


>>> global s

>>> s
<__main__.myclass object at 0x0000019C86EAEDC0>
>>> s()
Traceback (most recent call last):
  File "<pyshell#384>", line 1, in <module>
    s()
TypeError: 'myclass' object is not callable

>>> s.mymethod()
first attr1 is : dog
second attr2 is : rabit

>>> def fun():
	value=10
	def get():
		nonlocal value
		value=value+10
		print(value)
	get()
	print('value:',value)

	
>>> fun()
20
value: 20

>>> value=10


>>> value=10

>>> value=10

>>> def fun():
	value=11
	def get():
		nonlocal value
		value+value+1
		print(value)
	get()
	print('value:',value)

	
>>> fun()
11
value: 11

>>> value=10

>>> def fun():
	value=11
	def get():
		nonlocal value
		value=value+1
		print(value)
	get()
	print('value:',value)


>>> fun()
12
value: 12

>>> value
10