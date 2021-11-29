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

>>> help(Exception)
Help on class Exception in module builtins:

class Exception(BaseException)
 |  Common base class for all non-exit exceptions.
 |  
 |  Method resolution order:
 |      Exception
 |      BaseException
 |      object
 |  
 |  Built-in subclasses:
 |      ArithmeticError
 |      AssertionError
 |      AttributeError
 |      BufferError
 |      ... and 15 other subclasses
 |  
 |  Methods defined here:
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseException:
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |  
 |  __setstate__(...)
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  with_traceback(...)
 |      Exception.with_traceback(tb) --
 |      set self.__traceback__ to tb and return self.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseException:
 |  
 |  __cause__
 |      exception cause
 |  
 |  __context__
 |      exception context
 |  
 |  __dict__
 |  
 |  __suppress_context__
 |  
 |  __traceback__
 |  
 |  args


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
