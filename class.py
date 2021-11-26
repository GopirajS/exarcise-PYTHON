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


>>> #    class

>>> n=20

>>> type(n)
<class 'int'>

>>> s='Python'

>>> type(s)
<class 'str'>

>>> class student:
	pass

>>> student
<class '__main__.student'>

>>> s=student

>>> s=student()

>>> class student:
	schoolName='Gugai Her Secondery School'

	
>>> s=student()

>>> s.schoolName
'Gugai Her Secondery School'

>>> student.schoolName
'Gugai Her Secondery School'

>>> student.schoolName='Goverment Hr Sec School'

>>> s.schoolName
'Goverment Hr Sec School'
>>> s=student()

>>> s.schoolName='Muthayammal Collage of Arts & Science'

>>> student.schoolName
'Goverment Hr Sec School'

>>> s.schoolName
'Muthayammal Collage of Arts & Science'

>>> del student.schoolName

>>> student.schoolName
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    student.schoolName
AttributeError: type object 'student' has no attribute 'schoolName'



>>> class student:
	count=0
	def __init__(self):
		student.count+=1

		
>>> s=student()

>>> s.count
1

>>> d=student()

>>> d.count
2

>>> f=student()

>>> f.count
3

>>> s.count
3

#-------------------------------------------------------------
>>> #          constructor



>>> class student(object):
	count=0
	def __init__(self):
		student.count+=1

		
>>> s=student()

>>> s
<__main__.student object at 0x000002C4B7BB92E0>

>>> s.count
1

>>> d=student()

>>> d.count
2



>>> class myclass(object):
	def __init__(self):
		print('constructor invoked')

		
>>> obj=myclass()
constructor invoked

>>> obj2=myclass()
constructor invoked


>>> class student(object):
	schoolName='Gugai Hr Sec School'
	def __init__(self):
		name=''
		age=0

		
>>> s=student()

>>> s.schoolName
'Gugai Hr Sec School'

>>> class student(object):
	schoolName='Gugai Hr Sec School'
	def __init__(self):
		self.name=''
		self.age=0

		
>>> s=student

>>> s=student()

>>> s.age
0

>>> s.name
''

>>> s.schoolName
'Gugai Hr Sec School'

>>> s.age=21

>>> s.name='gopi'

>>> s.schoolName
'Gugai Hr Sec School'

>>> s.age
21

>>> s.name
'gopi'

>>> s.schoolName='MCAS'

>>> s.schoolName
'MCAS'

>>> student.schoolName

'Gugai Hr Sec School'

>>> class student(object):
	schoolName='Gugai Hr Sec School'
	def __init__(self):
		self.name=''
		self.age=0

		
>>> s=student()


>>> s.name
''
>>> s.schoolName
'Gugai Hr Sec School'

>>> s.schoolName='MCAS'

>>> s.schoolName
'MCAS'

>>> s=student()

>>> s.schoolName
'Gugai Hr Sec School'

>>> class student(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

		

>>> s=student('Gopi Raj','21')

>>> s.name
'Gopi Raj'

>>> s.age
'21'

>>> s.name='Sathish kumar'

>>> s.name
'Sathish kumar'

>>> s.age
'21'

>>> s.age='27'


>>> s.name
'Sathish kumar'

>>> s.age

'27'



>>> s=student('gopal','21')

>>> s.name

'gopal'

>>> s.age
'21'

>>> s.age=20

>>> s.name
'gopal'




>>> class myclass(object):
	def __init__(self,name='gopi',age=21):
		self.name=name
		self.vayathu=age

		
>>> s=myclass()

>>> s.vayathu

21

>>> s.name
'gopi'

>>> class myclass(object):
	def __init__(self,name='gopi',age=21):
		self.name=name
		self.age=age

		
>>> s=myclass(age=30)

>>> s.name
'gopi'


>>> s.age
30

>>> class student(object):
	def __init__(self):
		self.__name=''
	def setname(self):
		print("setname() , calling")
		self.__name=name
	def getname(self):
		print('getname() ,calling')
		return self.__name
	name=property(getname,setname)

	
>>> s=student()

>>> s.name
getname() ,calling
''
>>> s.setname
<bound method student.setname of <__main__.student object at 0x000002A1615EC280>>

>>> s.setname()

setname() , calling
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.setname()
  File "<pyshell#28>", line 6, in setname
    self.__name=name
NameError: name 'name' is not defined

>>> s=student()

>>> s.name='gopiraj'
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.name='gopiraj'
TypeError: setname() takes 1 positional argument but 2 were given

>>> class Student:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    name=property(getname, setname)

    
>>> s=student()

>>> s.name
getname() ,calling
''
>>> s.name='gopi'
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.name='gopi'
TypeError: setname() takes 1 positional argument but 2 were given

>>> #----------------------------------------------

>>> #   class method

>>> class myclass(object):
	def display(self):
		print('display the student info')

		
>>> s=myclass()

>>> s.display()
display the student info

>>> s.display
<bound method myclass.display of <__main__.myclass object at 0x000002A16169ED60>>

>>> s.display()
display the student info


>>> class demo():
	def display(self):
		print('hellow world')

		
>>> s=demo()

>>> s.display()
hellow world
>>> class demo():
	def display(s):
		print('hellow world')

		


>>> s.display
<bound method demo.display of <__main__.demo object at 0x000002A16168B310>>

>>> s.display()

hellow world

>>> d=demo()

>>> d.display()
hellow world


>>> class demo():
	def display():
		print('hellow world')

		
>>> a=demo()

>>> a.display()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.display()
TypeError: display() takes 0 positional arguments but 1 was given

>>> #   example class method

>>> class mycls(object):
	def __init__(self,name,age):
		self.namr=name
		self.age=age
	def display(self):
		print(self.name,'',self.age)

		

>>> s=mycls('Gopiraj',21)

>>> s.age
21

>>> s.namr
'Gopiraj'

>>> class mycls(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print(self.name,'',self.age)



>>> s=mycls('Gopiraj','21')

>>> s.display
<bound method mycls.display of <__main__.mycls object at 0x000002A16168B310>>

>>> s.display()
Gopiraj  21

>>> s.name
'Gopiraj'

>>> s.age
'21'

>>> s=mycls('Gopiraj',21)


>>> s.age
21


>>> #---------------------------------------------------------

>>> #    delete  attribute, object, class

>>> class mycls(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print(self.name,'',self.age)

		



>>> obj=mycls('Gopiraj',21)

>>> obj.age
21

>>> obj.display()
Gopiraj  21

>>> obj.name
'Gopiraj'



>>> del obj.age

>>> obj.name
'Gopiraj'

>>> obj.display()
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    obj.display()
  File "<pyshell#137>", line 6, in display
    print(self.name,'',self.age)
AttributeError: 'mycls' object has no attribute 'age'


>>> del obj

>>> obj
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    obj
NameError: name 'obj' is not defined

>>> del mycls


>>> mycls
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    mycls
NameError: name 'mycls' is not defined


	
>>>#==========================================================================




>>> class my_class():
	def __init__(self,name):
		self.name=name
	def msg(self):
		return  'Hellow Mr '+ self.name

	
>>> s=my_class('Gpi')

>>> s.name
'Gpi'

>>> s.msg()
'Hellow Mr Gpi'


>>> class dog():
	animal='dog'
	def __init__(self,breed,color):
		self.breed=breed
		self.color=color


>>> gimmy=dog('pug','brown')

>>> gimmy.animal
'dog'

>>> gimmy.breed
'pug'

>>> gimmy.color
'brown'

>>> tommy=dog('bulldog','black')

>>> tommy.color
'black'

>>> tommy.breed
'bulldog'

>>> tommy.animal
'dog'

>>> class greed():
	def __init__(self):
		self.geek='hellow world'
	def print_msg(self):
		print(self.geek)

		
>>> s=greed()

>>> s.geek
'hellow world'

>>> s.print_msg()
hellow world

>>> s.geek='hellow world in python'

>>> s.print_msg()
hellow world in python


>>> class calculate():
	def __init__(self,f,s):
		self.f=f
		self.s=s
	def print__msg(self):
		print('first number:',self.f)
		print('second number',self.s)
		print('answer is :',self.ans)
	def calculate(self):
		self.ans=self.f+self.s

		

>>> s=calculate(2,3)

>>> s.f
2

>>> s.s
3

>>> s.calculate()

>>> s.print__msg()
first number: 2
second number 3
answer is : 5

>>> s.f=1

>>> s.s=2

>>> s.print__msg()
first number: 1
second number 2
answer is : 5

>>> s.calculate()

>>> s.print__msg()
first number: 1
second number 2
answer is : 3

>>> d=calculate(1,2)

>>> d.f
1

>>> d.s
2


>>> class s:
	first=0
	second=0
	def __init__(self,f,s):
		self.first=f
		self.second=s
	def print_msg(self):
		print('first number',self.first)
		print('second number',self.second)

		
>>> s=s(1,2)

>>> s.first
1

>>> s.second
2

>>> s.print_msg()
first number 1
second number 2


>>> class s:
	fir=0
	sec=0
	def __init__(self,f,s):
		self.first=f
		self.second=s
	def print_msg(self):
		print('first number',self.first)
		print('second number',self.second)

		

>>> s=s(1,2)

>>> s.first
1

>>> s.second
2

>>> s.fir
0

>>> s.sec
0

>>> s.print_msg()
first number 1
second number 2

>>> class s:
	first=0
	second=0
	def __init__(self,f,s):
		self.first=f
		self.second=s
	def print_msg(self):
		print('first number',self.first)
		print('second number',self.second)

		

>>> s=s(1,2)


>>> s.print_msg()
first number 1
second number 2

>>> s.second=3

>>> s.print_msg()
first number 1
second number 3

>>> class destro():
	def __init__(self,name):
		self.name=name
		print('Destructor')
	def __del__(self):
		print('dectructor is called..')
		print('deleted reference of obj of class')

		

>>> s=destro('Gopi')
Destructor

>>> s.name
'Gopi'


>>> del s
dectructor is called..
deleted reference of obj of class



>>> del destro


>>> class destro():
	def __init__(self,name):
		self.name=name
		print('Destructor')
	def __del__(self):
		print('dectructor is called..')
		print('deleted reference of obj of class')

		

>>> destro
<class '__main__.destro'>


>>> def creat_obj():
	print('Making object for class')
	obj=destro('Gopi')
	print('function ended..')
	return obj


>>> s=destro('Gopi')
Destructor

>>> s
<__main__.destro object at 0x000001D2D8C040D0>

>>> s=creat_obj()
Making object for class
Destructor
function ended..

>>> s
dectructor is called..
deleted reference of obj of class
<__main__.destro object at 0x000001D2D8C9EC70>

>>> s
<__main__.destro object at 0x000001D2D8C9EC70>

>>> def fuction():
	print('imm from function')

	
>>> s=fuction()
imm from function

>>> s

>>> type(s)
dectructor is called..
deleted reference of obj of class
<class 'NoneType'>

>>> s

>>> type(s)
<class 'NoneType'>

>>> def fuction():
	print('im from fuction')
	s=class_my()
	return s


>>> class class_my():
	def __init__(self):
		print('im from constructor in class')

		
>>> s=class_my()
im from constructor in class

>>> d=fuction()
im from fuction
im from constructor in class

>>> def fuction():
	print('im from fuction')
	s=class_my()
	d='hello world'
	return d

>>> s=class_my()
im from constructor in class

>>> obj=fuction()
im from fuction
im from constructor in class

>>> obj
'hello world'

>>> def fuction():
	print('im from fuction')
	s=class_my()
	return s


>>> s=class_my()
im from constructor in class

>>> obj=fuction()
im from fuction
im from constructor in class

>>> obj
<__main__.class_my object at 0x000001D2D8C9ECA0>

>>> class my_class():
	def __init__(self):
		print('im from constructor in my_class')
	def __del__(self):
		print(' im from destructor in my class')

		

>>> s=my_class()
im from constructor in my_class

>>> s.__del__
<bound method my_class.__del__ of <__main__.my_class object at 0x000001D2D8C9EBB0>>

>>> s.__del__()
 im from destructor in my class

>>> s
<__main__.my_class object at 0x000001D2D8C9EBB0>

>>> d=my_class()
im from constructor in my_class

>>> del d
 im from destructor in my class

>>>#===============================================================


>>> class person():
	def __init__(self,name):
		self.name=name
	def getName(self):
		return self.name
	def isEmployee(self):
		return False


>>> s=person("Gopi")

>>> s.name
'Gopi'

>>> s.isEmployee
<bound method person.isEmployee of <__main__.person object at 0x00000269B52EB310>>

>>> s.isEmployee()
False

>>> s.getName
<bound method person.getName of <__main__.person object at 0x00000269B52EB310>>

>>> s.getName()
'Gopi'

>>> class Employee(person):
	def __init__(self):
		return True

	

>>> class Employee(person):
	def isEmployee(self):
		return True

	
>>> s=Employee('GOpi')

>>> s.isEmployee
<bound method Employee.isEmployee of <__main__.Employee object at 0x00000269B52EB2E0>>

>>> s.isEmployee()
True

>>> s.name
'GOpi'

>>> s.getName
<bound method person.getName of <__main__.Employee object at 0x00000269B52EB2E0>>

>>> s.getName()
'GOpi'


>>> class person(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def print_msg(self):
		print(self.name)
		print(self.age)

		

>>> s=person('Gopi',21)

>>> s.age
21

>>> s.name
'Gopi'

>>> s.print_msg()
Gopi
21

>>> class child(person):
	def __init__(self,name,age,city,education):
		self.city=city
		self.education=education

		

>>> s=child('Gopi',21,'salem','B.Sc Math')

>>> s.city
'salem'

>>> s.education
'B.Sc Math'



>>> class child(person):
	def __init__(self,name,age,city,education):
		self.city=city
		self.education=education
		person.__init__(self,name,age)

		
>>> s=child('Gopi',21,'salem','B.Sc Math')

>>> s.age
21

>>> s.city
'salem'

>>> s.education
'B.Sc Math'

>>> s.city
'salem'

>>> s.print_msg()
Gopi
21


>>> class base1(object):
	def __init__(self):
		self.str1='gopi raj 1'
		print('base 1')

		

>>> class base2(object):
	def __init__(self):
		self.str2='gopi raj 2'
		print('base 2')

		
>>> class parent(base1,base2):
	def __init__(self):
		base1.__init__(self)
		base2.__init__(self)
		print('Derived')
	def print_str(self):
		print(self.str1)
		print(self.str2)

		
>>> s=parent()
base 1
base 2
Derived

>>> s.str1
'gopi raj 1'

>>> s.str2
'gopi raj 2'

>>> s.print_str()
gopi raj 1
gopi raj 2

>>> class parent(base1,base2):
	def __init__(self):
		base1.__init__(self)
		#base2.__init__(self)
		print('Derived')
	def print_str(self):
		print(self.str1)
		print(self.str2)

		


>>> s=parent()
base 1
Derived

>>> s.str1
'gopi raj 1'




>>> #---------------------------------------------


>>> class base(object):
	def __init__(self,name):
		self.name=name
	def get_name(self):
		return self.name

	

>>> class child(base):
	def __init__(self,name,age):
		base.__init__(self,name)
		self.age=age
	def get_age(self):
		return self.age

	

>>> class parent(child):
	def __init__(self,name,age,city):
		parent.__init__(self,name,age)
		self.city=city
	def get_city(self):
		return self.city

	
>>> class parent(child):
	def __init__(self,name,age,city):
		child.__init__(self,name,age)
		self.city=city
	def get_city(self):
		return self.city

	

>>> s=parent('Gopi',21,'salem')

>>> s.age
21

>>> s.city
'salem'

>>> s.get_age()
21

>>> s.get_name()
'Gopi'

>>> s.get_city()
'salem'

>>> s.name
'Gopi'

>>> s.age
21

>>> s.city
'salem'


>>> class A(object):
	def __init__(self):
		self.a=123
		self.__s='Gopi'

	

>>> class B(A):
	def __init__(self):
		self.__g='Sathish Kumar'
		A.__init__(self)

		

>>> a=B()

>>> a.a
123

>>> class base(object):
	def __init__(self,name):
		self.name=name
	def get_name(self):
		return 'Hellow '+self.name

	
>>> s=base('Gopi raj')


>>> s.name
'Gopi raj'

>>> s.get_name()
'Hellow Gopi raj'

>>>#==========================================================

>>> class child(base):
	def __init__(self,name,age):
		self.age=age
		base.__init__(self,name)
	def get_age(self):
		return self.name +'age is '+self.age

	
>>> s=child('Gopi',21)

>>> s.name
'Gopi'

>>> s.age
21


>>> class child(base):
	def __init__(self,name,age):
		self.age=age
		base.__init__(self,name)
	def get_age(self):
		return self.name +'age is '+str(self.age)

	

>>> s=child('Gopi',21)

>>> s.get_age()
'Gopiage is 21'

>>> class child(base):
	def __init__(self,name,age):
		self.age=age
		base.__init__(self,name)
	def get_age(self):
		return self.name +' age is '+str(self.age)

	

>>> s=child('Gopi',21)

>>> s.name
'Gopi'

>>> s.age
21

>>> s.get_age()
'Gopi age is 21'

>>> s.get_name()
'Hellow Gopi'


>>> s=child('Gopi Raj',21)

>>> s.name
'Gopi Raj'

>>> s.age
21

>>> s.get_age()
'Gopi Raj age is 21'

>>> s.get_name()
'Hellow Gopi Raj'

>>> class base(object):
	def __init__(self,name):
		self.name=name
	def get_name(self):
		return 'hellow '+self.name
	def isEmployee(self):
		return False

	
>>> class child(base):
	def isEmployee(self):
		return True

	
>>> s=child('Gopi')

>>> s.name
'Gopi'

>>> s.get_name()
'hellow Gopi'

>>> s.isEmployee()
True

>>> class my_class1(object):
	def fuction1(self):
		print('im from fuction1 in my_class1')

		
>>> class my_class(my_class1):
	def fuction2(self):
		print('im from fuction2 in my_claSS')

		
>>> s=my_class()

>>> s.fuction1
<bound method my_class1.fuction1 of <__main__.my_class object at 0x0000015D3DB2C850>>

>>> s.fuction1()
im from fuction1 in my_class1

>>> s.fuction2()
im from fuction2 in my_claSS


>>> d=my_class1()

>>> d.fuction1()
im from fuction1 in my_class1

>>> # multiple inheritence

>>> def father(object):
	father=''
	def father(self):
		return self.father

	
>>> class father(object):
	father=''
	def father(self):
		return self.father

	
>>> s=father()

>>> s.father
<bound method father.father of <__main__.father object at 0x0000015D3DBCBFD0>>

>>> s.father()
<bound method father.father of <__main__.father object at 0x0000015D3DBCBFD0>>

>>> s.father
<bound method father.father of <__main__.father object at 0x0000015D3DBCBFD0>>

>>> s.father()
<bound method father.father of <__main__.father object at 0x0000015D3DBCBFD0>>

>>> s.father='Shanmugam'



>>> class father(object):
	father=''
	def father_fun(self):
		return self.father

	
>>> s=father()

>>> s.father
''

>>> s.father_fun()
''

>>> class mother:
	mother=''
	def mother(self):
		return self.mother

	
>>> s=mother()

>>> s.mother
<bound method mother.mother of <__main__.mother object at 0x0000015D3DBCBFD0>>

>>> class mother:
	mother=''
	def mother_fun(self):
		return self.mother

	

>>> s=mother()

>>> s.mother
''

>>> s.mother_fun()
''
>>> s.mother='Parimal'

>>> s.mother_fun
<bound method mother.mother_fun of <__main__.mother object at 0x0000015D3DBDEB20>>

>>> s.mother_fun()
'Parimal'

>>> s.mother
'Parimal'

>>> class child(father,mother):
	def parent(self):
		print('father name:',self.father)
		print('mother name:',self.mother)

		

>>> s=child()

>>> s.father
''

>>> s.mother
''

>>> s.father_fun()
''

>>> s.mother_fun()
''
>>> s.parent()
father name: 
mother name: 

>>> s.father='Shanmugam'

>>> s.mother='Parimala'


>>> s.father_fun()
'Shanmugam'

>>> s.mother_fun()
'Parimala'

>>> s.father
'Shanmugam'

>>> #-----------------------------------------


>>> class g_father(object):
	def __init__(self,g_f_name):
		self.g_fathername=g_f_name

		

>>> class father(g_father):
	def __init__(self,f_n,g_f_n):
		self.father_name=f_n
		g_father.__init__(self,g_f_n)

		
>>> s=father('Shanmugam','sudukaru Raja')

>>> s.g_fathername
'sudukaru Raja'

>>> s.father_name
'Shanmugam'


>>> class son(father):
	def __init__(self,son_name,father_name,g_father_name):
		self.son_name=son_name
		father.__init__(self,father_name,g_father_name)

		
>>> s=son('Gopi raj','shanmugam','athanari saami')

>>> s.father_name
'shanmugam'

>>> s.g_fathername
'athanari saami'
>>> s.son_name
'Gopi raj'

>>> #------------------------------------

>>> #  hierarchical inheritance


>>> class parent(object):
	def function1(self):
		print('im from parent fuction 1')

		
>>> class yielder_son(parent):
	def fuction2(self):
		print('im from fuction 2 in yielder_son')

		
>>> class younger_son(parent):
	def fuction3(self):
		print('im from fuction3 in younger son')

		

>>> obj1=yielder_son()

>>> obj1.function1()

im from parent fuction 1

>>> obj1.fuction2()
im from fuction 2 in yielder_son


>>> obj2=younger_son()

>>> obj2.function1()
im from parent fuction 1

>>> obj2.fuction3()
im from fuction3 in younger son


>>>#============================================================




>>> # Encapsulation in python

>>> class base(object):
	def __init__(self):
		self.a='hellow world'
		self._c='this is protected member'

	
>>> class derived(base):
	def __init__(self):
		base.__init__(self)
		print(self._c)

		
>>> s=base()

>>> s.a
'hellow world'

>>> s._c
'this is protected member'

>>> obj=derived()
this is protected member

>>> class Map:
    def __init__(self, iterate):
        self.list = []
        self.__geek(iterate)
    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)

            



>>> class Map:
    def __init__(self, iterate):
        self.list = []
        self.__geek(iterate)
    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)
    __geek = geek

    
>>> class MapSubclass(Map):
     
    # provides new signature for geek() but
    # does not break __init__()
    def geek(self, key, value):       
        for i in zip(keys, value):
            self.list.append(i)

            

>>> l=[1,2,3,4,5,6,7]


>>> s=MapSubclass(l)

>>> s.list
[1, 2, 3, 4, 5, 6, 7]

>>> s.geek
<bound method MapSubclass.geek of <__main__.MapSubclass object at 0x00000120015CC850>>


>>> class base(object):
	def __init__(self):
		self.a='gopiraj'
		self.__c='sathish kumar'

		
>>> class derive(base):
	def __init__(self):
		base.__init__(self)
		print(self.__c)

		
>>> s=base()

>>> s.a
'gopiraj'


>>> class base(object):
	def __init__(self):
		self.a='gopiraj'
		self._c='sathish kumar'

		

>>> class derive(base):
	def __init__(self):
		base.__init__(self)
		print(self.__c)

		

>>> class derive(base):
	def __init__(self):
		base.__init__(self)
		print(self._c)

		

>>> ss=derive()
sathish kumar

>>> ss.a
'gopiraj'

>>> #---------------------------------------

>>> #               polymorphism in python

>>> print(len('geeks'))
5

>>> print(len([1,2,3,4,5,6]))
6

>>> print(len([1,2,3,4,5,6,'gopiraj']))
7

>>> def add(x=0,y=0,z=0):
	return x+y+z


>>> add(1,2,3)
6

>>> add(1,2)
3

>>> add()
0

>>> class india(object):
	def capital(self):
		print('New delhi is capital of india')
	def language(self):
		print('Tamil language is most widely speaking language')
	def type(self):
		print('india is devaloped country')

		
>>> class USA(object):
	def capital(self):
		print('washington D.C is capital of USA')
	def language(self):
		print('English is primery language of USA')
	def type(self):
		print('USA is developed county')

		
>>> obj=india()

>>> obj.capital()
New delhi is capital of india

>>> obj.language()
Tamil language is most widely speaking language

>>> obj.type()
india is devaloped country

>>> obj=india()

>>> obj2=USA()

>>> for i in (obj,obj2):
	i.capital()
	i.language()
	i.type()

	
New delhi is capital of india
Tamil language is most widely speaking language
india is devaloped country
washington D.C is capital of USA
English is primery language of USA
USA is developed county



>>> class bird(object):
	def intro(self):
		print('there are many type of birds.')
	def flight(self):
		print('Most of the bird can be fly but some one canot')

		


>>> class sparrow(bird):
	def flight(self):
		print('sparrow can be fly')

		
>>> class ostrich(bird):
	def flight(self):
		print('ostrich canot fly')

		

>>> s=bird()

>>> s.flight()
Most of the bird can be fly but some one canot

>>> s.intro()
there are many type of birds.

>>> s=sparrow()

>>> s.intro()
there are many type of birds.

>>> s.flight()
sparrow can be fly


>>> s=ostrich()

>>> s.intro()
there are many type of birds.

>>> s.flight()
ostrich canot fly


>>> class base(object):
	stream='B.Sc'
	def __init__(self,name,age):
		self.name=name
		self.age=age

		

>>> s=base('Gopi raj',21)

>>> s.age
21

>>> s.name
'Gopi raj'

>>> s.stream
'B.Sc'

>>> b=base('Sathish kumar',27)

>>> b.name
'Sathish kumar'

>>> b.age
27

>>> b.stream
'B.Sc'

>>> b.stream="BE bio tech"

>>> s.stream
'B.Sc'

>>> b.stream
'BE bio tech'

>>> base.stream='CSC'

>>> b.stream
'BE bio tech'

>>> s.stream
'CSC'

>>> import datetime

>>> import datetime as t

>>> t.date.today()
datetime.date(2021, 11, 26)

>>> t.date.today().year
2021

>>> _-1999
22

>>> class person():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	@classmethod
	def frombithyear(cls,name,year):
		return cls(name,t.date.today().year-year)
	def isAdult(age):
		return 18<age


>>> s=person('gopi',21)

>>> s.name
'gopi'


>>> class person():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	@classmethod
	def frombithyear(cls,name,year):
		return cls(name,t.date.today().year-year)
	def isAdult(age):
		return 18<age


>>> class person():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	@classmethod
	def frombithyear(cls,name,year):
		return cls(name,t.date.today().year-year)
	@staticmethod
	def isAdult(age):
		return 18<age

	

>>> s=person('Gopi',21)


>>> b=person.frombithyear('Gopi',1999)

>>> b.age
22

>>> b.name
'Gopi'

>>> b.isAdult
<function person.isAdult at 0x000001200169BC10>

>>> b.isAdult(22)
True

>>> b.frombithyear('gopi',2000)
<__main__.person object at 0x000001200166BEB0>

>>> b.name
'Gopi'

>>> b.age
22

>>> s.name
'Gopi'

>>> s.age
21

>>> s.isAdult(21)
True

>>> s=person.frombithyear('Sathish kumar',1991)

>>> s.name
'Sathish kumar'

>>> s.age
30

>>> s.isAdult(30)
True
