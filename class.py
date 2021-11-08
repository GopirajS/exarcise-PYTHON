Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # class
>>> 
>>> class mydata(object):
	name='gopiraj'
	age=21
	def fun(self):
		print('hellow ,mr.',self.name)
		print('and his age is :',self.age)

		
>>> s=mydata()
>>> print(s.name)
gopiraj
>>> s.age
21
>>> s.fun()
hellow ,mr. gopiraj
and his age is : 21
>>> 
>>> 
>>> class person:
	def __init__(self,name):
		self.name=name
	def fun(self):
		print('hellow,',self.name)

		
>>> s=person('gopi')
>>> s.fun()
hellow, gopi
>>> s.name
'gopi'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class dog(object):
	animal='dog'
	def __init__(self,breed,color):
		self.breed=breed
		self.color=color

		
>>> s=dog('germensufferd','brow')
>>> s.animal
'dog'
>>> s.breed
'germensufferd'
>>> s.color
'brow'
>>> 
>>> 
>>> d=dog('street dog','black')
>>> d.animal
'dog'
>>> d.breed
'street dog'
>>> d.color
'black'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class dog:
	def __init__(self,name):
		self.name=name
	def set_color(self,color):
		self.color=color
	def ger_color(self):
		return self.color

	
>>> 
>>> 
>>> s=dog('gymmi')
>>> s.name
'gymmi'
>>> s.set_color('brown')
>>> s.color
'brown'
>>> s.ger_color()
'brown'
>>> 
>>> 
>>> 
>>> 
>>> #================================================================
>>> 
>>> 
>>> #                       constuctor
>>> 
>>> def __init__(name):
	print(name)

	
>>> __init__('gopi')
gopi
>>> 
>>> 
>>> 