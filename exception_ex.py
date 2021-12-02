>>> class my_cls:
	pass

>>> obj=my_cls()

>>> obj.attribute
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    obj.attribute
AttributeError: 'my_cls' object has no attribute 'attribute'

>>> while True:
	deta =input('enter a string:')
	print('hellow',data)

	
enter a string:'ad'
Traceback (most recent call last):
  File "<pyshell#10>", line 3, in <module>
    print('hellow',data)
NameError: name 'data' is not defined

>>> while True:
	deta =input('enter a string:')
	print('hellow',data)

	
enter a string:gopi
Traceback (most recent call last):
  File "<pyshell#12>", line 3, in <module>
    print('hellow',data)
NameError: name 'data' is not defined

>>> while True:
	data =input('enter a string:')
	print('hellow',data)

	
enter a string:gopi
hellow gopi
enter a string:
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    data =input('enter a string:')
KeyboardInterrupt

>>> import math

>>> math.exp(1000)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    math.exp(1000)
OverflowError: math range error

>>> def fun():
	try:
		for i in range(5):
			print('yieled',i)
			yield i
	except GeneratorExit:
		print('Exicitin early')

		
>>> s=fun()

>>> s.throw
<built-in method throw of generator object at 0x000002AB866B4970>

>>> s.gi_code
<code object fun at 0x000002AB865E7450, file "<pyshell#31>", line 1>

>>> s.gi_code()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s.gi_code()
TypeError: 'code' object is not callable

>>> next(s)
yieled 0
0

>>> next(s)
yieled 1
1

>>> next(s)
yieled 2
2

>>> next(s)
yieled 3
3

>>> next(s)
yieled 4
4

>>> next(s)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    next(s)
StopIteration

>>> import module_does_not_exit
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    import module_does_not_exit
ModuleNotFoundError: No module named 'module_does_not_exit'


>>> import exception
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    import exception
ModuleNotFoundError: No module named 'exception'

>>> import exceptions
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    import exceptions
ModuleNotFoundError: No module named 'exceptions'


>>> import Userexception
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    import Userexception
ModuleNotFoundError: No module named 'Userexception'

>>> array=[1,2,3,4]

>>> array[9]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    array[9]
IndexError: list index out of range

>>> dict(name:'
     
SyntaxError: invalid syntax

>>> dict(name:'gopi',age:'21')
SyntaxError: invalid syntax

>>> dict(name='gopi',age='21')
{'name': 'gopi', 'age': '21'}

>>> s=dict(name='gopi',age='21')

>>> s
{'name': 'gopi', 'age': '21'}

>>> s[age]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s[age]
NameError: name 'age' is not defined

>>> s['age']
'21'

>>> s['name']
'gopi'


>>> s[city]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s[city]
NameError: name 'city' is not defined

>>> try:
	print ('Press Return or Ctrl-C:',)
	ignored = input()
except Exception, err:
	print ('Caught exception:', err)
except KeyboardInterrupt, err:
	print ('Caught KeyboardInterrupt')
else:
	print ('No exception')

SyntaxError: invalid syntax

>>> import sys

>>> sys.maxsize
9223372036854775807

>>> len(sys.maxsize)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    len(sys.maxsize)
TypeError: object of type 'int' has no len()

>>> for i in range(0, 100, 10):
    print ('%2d' % i, 2L ** i)
    
SyntaxError: invalid syntax

>>> for i in range(0, 100, 10):print ('%2d' % i, 2L ** i)
SyntaxError: invalid syntax

>>> for i in range(0, 100, 10):print ('%2d' % i, 2L ** i)
SyntaxError: invalid syntax

>>> for i in range(0, 100, 10):
	print ('%2d' % i, 2L ** i)
	
SyntaxError: invalid syntax

>>> for i in range(0, 100, 10):
	print ('%2d' % i, 2L ** i)
	
SyntaxError: invalid syntax

>>> repr("gopi")
"'gopi'"

>>> repr("gopi")
"'gopi'"



>>> class myclass(Exception):
	def __init__(self,name):
		self.value=name
	def __str__(self):
		return repr(self.value)


>>> try:
	raise(myclass('gopi'))
except MyError as error:
	print('A New Exception occured: ',error.value)

	
Traceback (most recent call last):
  File "<pyshell#118>", line 2, in <module>
    raise(myclass('gopi'))
myclass: 'gopi'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#118>", line 3, in <module>
    except MyError as error:
NameError: name 'MyError' is not defined



>>> try:
	raise(myclass('gopi'))
except :
	print('A New Exception occured: ',error.value)

	
Traceback (most recent call last):
  File "<pyshell#129>", line 2, in <module>
    raise(myclass('gopi'))
myclass: 'gopi'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#129>", line 4, in <module>
    print('A New Exception occured: ',error.value)
NameError: name 'error' is not defined

>>> try:
	raise(myclass(3*2))
except :
	print('A New Exception occured: ',error.value)

	
Traceback (most recent call last):
  File "<pyshell#131>", line 2, in <module>
    raise(myclass(3*2))
myclass: 6

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#131>", line 4, in <module>
    print('A New Exception occured: ',error.value)
NameError: name 'error' is not defined

>>> try:
	raise(myclass(3*2))
except myclass as error:
	print('A New Exception occured: ',error.value)

	
A New Exception occured:  6

>>> try:
	raise(myclass(gopi))
except myclass as error:
	print('A New Exception occured: ',error.value)

	
Traceback (most recent call last):
  File "<pyshell#139>", line 2, in <module>
    raise(myclass(gopi))
NameError: name 'gopi' is not defined

>>> try:
	raise(myclass('gopi'))
except myclass as error:
	print('A New Exception occured: ',error.value)

	
A New Exception occured:  gopi

>>> raise(myclass('gopi'))
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    raise(myclass('gopi'))
myclass: 'gopi'

>>> try:
	raise(myclass('gopi'))
except myclass as error:
	global s
	s=error
	print('A New Exception occured: ',error.value)

	
A New Exception occured:  gopi

>>> s
myclass('gopi')

>>> s.args
('gopi',)

>>> s.with_traceback
<built-in method with_traceback of myclass object at 0x000002AB866C4B80>

	 
	 
>>>#================================================================


>>> class myclass(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return self.value

	
>>> s=myclass('Error')

>>> s.value
'Error'

>>> s.args
('Error',)

>>> class myclass():
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return self.value

	
>>> s=myclass('Error')

>>> s.value
'Error'

>>> raise s.value
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    raise s.value
TypeError: exceptions must derive from BaseException

>>> class myclass(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return self.value

	
>>> s=myclass('Error')

>>> raise s.value
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    raise s.value
TypeError: exceptions must derive from BaseException

>>> try:
	raise myclass('Gopi')
except myclass as error:
	print(error)

	
Gopi

>>> class error(Exception):
	pass


>>> class my_class(error):
	def __init__(self,prev,mul,resu):
		self.prev=prev
		self.mul=mul
		self.resu=resu

		

>>> try:
	raise(my_class('mul',2*3,'Not Allowed'))
except my_class as e:
	print('error occured is:',e.resu)

	
error occured is: Not Allowed

>>> try:
	raise(my_class('mul',2*3,'Not Allowed'))
except my_class as error:
	print('error occured is:',error.resu)

	
error occured is: Not Allowed

>>> class my_class(RuntimeError):
	def __init__(self,value):
		self.value=value

		

>>> try:
	raise my_class('error')
except my_class as e:
	print('erroe occured is:',e.args)

	
erroe occured is: ('error',)

>>> try:
	raise my_class('error')
except my_class as e:
	print(e.args)

	
('error',)

>>> try:
	raise my_class("error")
except my_class as e:
	print(e.args)

	
('error',)

>>> class my_class(RuntimeError):
	def __init__(self,value):
		self.value=value

		
>>> s=my_class('Gopiraj')

>>> s.args
('Gopiraj',)

>>> s.value
'Gopiraj'

	 
>>> s.with_traceback()
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    s.with_traceback()
TypeError: BaseException.with_traceback() takes exactly one argument (0 given)

	 

>>> try:
	print(10/0)
except:
	print('an exception raiced')
finally:
	print('stop the coding')

	
an exception raiced
stop the coding

>>> try:
	amount=input('enter your amount:')	if
	
SyntaxError: invalid syntax

>>> try:
	amount=input('enter your amount:')
	if amount<2000:
		raise ValueError('you account money lower then minmun level')
	print('your account current level maintaing')
except ValueError as e:
	print(e)
finally:
	print('coding success fully run')

	
enter your amount:1234
coding success fully run
Traceback (most recent call last):
  File "<pyshell#24>", line 3, in <module>
    if amount<2000:
TypeError: '<' not supported between instances of 'str' and 'int'



>>> try:
	amount=int(input('enter your amount:'))
	if amount<2000:
		raise ValueError('you account money lower then minmun level')
	print('your account current level maintaing')
except ValueError as e:
	print(e)
finally:
	print('coding success fully run')

	
enter your amount:1233
you account money lower then minmun level
coding success fully run


>>> try:
	amount=int(input('enter your amount:'))
	if amount<2000:
		raise ValueError('you account money lower then minmun level')
	print('your account current level maintaing')
except ValueError as e:
	print(e)
finally:
	print('coding success fully run')

	
enter your amount:12345
your account current level maintaing
coding success fully run

>>> print('local() method:::',locals())
local() method::: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'amount': 12345}

>>> print('global() method:::',global())
SyntaxError: invalid syntax

>>>  globals()
 
SyntaxError: unexpected indent

>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'amount': 12345}

>>> def fun():
	n='gopi'
	a=21
	c='salem'

	
>>> def fun():
	n='gopi'
	a=21
	c='salem'
	print(locals())

	
>>> fun()
{'n': 'gopi', 'a': 21, 'c': 'salem'}


>>> def fun():
	n='gopi'
	a=21
	c='salem'
	print('loval::',locals())
	print('globals::',globals())

	
>>> fun()
loval:: {'n': 'gopi', 'a': 21, 'c': 'salem'}
globals:: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'amount': 12345, 'fun': <function fun at 0x000001EEA2533550>}

>>> def fun():
	n='gopi'
	a=21
	c='salem'
	print('loval::',locals()['n']='sathish')
	print(n)
	print('globals::',globals())
	
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

>>> def fun():
	n='gopi'
	a=21
	c='salem'
	print('loval::',locals())
	locals()['n']='sathish'
	print(n)
	print('globals::',globals())

	
>>> fun()
loval:: {'n': 'gopi', 'a': 21, 'c': 'salem'}
gopi
globals:: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'amount': 12345, 'fun': <function fun at 0x000001EEA25334C0>}


	 
>>>#===================================================================================
	 
	 

>>> try:
	a=10/0
	print(a)
except:
	print('Zerodivition error')
finally:
	print('coding is run succesh fully')

	
Zerodivition error
coding is run succesh fully


>>> try:
	a=10/0
	print(a)
except ArithmeticError as  a:
	print('Zerodivition error:',a)
finally:
	print('coding is run succesh fully')

	
Zerodivition error: division by zero
coding is run succesh fully


>>> try:
	a=10/0
	print(a)
except Exception as a
	print('Zerodivition error:',a)
finally:
	print('coding is run succesh fully')
	
SyntaxError: invalid syntax


>>> try:
	a=10/0
	print(a)
except Exception as a:
	print('Zerodivition error:',a)
finally:
	print('coding is run succesh fully')

	
Zerodivition error: division by zero
coding is run succesh fully


>>> try:
	a=10/0
	print(a)
except ZeroDivisionError as a:
	print('Zerodivition error:',a)
finally:
	print('coding is run succesh fully')

	
Zerodivition error: division by zero
coding is run succesh fully


>>> try:
	a=[1,2,3,4]
	print(a[4])
except LookupError as a:
	print(a)
finally:
	print('success')

	
list index out of range
success

>>> class attribute(object):
	pass

>>> s=attribute()

>>> s.attribute
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.attribute
AttributeError: 'attribute' object has no attribute 'attribute'

>>> s.__str__()
'<__main__.attribute object at 0x000001C30A53C850>'

>>> s.__ge__('GOPi')
NotImplemented

>>> while True:
	Name=input('enter your name')
	print('hello ',Name)

	
enter your namegopi
hello  gopi
enter your namesathish
hello  sathish
enter your namegopal
hello  gopal
enter your nameindumathi
hello  indumathi
enter your namegowri
hello  gowri
enter your name
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    Name=input('enter your name')
KeyboardInterrupt


>>> import math

>>> help(math.exp)
Help on built-in function exp in module math:

exp(x, /)
    Return e raised to the power of x.


>>> math.exp(3)
20.085536923187668

>>> math.exp(1)
2.718281828459045


>>> print()

>>> print(math.exp(3))
20.085536923187668

>>> print(math.exp(3000))
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(math.exp(3000))
OverflowError: math range error

>>> math.exp(3000)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    math.exp(3000)
OverflowError: math range error

>>> try:
	for i in range(5):
		print('Yielded:',i)
		yield i
except GeneratorExit as a:
	print(a)
	
SyntaxError: 'yield' outside function

>>> try:
	for i in range(5):
		print('Yielded:',i)
		yield i
except GeneratorExit:
	print("Exiting error")
	
SyntaxError: 'yield' outside function


>>> try:
	for i in range(5):
		print('Yielded:',i)
	yield i
except GeneratorExit:
	print("Exiting error")
	
SyntaxError: 'yield' outside function

>>> try:
	for i in range(5):
		print('Yielded:',i)
		yield i
except GeneratorExit:
	print("Exiting error")
	
SyntaxError: 'yield' outside function

>>> import dummy_modules
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    import dummy_modules
ModuleNotFoundError: No module named 'dummy_modules'

>>> from math import factorial

>>> factorial(3)
6

>>> from math import factorials
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    from math import factorials
ImportError: cannot import name 'factorials' from 'math' (unknown location)

>>> from math import factorial as f

>>> f(3)
6

>>> array=[1,2,3]

>>> array[4]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    array[4]
IndexError: list index out of range

>>> d={'name':}
SyntaxError: invalid syntax

>>> d={'name':'gopi','age':'21'}

>>> d['name']
'gopi'

>>> d['city']
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    d['city']
KeyError: 'city'

>>> def fun(x):
	factorial=[]
	for i in range(1,x+1):
		if x%i==0:
			factorial.append(i)
	return factorial

>>> num=123

>>> fun(num)
[1, 3, 41, 123]

>>> num=600851475143

>>> fun(num)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    fun(num)
  File "<pyshell#114>", line 4, in fun
    if x%i==0:
KeyboardInterrupt

>>> fun(num)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    fun(num)
  File "<pyshell#114>", line 4, in fun
    if x%i==0:
KeyboardInterrupt


>>> print 'gopi'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('gopi')?

>>> def fun()
SyntaxError: invalid syntax

>>> def fun():
	print ans
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(ans)?
>>> def fun():
	print(namem)

	
>>> fun()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    fun()
  File "<pyshell#127>", line 2, in fun
    print(namem)
NameError: name 'namem' is not defined


>>> class my_class(object):
	def print_msg(self):
		print(self.__class__.__name__)

		
>>> s=my_class()

>>> s.print_msg()
my_class


>>> class my_class(object):
	def print_msg(self):
		print(self.__class__)

		

>>> s=my_class()

>>> s.print_msg()
<class '__main__.my_class'>

>>> class bash_class(object):
	def __init__(self):
		super(bash_class,self).__init__()
	def do_somthing(self):
		raise NotImplementedError(self.__class__.__name__)

	

>>> class my_class(bash_class):
	def do_somthing(self):
		print(self.__class__.__name__)

		
>>> my_class().do_somthing()
my_class

>>> bash_class().do_somthing()
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    bash_class().do_somthing()
  File "<pyshell#153>", line 5, in do_somthing
    raise NotImplementedError(self.__class__.__name__)
NotImplementedError: bash_class

>>> import sys

>>> print('regular integer:',sys.maxsize)
regular integer: 9223372036854775807

>>> 9223372036854775807+12
9223372036854775819

>>> 9223372036854775807*123
1134474760533137424261

>>> 9223372036854775807*12345678
113868781241213194875412146

>>> 9223372036854775807*12345678123456789
113868782379901090297892426447103723

>>> 9223372036854775807*123456781234567891234567890
1138687823799010914365803218695840034471037230



>>> import sys

>>> try:
	i=sys.maxsize*3
	print('	NO Overflow for ',type(i),'i=',i)
except OverflowError as e:
	print(e)

	
	NO Overflow for  <class 'int'> i= 27670116110564327421

>>> try:
	i=sys.maxsize*3
	print('	NO Overflow for ',type(i),'i=',i)
except OverflowError ,err:
	print(err)
	
SyntaxError: invalid syntax

>>> arr=[1,2,3,4]

>>> i=iter(arr)

>>> for i in i:
	print(next(i))

	
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    print(next(i))
TypeError: 'int' object is not an iterator

>>> i
1

>>> i
1

>>> arr=[4,3,2,1]

>>> num=iter(arr)

>>> num
<list_iterator object at 0x0000015C8D58BD90>

>>> next(num)
4

>>> next(num)
3

>>> next(num)
2

>>> next(num)
1

>>> next(num)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    next(num)
StopIteration

>>> eval('gopiraj sathish kuamr')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    eval('gopiraj sathish kuamr')
  File "<string>", line 1
    gopiraj sathish kuamr
            ^
SyntaxError: invalid syntax

>>> try:
	eval('gopiraj sathish kuamr')
except SyntaxError as s:
	print(s.filename,s.lineno,s.offset,s.text)

	
<string> 1 9 gopiraj sathish kuamr

>>> try:
	s=eval('gopiraj sathish kuamr')
except SyntaxError as s:
	print(s.filename,s.lineno,s.offset,s.text)

	
<string> 1 9 gopiraj sathish kuamr

>>> s
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s
NameError: name 's' is not defined
	 
	 

	 
>>>#======================================================
	 
	 
>>> class Networkerror(RuntimeError):
	def __init__(self,name):
		self.name=name

	
>>> s=Networkerror('gopiraj')

>>> s.args
('gopiraj',)

>>> s.name
'gopiraj'


>>> try:
	raise Networkerror('Gopiraj')
except Networkerror as e:
	print(e)

	
Gopiraj


>>> class myerror(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return repr(self.value)

	

>>> try:
	raise myerror('user define error is: NOT VALIED')
except myerror as s:
	print(s)

	
'user define error is: NOT VALIED'


>>> class myerror(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return self.value

	


>>> try:
	raise myerror('user define error is: NOT VALIED')
except myerror as s:
	print(s)

	
user define error is: NOT VALIED


>>> class Error(Exception):
	def __init__(self,value):
		self.value=value

	

>>> class Error(Exception):
	pass





>>> class TransitionError(Error):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return self.value

	


>>> try:
	raise TransitionError('super class exception : NOt VALIED')
except TransitionError as e:
	print(e)

	
super class exception : NOt VALIED


>>> class Networkerro(RuntimeError):
	def __init__(self,value):
		print(value)

		

>>> try:
	raise Networkerro('user definr super class exception : NOT VALIED')
except Networkerro as e:
	print(e)

	
user definr super class exception : NOT VALIED
user definr super class exception : NOT VALIED


>>> try:
	raise Networkerro('user definr super class exception : NOT VALIED')
except Networkerro as e:
	print(e)

	
user definr super class exception : NOT VALIED
user definr super class exception : NOT VALIED


>>> class Networkerror(RuntimeError):
	def __init__(self,name):
		self.name=name

		
>>> try:
	raise Networkerror('Gopiraj')
except Networkerror as e:
	print(e)

	
Gopiraj


>>> try:
	raise Networkerror('user definr super class exception : NOT VALIED')
except Networkerror as e:
	print(e)

	
user definr super class exception : NOT VALIED



>>> class Networkerro(RuntimeError):

	def __init__(self,value):
		self.value=value

		

>>> try:
	raise Networkerro('user definr super class exception : NOT VALIED')
except Networkerro as e:
	print(e)

	
user definr super class exception : NOT VALIED


>>> class myclass(object):
	def __init__(self,value):
		print(value)

		

>>> s=myclass('Gopi')
Gopi

>>> s.__str__
<method-wrapper '__str__' of myclass object at 0x000001B4E7E5EC70>

>>> s.__str__()
'<__main__.myclass object at 0x000001B4E7E5EC70>'


>>> str
<class 'str'>



>>> x,y=input('Enter a number').split(' ')
Enter a number12 33

>>> x
'12'

>>> y
'33'

>>> x=int(x)

>>> x
12

>>> y=int(y)

>>> y
33


>>> print(x, '' ,y)
12  33	 
	 
>>>print(x)
12
	 
>>>print('Gopiraj')	 
Gopiraj
	 
>>>#=========================================================
	 
	 
	 
	 

>>> from math import cube
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from math import cube
ImportError: cannot import name 'cube' from 'math' (unknown location)

>>> l=[1,2,3,4]

>>> l[0]
1

>>> l[2]
3

>>> l[3]
4

>>> l[5]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    l[5]
IndexError: list index out of range


>>> i=iter(l)

>>> next(i,'list out of range')
1

>>> next(i,'list out of range')
2

>>> next(i,'list out of range')
3

>>> next(i,'list out of range')
4

>>> next(i,'list out of range')
'list out of range'

>>> next(i,'list out of range')
'list out of range'

>>> next(i)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    next(i)
StopIteration

>>> d={'name':'Gopiraj','age':'21'}

>>> d['name']
'Gopiraj'

>>> d.values('name')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d.values('name')
TypeError: dict.values() takes no arguments (1 given)

>>> d.values()
dict_values(['Gopiraj', '21'])

>>> s=d.values()

>>> for i in s:
	i

	
'Gopiraj'
'21'

>>> '2'+2
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    '2'+2
TypeError: can only concatenate str (not "int") to str

>>> '2'*2
'22'

>>> 2+'2'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    2+'2'
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> age
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    age
NameError: name 'age' is not defined


>>> x=100/0
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    x=100/0
ZeroDivisionError: division by zero

>>> x
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    x
NameError: name 'x' is not defined

>>> while True:
	name=input('Enter your name:')
	print(name)

	
Enter your name:gopi
gopi
Enter your name:sathish
sathish
Enter your name:parimal
parimal
Enter your name:
Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    name=input('Enter your name:')
KeyboardInterrupt


>>> try:
	x=12
	y='9'
	ans=x+y
	print(ans)
except:
	print('Some Error Occured')

	
Some Error Occured


>>> try:
	x=12
	y='9'
	ans=x+y
	print(ans)
except TypeError:
	print('Unsupport Operator find')

	
Unsupport Operator find

>>> try:
	ans=12/0
	print(ans)
except TypeError:
	print('Unsupport operaor')
except ZeroDivisionError:
	print('canot divided number by zero')

	
canot divided number by zero


>>> try:
	print('Try block')
	n=int(input("Enter a number:"))
	m=int(input('Enter a number:'))
	ans=n/m
except ZeroDivisionError:
	print('Except ZerodivisionError block')
	print('Canot divided a number by zero')
else:
	print('Else Block')
	print("Division is :",ans)
finally:
	print('finally block')

	
Try block
Enter a number:2
Enter a number:3
Else Block
Division is : 0.6666666666666666
finally block

>>> x
12

>>> n
2

>>> m
3

>>> try:
	print('Try block')
	n=int(input("Enter a number:"))
	m=int(input('Enter a number:'))
	ans=n/m
except ZeroDivisionError:
	print('Except ZerodivisionError block')
	print('Canot divided a number by zero')
else:
	print('Else Block')
	print("Division is :",ans)
finally:
	print('finally block')
	n,m=0,0

	
Try block
Enter a number:
finally block
Traceback (most recent call last):
  File "<pyshell#110>", line 3, in <module>
    n=int(input("Enter a number:"))
ValueError: invalid literal for int() with base 10: ''


>>> try:
	print('Try block')
	n=int(input("Enter a number:"))
	m=int(input('Enter a number:'))
	ans=n/m
except ZeroDivisionError:
	print('Except ZerodivisionError block')
	print('Canot divided a number by zero')
else:
	print('Else Block')
	print("Division is :",ans)
finally:
	print('finally block')
	n,m=0,0

	
Try block
Enter a number:3
Enter a number:5
Else Block
Division is : 0.6
finally block


>>> n
0

>>> m
0


>>> try:
	x=int(input("enter a number:"))
	if x>100:
		raise ValueError(x)
except ValueError:
	print(x,'Is out of allowed range')
else:
	print(x,'is within the allowed range')

	
enter a number:3
3 is within the allowed range


>>> try:
	x=int(input("enter a number:"))
	if x>100:
		raise ValueError(x)
except ValueError:
	print(x,'Is out of allowed range')
else:
	print(x,'is within the allowed range')

	
enter a number:123
123 Is out of allowed range	 
	 
	 
>>>#=====================================================


>>> x=0


>>> assert x>0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    assert x>0
AssertionError

>>> x=0

>>> assert x>=0

>>> print('x value is :',x)
x value is : 0


>>> def fun(x):
	assert x>=0,'only positive number alllowed'
	print(x*x)

	
>>> fun(2)
4

>>> fun(-2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fun(-2)
  File "<pyshell#15>", line 2, in fun
    assert x>=0,'only positive number alllowed'
AssertionError: only positive number alllowed

>>> try:
	fun(2)
except AssertionError as msg:
	print(msg)

	
4

>>> try:
	fun(22)
except AssertionError as msg:
	print(msg)

	
484

>>> try:
	fun(22)
except AssertionError as msg:
	print(msg)

	
484

>>> try:
	fun(-22)
except AssertionError as msg:
	print(msg)

	
only positive number alllowed



>>> class Student(object):
	attr='Muthayammal collage of Arts & Science' #class atrribute
	def __init__(self,name,age):
		self.name=name #instance Attribute
		self.age=age # insstance Attribute

		

>>> obj=Student('GOPIRAJ',22)

>>> obj.attr
'Muthayammal collage of Arts & Science'

>>> obj.age
22

>>> obj.name
'GOPIRAJ'

>>> class Student(object):
	_attr='Muthayammal collage of Arts & Science' #class atrribute
	def __init__(self,name,age):
		self.name=name #instance Attribute
		self.age=age # insstance Attribute

		
>>> obj=Student('GOPIRAJ',22)

>>> obj.age
22

>>> obj.name
'GOPIRAJ'

>>> obj._attr
'Muthayammal collage of Arts & Science'


>>> class Student(object):
	_attr='Muthayammal collage of Arts & Science' #class atrribute
	def __init__(self,name,age):
		self.name=name #instance Attribute
		self.age=age # insstance Attribute
	def msg(self):
		print(self.name ' collage is :',self._attr)
		
SyntaxError: invalid syntax


>>> class Student(object):
	_attr='Muthayammal collage of Arts & Science' #class atrribute
	def __init__(self,name,age):
		self.name=name #instance Attribute
		self.age=age # insstance Attribute
	def msg(self):
		print(self.name ,' collage is :',self._attr)

		
>>> obj=Student('GOPIRAJ',22)

>>> obj.age
22

>>> obj.msg()
GOPIRAJ  collage is : Muthayammal collage of Arts & Science


>>> class Student(object):
	_attr='Muthayammal collage of Arts & Science' #class atrribute
	def __init__(self,name,age):
		self.name=name #instance Attribute
		self.age=age # insstance Attribute
	def msg(self):
		print(self.name ,' collage is :',self.attr)

		
>>> obj=Student('GOPIRAJ',22)

>>> obj.msg()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    obj.msg()
  File "<pyshell#75>", line 7, in msg
    print(self.name ,' collage is :',self.attr)
AttributeError: 'Student' object has no attribute 'attr'


>>> class Student(object):
	_attr='Muthayammal collage of Arts & Science' #class atrribute
	def __init__(self,name,age):
		self.name=name #instance Attribute
		self.age=age # insstance Attribute
	def msg(self):
		print(self.name ,' collage is :',Student._attr)

		
>>> obj=Student('GOPIRAJ',22)

>>> obj.msg()
GOPIRAJ  collage is : Muthayammal collage of Arts & Science


>>> class Student(object):
	_attr='Muthayammal collage of Arts & Science' #class atrribute
	def __init__(self,name,age):
		self.name=name #instance Attribute
		self.age=age # insstance Attribute
	def msg(self):
		print(self.name ,' collage is :',Student.attr)

		
>>> obj=Student('GOPIRAJ',22)

>>> obj.msg()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    obj.msg()
  File "<pyshell#87>", line 7, in msg
    print(self.name ,' collage is :',Student.attr)
AttributeError: type object 'Student' has no attribute 'attr'


>>> class base(object):
	_clg=MCAS
	def __init__(self,name):
		self.name=name
	def greet(self):
		print('hellow mr ',self.name)

		
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    class base(object):
  File "<pyshell#99>", line 2, in base
    _clg=MCAS
NameError: name 'MCAS' is not defined

>>> class base(object):
	_clg='MCAS'
	def __init__(self,name):
		self.name=name
	def greet(self):
		print('hellow mr ',self.name)

		
>>> class superclass(base):
	def __init__(self):
		super(base).__init__()
	def msg(self):
		print(base._clg)

		

>>> s=superclass()

>>> s.greet
<bound method base.greet of <__main__.superclass object at 0x000001F215F4E1C0>>

>>> s.greet()
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    s.greet()
  File "<pyshell#103>", line 6, in greet
    print('hellow mr ',self.name)
AttributeError: 'superclass' object has no attribute 'name'

>>> class superclass(base):
	def __init__(self):
		super(base).__init__('GOPi')
	def msg(self):
		print(base._clg)

		
>>> s=superclass()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    s=superclass()
  File "<pyshell#115>", line 3, in __init__
    super(base).__init__('GOPi')
TypeError: super() argument 1 must be type, not str


>>> class base(object):
	def __init__(self,name):
		self._name=name
		
	def name(self):
		print('Hellow mr ',self._name)
	def setter(self,new_name):
		self._name=new_name

		
>>> b=base('Gopi')

>>> b.name()
Hellow mr  Gopi

>>> b.setter('Sathish kumar')

>>> b.name()
Hellow mr  Sathish kumar


>>> class base(object):
	def __init__(self,name):
		self._name=name
	@property	
	def name(self):
		print('Hellow mr ',self._name)
	@name.setter	
	def name(self,new_name):
		self._name=new_name

		

>>> s=base('Gopi')

>>> s.name
Hellow mr  Gopi

>>> s.name='sathish kuamr'

>>> s.name
Hellow mr  sathish kuamr

>>> class base():
	def __init__(self,name):"
	
SyntaxError: EOL while scanning string literal

>>> class base():
	__clg="MCAS
	def __init__(self,name):
		self.__name=name
		
SyntaxError: EOL while scanning string literal

>>> class base():

	__clg="MCAS"
	def __init__(self,name):
		self.__name=name
	def msg(self):
		print("hellow mr.",self.__name)
		print('His collage is ',__clg)

		
>>> s=base('Gopi raj')

>>> s.msg()
hellow mr. Gopi raj
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    s.msg()
  File "<pyshell#154>", line 7, in msg
    print('His collage is ',__clg)
NameError: name '_base__clg' is not defined


>>> class base():
	__clg="MCAS"
	def __init__(self,name):
		self.__name=name
	def msg(self):
		print("hellow mr.",self.__name)
		print('His collage is ',base.__clg)

		
>>> s=base('Gopi raj')


>>> s.msg()
hellow mr. Gopi raj
His collage is  MCAS

>>> s._base.__name
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    s._base.__name
AttributeError: 'base' object has no attribute '_base'

>>> s._base__name
'Gopi raj'

>>> s._base__name=
SyntaxError: invalid syntax

>>> s._base__name='sathish kumar'


>>> s.msg()
hellow mr. sathish kumar
His collage is  MCAS
	 
