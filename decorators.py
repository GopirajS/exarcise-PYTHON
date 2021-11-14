>>>#=========================================================

>>> # properties

>>> class student:
	def __init__(self,name,grad):
		self.name=name
		self.grad=grad
		self.msg=self.name +'got grad'+self.grad

		

>>> s=student('Gopiraj','B')

>>> s.name
'Gopiraj'

>>> s.grad
'B'

>>> s.msg
'Gopirajgot gradB'

>>> class student:
	def __init__(self,name,grad):
		self.name=name
		self.grad=grad
		self.msg=self.name +' got grad '+ self.grad

		
>>> s=student('Gopiraj','B')

>>> s.msg
'Gopiraj got grad B'

>>> print(s.msg)
Gopiraj got grad B

>>> s.grad='A'

>>> s.msg

'Gopiraj got grad B'

>>> s.name
'Gopiraj'

>>> s.grad
'A'

>>> s.msg
'Gopiraj got grad B'

>>> #------------------------------

>>> class student:
	def __init__(self,name,grad):
		self.name=name
		self.grad=grad
	def msg(self):
		return self.name +' got grade '+ self.grade

	

>>> s=student('Gopiraj','B')

>>> s.name
'Gopiraj'

>>> s.grad
'B'

>>> s.msg()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.msg()
  File "<pyshell#30>", line 6, in msg
    return self.name +' got grade '+ self.grade
AttributeError: 'student' object has no attribute 'grade'
>>> class student:
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	def msg(self):
		return self.name +' got grade '+ self.grade

	

>>> s=student('Gopiraj','B')

>>> s.name
'Gopiraj'

>>> s.grade
'B'

>>> s.msg
<bound method student.msg of <__main__.student object at 0x0000019081DBBDF0>>

>>> s.msg()
'Gopiraj got grade B'


>>> s.grade="A"


>>> s.name
'Gopiraj'

>>> s.grade
'A'

>>> s.msg()
'Gopiraj got grade A'

>>> s.msg='Gopiraj got grade C'

>>> s.msg()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s.msg()
TypeError: 'str' object is not callable

>>> #------------------------


>>> class student:
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	def msg(self):
		return self.name +' got grade '+ self.grade
	def setter(self,msg):
		send=msg.split(' ')
		self.name=[0]
		self.grade=[-1]

		


>>> s=student('gopi','D')

>>> s.msg()
'gopi got grade D'

>>> s.name
'gopi'

>>> s.grade
'D'

>>> s.setter('Gopiraj got grade A')

>>> s.msg()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s.msg()
  File "<pyshell#64>", line 6, in msg
    return self.name +' got grade '+ self.grade
TypeError: can only concatenate list (not "str") to list


>>> s='gopi got grade A'

>>> s.split()
['gopi', 'got', 'grade', 'A']

>>> s.split(' ')
['gopi', 'got', 'grade', 'A']


>>> send=s.split(' ')

>>> send[0]
'gopi'

>>> send[-1]
'A'

>>> class student:
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	def msg(self):
		return self.name +' got grade '+ self.grade
	def setter(self,msg):
		send=msg.split(' ')
		self.name=send[0]
		self.grade=send[-1]

		

>>> s=student('Gopi','A')

>>> s.name
'Gopi'

>>> s.grade
'A'

>>> s.msg()
'Gopi got grade A'

>>> s.setter('Gopiraj got grade D')

>>> s.msg()
'Gopiraj got grade D'

>>> s.setter('Sathish got Grade A')


>>> s.msg()
'Sathish got grade A'


>>> class student:
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	@property	
	def msg(self):
		return self.name +' got grade '+ self.grade
	@msg.setter
	def msg(self,msg):
		send=msg.split(' ')
		self.name=send[0]
		self.grade=send[-1]

		

>>> s=student('Gopi','G')


>>> s.msg()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    s.msg()
TypeError: 'str' object is not callable

>>> s.msg
'Gopi got grade G'

>>> s.msg='Sathish got grade A'

>>> s.msg
'Sathish got grade A'

>>> s.msg
'Sathish got grade A'

>>> s.name
'Sathish'

>>> s.grade
'A'

>>> #-------------------------------------------------


>>> class student():
	def __init__(self,mark):
		self.mark=mark
	def per(self):
		return (self.mark/500)*100

	

>>> s=student(400)

>>> s.mark
400

>>> s.per
<bound method student.per of <__main__.student object at 0x0000019081DBB430>>

>>> s.per()
80.0
>>> print(s.per,'%')
<bound method student.per of <__main__.student object at 0x0000019081DBB430>> %

>>> print(s.per(),'%')
80.0 %

>>> s.mark=350

>>> s.per()
70.0

>>> s.mark=450

>>> s.per()
90.0

>>> s.mark=340

>>> s.per()
68.0


>>> class student():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100

	

>>> s=student(328)

>>> s.per()
65.60000000000001


>>> class student():
	def __init__(self,mark):
		self.mark=mark
	def per(self):
		return (self.mark/500)*100
	def setter(self,value):
		self.__mark=value

		

>>> s=student(345)

>>> s.mark
345

>>> class student():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100
	def setter(self,value):
		self.__mark=value

		
>>> s=student(345)

>>> s.per()
69.0

>>> s.setter(432)

>>> s.per()
86.4


>>> class student():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100,self.__mark
	def setter(self,value):
		self.__mark=value

		

>>> s=student(345)


>>> s.per()
(69.0, 345)

>>> s=student(123)

>>> s.per()
(24.6, 123)

>>> s.setter(234)

>>> s.per()
(46.800000000000004, 234)


>>> class student():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100,self.__mark
	def setter(self,value):
		self.__mark=value
	def getter(self):
		return self.__mark

	
>>> s=student(234)

>>> s.per()
(46.800000000000004, 234)

>>> s.getter()
234

>>> s.setter(456)

>>> s.getter()
456

>>> s.per()
(91.2, 456)


>>> class student():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100,self.__mark
	@property
	def mark(self):
		return self.__mark
	@mark.setter
	def setter(self,value):
		self.__mark=value

		
>>> s=student(234)

>>> class student():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100,self.__mark
	@property
	def mark(self):
		return self.__mark
	@mark.setter
	def mark(self,value):
		self.__mark=value

		
>>> s=student(234)

>>> s.mark=456

>>> s.per()
(91.2, 456)

>>> s.mark
456

>>> s.mark=345

>>> s.per()
(69.0, 345)


		
>>> s=student(244)


>>> class student():
	def __init__(self,mark):
		self.__mark=mark
	def per(self):
		return (self.__mark/500)*100,self.__mark
	@property
	def mark(self):
		return self.__mark
	@mark.setter
	def mark(self,value):
		self.__mark=value

		
>>> s=student(234)

>>> s.per()
(46.800000000000004, 234)

>>> s.mark
234

>>> s.mark=567

>>> s.mark
567

>>> s.per()
(113.39999999999999, 567)

>>> #===============================================


>>> class student(object):
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
		self.msg=self.name +' got grade '+self.grade

		

>>> s=student('Gopi','A')

>>> s.name
'Gopi'

>>> s.grade
'A'

>>> s.msg
'Gopi got grade A'

>>> s=student('Gopi','b')

>>> s.name
'Gopi'

>>> s.grade
'b'

>>> s.msg
'Gopi got grade b'

>>> s=student('Sathish ','A')

>>> s.msg
'Sathish  got grade A'

>>> s.grade='B'

>>> s.msg
'Sathish  got grade A'


>>> s.name='Raj'

>>> s.msg
'Sathish  got grade A'

>>> class student(object):
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade

		


>>> class student(object):
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	def msg(self):
		return self.name +' got grade '+self.grade

	
>>> s=student('Gopi',"S")

>>> s.msg()
'Gopi got grade S'

>>> s.name
'Gopi'

>>> s.grade
'S'

>>> s.msg
<bound method student.msg of <__main__.student object at 0x0000019081DF0490>>

>>> s.msg()
'Gopi got grade S'

>>> s.name='Sathish'

>>> s.msg()
'Sathish got grade S'

>>> s.grade="A"

>>> s.msg()
'Sathish got grade A'

>>> class student(object):
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	@property	
	def msg(self):
		return self.name +' got grade '+self.grade

	

>>> s=student('Gopi',"S")

>>> s.msg
'Gopi got grade S'

>>> type(s)
<class '__main__.student'>

>>> type(s.grade)
<class 'str'>

>>> type(s.name)
<class 'str'>


>>> s.msg
'Gopi got grade S'

>>> s.msg='Sathish got grade A'
Traceback (most recent call last):
  File "<pyshell#287>", line 1, in <module>
    s.msg='Sathish got grade A'
AttributeError: can't set attribute


>>> s.msg
'Gopi got grade S'

>>> class student(object):
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	@property
	def msg(self):
		return self.name +' got grade '+self.grade
	@msg.setter
	def msg(self,value):
		send=value.split(' ')
		self.name=send[0]
		self.grade=send[-1]

		
>>> s=student('Gopiraj','B')

>>> s.name
'Gopiraj'

>>> s.grade
'B'

>>> s.msg
'Gopiraj got grade B'

>>> s.msg='Sathishkumar got grade A'

>>> s.name
'Sathishkumar'

>>> s.grade
'A'

>>> s.msg
'Sathishkumar got grade A'


>>> del s.msg
Traceback (most recent call last):
  File "<pyshell#307>", line 1, in <module>
    del s.msg
AttributeError: can't delete attribute


>>> class student(object):
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	@property
	def msg(self):
		return self.name +' got grade '+self.grade
	@msg.setter
	def msg(self,value):
		send=value.split(' ')
		self.name=send[0]
		self.grade=send[-1]
	@msg.delete
	def msg(self):
		self.name=None
		self.grade=None

		
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    class student(object):
  File "<pyshell#316>", line 13, in student
    @msg.delete
AttributeError: 'property' object has no attribute 'delete'

>>> class student(object):
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	@property
	def msg(self):
		return self.name +' got grade '+self.grade
	@msg.setter
	def msg(self,value):
		send=value.split(' ')
		self.name=send[0]
		self.grade=send[-1]
	@msg.deleter
	def msg(self):
		self.name=None
		self.grade=None

		
>>> s=student('Gopi','F')

>>> s.name
'Gopi'

>>> s.grade
'F'
>>> s.msg
'Gopi got grade F'

>>> s.name='Sathish kumar'

>>> s.name
'Sathish kumar'

>>> s.msg
'Sathish kumar got grade F'

>>> s.grade='A'

>>> s.msg
'Sathish kumar got grade A'

>>> s.msg
'Sathish kumar got grade A'

>>> s.msg='Gopiraj got grade G'

>>> s.name
'Gopiraj'

>>> s.grade
'G'

>>> s.msg
'Gopiraj got grade G'

>>> del s.msg

>>> s.msg
Traceback (most recent call last):
  File "<pyshell#335>", line 1, in <module>
    s.msg
  File "<pyshell#318>", line 7, in msg
    return self.name +' got grade '+self.grade
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'


>>>#------------------------------------------------------------------------------------------


>>> #                           @property        Decorator


>>> class student(object):
	def __init__(self,name):
		self.__name=name

	

>>> s=student('Gopi')


>>> class student(object):
	def __init__(self,name):
		self.__name=name
	def name(self):
		return self.__name

	
>>> s=student('Gopi')

>>> s.name
<bound method student.name of <__main__.student object at 0x000001FEAF08C280>>

>>> s.name()
'Gopi'

>>> print(s.name())
Gopi

>>> class student(object):
	def __init__(self,name):
		self.__name=name
	@property	
	def name(self):
		return self.__name

	

>>> s=student('Gopi')

>>> s.name

'Gopi'

>>> print(s.name)
Gopi

>>> s.name='Sathish'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.name='Sathish'
AttributeError: can't set attribute


>>> class student(object):
	def __init__(self,name):
		self.__name=name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,value):
		self.__name=value

		

>>> s=student('Gopi')

>>> s.name
'Gopi'

>>> s.name='Sathish kumar'

>>> s.name
'Sathish kumar'


>>> class student(object):
	def __init__(self,name):
		self.__name=name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,value):
		self.__name=value
	def name(self):
		print('Deleting...')
		del self.__name

		
>>> s=student('Gopi')

>>> s.name()
Deleting...

>>> s.name
<bound method student.name of <__main__.student object at 0x000001FEAF12B970>>

>>> s.name()
Deleting...
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.name()
  File "<pyshell#42>", line 12, in name
    del self.__name
AttributeError: _student__name

>>> class student(object):
	def __init__(self,name):
		self.__name=name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,value):
		self.__name=value
	@name.deleter	
	def name(self):
		print('Deleting...')
		del self.__name

		
>>> s=student('Gopi')

>>> s.name
'Gopi'

>>> s.name='SAthish kuamr'


>>> s.name
'SAthish kuamr'
>>> del s.name
Deleting...

		
		
		

>>>#========================================================================
