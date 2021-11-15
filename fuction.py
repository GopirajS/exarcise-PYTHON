Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fuction():
	print('hellow world')

	
>>> fuction()
hellow world
>>> 
>>> 
>>> def fuction(n):
	print('hellow world',name)

	
>>> fuction('gopi')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fuction('gopi')
  File "<pyshell#7>", line 2, in fuction
    print('hellow world',name)
NameError: name 'name' is not defined
>>> def fuction(n):
	print('hellow world',n)

	
>>> 
>>> fuction('gopi')
hellow world gopi
>>> fuction(n='gopi')
hellow world gopi

>>> 

>>> def fuction(*n):
	i=0
	print('hellow ',end='')
	while len(n)>i:
		print(n[i],end=' ')

		


>>> def fuction(*n):
	i=0
	print('hellow ',end='')
	while len(n)>i:
		print(n[i],end=' ')
		i+=1

		
>>> fuction('gopi','raj','sathish','kumar')
hellow gopi raj sathish kumar 

>>> def fuc(first,second):
	print('hellow',first,second)

	

>>> fuc(first='gopi',second='raj')
hellow gopi raj

>>> def fuct(**person):
	print('hellow',person[first],person[second])

	
>>> fuct(first='gopi',second='raj')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    fuct(first='gopi',second='raj')
  File "<pyshell#44>", line 2, in fuct
    print('hellow',person[first],person[second])
NameError: name 'first' is not defined

>>> def fuct(**person):
	print('hellow',person['first'],person['second'])

	
>>> fuct(first='gopi',second='raj')
hellow gopi raj


>>> def my_name(n):
	s='hellow ',n
	return s

>>> my_name('gopiraj')
('hellow ', 'gopiraj')

>>> def my_name(n):
	s='hellow ',n
	return s

>>> my_name('gopiraj')
('hellow ', 'gopiraj')
>>> 
>>> def my_name(n):
	return 'hellow'+ n

>>> my_name('gopiraj')
'hellowgopiraj'
>>> 
>>> 
>>> 
>>> def my_name(n):
	return 'hellow  '+ n

>>> my_name('gopiraj')
'hellow  gopiraj'
>>> 
>>> 
>>> 
>>> def my(d):
	if (d>0):
		result=d+my(k-1)
	else:
		result=0
	return result

>>> def my(d):
	if (d>0):
		result=d+my(d-1)
	else:
		result=0
	return result

>>> my(6)
21
>>> 



#======================================================================================

>>> #   simple python fuction

>>> def simple():
	print('hellow world')

	

>>> simple()
hellow world

>>> def fuc():
	print('welcome in python')

	
>>> fuc()
welcome in python



>>> def fuc():
	return 'gopi raj'


>>> fuc()
'gopi raj'

>>> s=fuc()

>>> s
'gopi raj'

>>> type(s)
<class 'str'>


>>> def fuction(x):
	if x%2==0:
		print('Even',x)
	else:
		print('Odd',x)

		

>>> fuction(3)
Odd 3

>>> fuction(4)
Even 4

>>> fuction(7)
Odd 7




>>> def fuction(name,clg="MCAS"):
	print('welcome ',name,'in ',clg)

	

>>> fuction('gopi')
welcome  gopi in  MCAS

>>> s=fuction

>>> s('Sathish','PSG')
welcome  Sathish in  PSG


>>> #  keyworld argument

>>> def fuction(firstname,lastname):
	print(firstname,lastname)

	
>>> fuction('Gopi','Raj')
Gopi Raj


>>> fuction('Sathish','Kumar')
Sathish Kumar

>>> #  non keyword argument


>>> def fuction(*args):
	for i in args:
		print(i,end=' ')

		

>>> fuction('Gopi','Sathish','Raj','Kumar')
Gopi Sathish Raj Kumar 

>>> def fuction(*args):
	for i in args:
		print(i)

		
>>> fuction('Gopi','Sathish','Raj','Kumar')
Gopi
Sathish
Raj
Kumar


>>> l=['Gopi','Sathish','Raj','Kumar']

>>> fuction(l)
['Gopi', 'Sathish', 'Raj', 'Kumar']


>>> def fuction(**kwargs):
	for key,value in kwargs.items():
		print(key,'==',value)

		
>>> fuction(name='Gopi Raj',age='21',sex='Male',city='Salem',email='gopiraj19599@gmail.com')
name == Gopi Raj
age == 21
sex == Male
city == Salem
email == gopiraj19599@gmail.com


>>> def fuction(**kwargs):
	for key,value in kwargs.items():
		print('%s = %s '%(key,value))

		

>>> fuction(name='Gopi Raj',age='21',sex='Male',city='Salem',email='gopiraj19599@gmail.com')
name = Gopi Raj 
age = 21 
sex = Male 
city = Salem 
email = gopiraj19599@gmail.com 


>>> #   Docstring

>>> def fuction(name):
	""" this is document of string of the fuction """
	print('hellow ',name)

	
>>> fuction('Gopi')
hellow  Gopi


>>> fuction.__doc__
' this is document of string of the fuction '


>>> def fuction(num):
	""" this fuction return the square value of the entered number"""
	return num**2

>>> fuction(5)
25

>>> fuction(10)
100

>>> fuction.__doc__
' this fuction return the square value of the entered number'

>>> fuction.__doc__
' this fuction return the square value of the entered number'


>>> def cube(x):
	return x*x*x


>>> cube(23)
12167


>>> lambda x:x*x*x
<function <lambda> at 0x000001ACE5381160>

>>> (lambda x:x*x*x)(2)
8

>>> (lambda x:x*x*x)(23)
12167


>>>       # nested fuction
      

>>> def f1():
	s=' I Love Python'
	def f2():
		print(s)
	f2()

	
>>> f1()
 I Love Python

>>> #===============================================================

>>> #   *args   and **kwargs


>>> def fuction(*args):
	for i in args:
		print(i)

		
>>> fuction('Gopi','Parimal','Kumar','Sathish')
Gopi
Parimal
Kumar
Sathish


>>> def myfuc(arg,*args):
	print('First argument:',arg)
	for i in args:
		print('Next argument through *args :',i)

		

>>> myfuc('Gopi','Sathish','kumar','raj')
First argument: Gopi
Next argument through *args : Sathish
Next argument through *args : kumar
Next argument through *args : raj

>>> #   keyword arguments


>>> def fuction(**kwargs):
	for key,value in kwargs:
		print(key,'=',value)

		

>>> def fuction(**kwargs):
	for key,value in kwargs.items():
		print(key,'=',value)

		

>>> fuction(name='Gopi',age=21,city='Salem',education='B.Sc Math')
name = Gopi
age = 21
city = Salem
education = B.Sc Math

>>> #--------------------------------------------------------

>>> def myfuc(arg1,arg2,arg3):
	print('arg1 :',arg1)
	print('arg2 :',arg2)
	print('arg3 :',arg3)

	


>>> myfuc('Gopi','raj','kuamr')
arg1 : Gopi
arg2 : raj
arg3 : kuamr

>>> l=('Gopi','raj','kuamr')

>>> myfuc(*l)
arg1 : Gopi
arg2 : raj
arg3 : kuamr

>>> l=('Gopi','raj','kuamr','sathish')


>>> def fuc(*s):
	for i in s:
		print(i)

		
>>> l=[1,2,3,34,4,5]


>>> fuc('Gopi','raj')
Gopi
raj

>>> l=('Gopi','raj','kuamr','sathish')


>>> fuc(l)
('Gopi', 'raj', 'kuamr', 'sathish')
>>> fuc(*l)
Gopi
raj
kuamr
sathish


>>> def myfuc(arg1,arg2,arg3):
	print('arg1 :',arg1)
	print('arg2 :',arg2)
	print('arg3 :',arg3)

	



>>> d={'arg1':'gopi','arg2':'raj','arg3':'kumar'}

>>> myfuc(**d)
arg1 : gopi
arg2 : raj
arg3 : kumar

>>> myfuc(*d)
arg1 : arg1
arg2 : arg2
arg3 : arg3

>>> d={'name':'gopi','age':'21','city':'salem'}


>>> myfuc(**d)
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    myfuc(**d)
TypeError: myfuc() got an unexpected keyword argument 'name'

>>> myfuc(*d)
arg1 : name
arg2 : age
arg3 : city


>>> d={'name':'gopi','age':'21','city':'salem','sex':'male'}

>>> myfuc(*d)
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    myfuc(*d)
TypeError: myfuc() takes 3 positional arguments but 4 were given





>>> def myfuc(*args,**kwargs):
	print('* args ')
	for i in args:
		print(i)
	for key ,value in kwargs.items():
		print(key,'=',value)

		

>>> myfuc('Gopi','Satish','Kumar',name='aaaa',age=21,city='salem')
* args 
Gopi
Satish
Kumar
name = aaaa
age = 21
city = salem

>>> def myfuc(*args,**kwargs):
	print('* args ')
	for i in args:
		print(i)

	print( "** kwargs ")	
	for key ,value in kwargs.items():
		print(key,'=',value)

		

>>> myfuc('Gopi','Satish','Kumar',name='aaaa',age=21,city='salem')
* args 
Gopi
Satish
Kumar
** kwargs 
name = aaaa
age = 21
city = salem

>>> #==========================================================

>>> #   When to use yierd instead of return in python ?

>>> def myfuc():
	yield 1
	yield 2
	yield 3

	

>>> myfuc()
<generator object myfuc at 0x000001E2D9921970>

>>> for i in myfuc():
	i

	
1
2
3


>>> def squar():
	count=0
	while True:
		yield cou/nt*count
		count+=1

		


>>> def squar():
	count=0
	while True:
		yield count*count
		count+=1

		
>>> for i in squar():
	if i >100:
		break
	else:
		print(i)

		
0
1
4
9
16
25
36
49
64
81
100

>>> for i in squar():
	if i >500:
		break
	else:
		print(i)

		
0
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400
441
484

>>> #----------------------------------------------------------------------------

>>> #                              lambda




>>> (lambda :'hellow world')()
'hellow world'

>>> s='gopiraj'

>>> print(lambda s:s)
<function <lambda> at 0x000001E2D9909EE0>


>>> (lambda s: s)(s)
'gopiraj'

>>> (lambda s: print('hellow',s))(s)
hellow gopiraj

>>> (lambda s: print('hellow'))(s)
hellow


>>> def cub(x):
	return x*x*x

>>> cub(4)
64

>>> (lambda x:x*x*x)(4)
64

>>> d=lambda x:x*x*x

>>> d(5)
125

>>> cub(5)
125

>>> def fuctio(x):
	def mul(y):
		return x*y

	
>>> s=fuctio(4)


>>> def fuctio(x):
	lambda y:y*x

	
>>> s=fuctio(4)


>>> def fuctio(x):
	return lambda y:y*x

>>> s=fuctio(4)

>>> fuctio(4)
<function fuctio.<locals>.<lambda> at 0x000001E2D9918820>

>>> fuctio(4)(4)
16

>>> def power(x):
	return lambda a:a**x

>>> s=power(3)


>>> s(4)
64

>>> s(5)
125

>>> s(7)  #7**3
343

>>> s(5)  #5**3
125

>>> s(8)  #8**3
512

>>> a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]




>>> s=filter(None,a)



>>> s=filter(lambda x:x%2==0,a)

>>> s
<filter object at 0x000001E2D990E0D0>

>>> for i in s:
	i

	
100
2
8
60
4
10

>>> filter(None,a)
<filter object at 0x000001E2D990E130>


>>> d=filter(None,a)

>>> for i in d:
	i

	
100
2
8
60
5
4
3
31
10
11

>>> s=filter(lambda x:x>=50,a)

>>> for i in s:
	i

	
100
60

>>> s=filter(lambda x:x>=10,a)


>>> for i in s:
	i

	
100
60
31
10
11



>>> map(lambda x:x%2==0,a)
<map object at 0x000001E2D990E970>

>>> for i in map(lambda x:x%2==0,a):
	i

	
True
True
True
True
False
True
False
False
True
False

>>> map(lambda x:x+0.00,a)
<map object at 0x000001E2D990E8E0>


>>> for i in map(lambda x:x+0.00,a):
	i

	
100.0
2.0
8.0
60.0
5.0
4.0
3.0
31.0
10.0
11.0

>>>#==============================================================================


>>> #   global and Local variables in python

>>> def fuc():
	s='local variable'
	print(s)

	

>>> fuc()
local variable


>>> #  creat global scope variable

>>> s='This is Global scope Variable'

>>> def fuc():
	print('inner fuction :',s)

	
>>> fuc()
inner fuction : This is Global scope Variable


>>> print('This is outer fuction:',s)
This is outer fuction: This is Global scope Variable


>>> def fuction():
	s='Gopiraj'
	print('Hellow',s)

	


>>> fuction()
Hellow Gopiraj


>>> s
'This is Global scope Variable'


>>> def f():
    s += 'GFG'
    print("Inside Function", s)

    


>>> def f():
    s += 'GFG'
    print("Inside Function", s)

    

>>> s='I Love GeekforGeeks'



>>> def f():
    global s
    s += ' GFG'
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)

    

>>> s = "Python is great!"


>>> f()
Python is great! GFG
Look for Geeksforgeeks Python Section


>>> def f():
    global s
    print(s)
    s += ' GFG'
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)

    

>>> s = "Python is great!"


>>> f()
Python is great!
Python is great! GFG
Look for Geeksforgeeks Python Section


>>> def f():
    global s
    print(s)
    s += ' GFG'
    print(s)
    s += "Look for Geeksforgeeks Python Section"
    print(s)

    
>>> f()
Look for Geeksforgeeks Python Section
Look for Geeksforgeeks Python Section GFG
Look for Geeksforgeeks Python Section GFGLook for Geeksforgeeks Python Section



>>> s='gopi'

>>> s+='Raj'

>>> s
'gopiRaj'


>>> name='Gopi'


>>> def f():
	print(name)

	
>>> f()
Gopi


>>> def f():
	name+='Raj'
	print(name)

	
>>> name
'Gopi'



>>> def f():
	global name
	name+='Raj'
	print(name)

	

>>> name
'Gopi'

>>> f()
GopiRaj

>>> def f():
	print(name)
	name+='Raj'
	print(name)

	>>> def f():
	print(name)

	
>>> f()
GopiRaj

>>> A=1

>>> def f():
	print('A')

>>> def g():
	A=2
	print(A)

	
>>> def f():
	global A
	A=4
	print(A)

	

>>> print(A)
1


>>> f()
4

>>> g()
2

>>> def h():
	print(A)

	
>>> h()
4

>>> #================================================================

>>> #                      Global keyword in python


>>> a=12345

>>> def fuc():
	print(a)

	
>>> fuc()
12345

>>> class myclass():
	print(a)

	
12345

>>> class myclass():
	def myfuc(self):
		print(a)

		
>>> s=myclass()

>>> s.myfuc()
12345

>>> a=1234

>>> def fuc():
	print(a)
	s=a+4
	print(s)

	
>>> fuc()
1234
1238


>>> a=1234

>>> def fuc():
	print(a)
	a=a+3
	print(s)

	
>>> fuc()
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    fuc()
  File "<pyshell#183>", line 2, in fuc
    print(a)
UnboundLocalError: local variable 'a' referenced before assignment



>>> def fuc():
	global  a
	print(a)
	a=a+3
	print(a)

	
>>> a
1237

>>> fuc()
1237
1240

>>> a
1240

>>> #-------------------------------------------------




>>> def add():
     x = 15
       
     def change():
         global x
         x = 20
     print("Before making changing: ", x)
     print("Making change")
     change()
     print("After making change: ", x)

     
>>> add()
Before making changing:  15
Making change
After making change:  15


>>> def add():
     x = 15

     def change():
         global x
         x = 20
         print('change():',x)
     print("Before making changing: ", x)
     print("Making change")
     change()
     print("After making change: ", x)

     
>>> add()
Before making changing:  15
Making change
change(): 20
After making change:  15


>>> x
20

>>> #------------------------------------------------

>>> def change(x):
	return x.upper()



>>> change('Gopi')
'GOPI'

>>> up=change

>>> up('Sathish kumar')
'SATHISH KUMAR'


>>> def upper(text):
	return text.upper()

>>> def lower(text):
	return text.lower()


>>> def greet(func):
    greeting = func("""Hi, I am created by a function
                    passed as an argument.""")

    

>>> greet(upper)

>>> def greet(func):
    greeting = func("""Hi, I am created by a function
                    passed as an argument.""")
    print(greeting)

    


>>> greet(upper)
HI, I AM CREATED BY A FUNCTION
                    PASSED AS AN ARGUMENT.


>>> greet(lower)
hi, i am created by a function
                    passed as an argument.

>>> #-------------------------------------------

>>> def create(x):
	def add(x):
		return x+y
	return add

>>> s=create(5)


>>> def create(x):
	def add(y):
		return x+y
	return add


>>> s=create(5)

>>> s(5)
10

>>> create(4)(5)
9


