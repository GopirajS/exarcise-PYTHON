Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>>              #Python List append()

>>> 

>>> cities = ['Mumbai', 'London', 'Paris', 'New York']

>>> city='tamil nadu'

>>> cities.append(city)

>>> cities
['Mumbai', 'London', 'Paris', 'New York', 'tamil nadu']


>>> tuple=('tamil nadu','salem')

>>> cities.append(tuple)

>>> cities
['Mumbai', 'London', 'Paris', 'New York', 'tamil nadu', ('tamil nadu', 'salem')]

>>> type(cities)
<class 'list'>

>>> city=['coimbatur',"chennai"]

>>> cities.append(city)

>>> cities
['Mumbai', 'London', 'Paris', 'New York', 'tamil nadu', ('tamil nadu', 'salem'), ['coimbatur', 'chennai']]

>>> cities = ['Mumbai', 'London', 'Paris', 'New York']

>>> cities.append(0)

>>> cities.append(10)

>>> cities
['Mumbai', 'London', 'Paris', 'New York', 0, 10]


>>> cities = ['Mumbai', 'London']

>>> d={'Paris':1, 'New York':2}

>>> cities
['Mumbai', 'London']

>>> cities.append(d)

>>> cities
['Mumbai', 'London', {'Paris': 1, 'New York': 2}]

>>> for i in cities:
	i

	
'Mumbai'
'London'
{'Paris': 1, 'New York': 2}

>>> tuble=('gopi','raj','sathish ','kumar')

>>> cities.append(tuble)

>>> cities
['Mumbai', 'London', {'Paris': 1, 'New York': 2}, ('gopi', 'raj', 'sathish ', 'kumar')]

>>> cities = ['Mumbai', 'London']

>>> cities.append('chennai')

>>> cities
['Mumbai', 'London', 'chennai']

>>> cities.append(4)

>>> cities
['Mumbai', 'London', 'chennai', 4]


>>> #-----------------------------------------------------------------------
>>> 
>>>                          #Python List clear() - Removes All Items From List


>>> cities = ['Mumbai', 'London', 'Paris', 'New York']

>>> print('Before calling clear():',cities)
Before calling clear(): ['Mumbai', 'London', 'Paris', 'New York']

>>> cities.clear()

>>> print('After calling clear():',cities)
After calling clear(): []

>>> cities = ['Mumbai',1,2,3,[4,5,'gopi']]

>>> cities.clear()

>>> cities
[]


>>> #--------------------------------------------------------------------------
>>>          #Python List copy() - Creates Shallow Copy of List



>>> cities = ['Mumbai', 'London', 'Paris', 'New York']

>>> s=cities.copy()

>>> s
['Mumbai', 'London', 'Paris', 'New York']

>>> print("original list:",cities)
original list: ['Mumbai', 'London', 'Paris', 'New York']

>>> print('copi list:',s)

copi list: ['Mumbai', 'London', 'Paris', 'New York']

>>> s.append('gopi')

>>> s
['Mumbai', 'London', 'Paris', 'New York', 'gopi']

>>> cities
['Mumbai', 'London', 'Paris', 'New York']

>>> num=[1,2,3,4,5]

>>> num.append(6)

>>> num
[1, 2, 3, 4, 5, 6]

>>> s=num.copy()

>>> s
[1, 2, 3, 4, 5, 6]

>>> s.append(7)

>>> s
[1, 2, 3, 4, 5, 6, 7]


>>> #-----------------------------------------------------------
>>>                              #python list count() methed

>>> # list.count() method return the number of time occurs in the list


>>> cities = ['Mumbai', 'London', 'Paris', 'New York','Mumbai']

>>> s=cities.count('Mumbai')

>>> print('the number of times mumbai  in list: ',s)
the number of times mumbai  in list:  2

>>> name=['gopi','raj','sathish','kumar','raj','gopi','gopi']

>>> d=name.count('gopi')

>>> print('number of the times "gopi" in list:',d)
number of the times "gopi" in list: 3

>>> s=name.count('raj')

>>> print('number of the times "raj" in list:',s)
number of the times "raj" in list: 2


>>> #-----------------------------------------------------------------
>>> 
>>>                            #Python List extend() - Adds Iterables to List


>>> #list.extend() method adds a all the iterms from the spacified iterable (tuple,list,dict,set,string)to the endd of the string


>>> name=['gopi','raj','sathish','kumar']

>>> name2=['parimal','shanmugam']

>>> name.extend(name2)

>>> name
['gopi', 'raj', 'sathish', 'kumar', 'parimal', 'shanmugam']

>>> name=['gopi','raj','sathish','kumar']

>>> string='gopiraj'

>>> name.extend(string)

>>> name
['gopi', 'raj', 'sathish', 'kumar', 'g', 'o', 'p', 'i', 'r', 'a', 'j']

>>> s=list('helllow')

>>> s
['h', 'e', 'l', 'l', 'l', 'o', 'w']

>>> t=('hai','hellow','python')

>>> name=['gopi','raj','sathish','kumar']

>>> name.extend(t)

>>> name
['gopi', 'raj', 'sathish', 'kumar', 'hai', 'hellow', 'python']

>>> name=['gopi','raj','sathish','kumar']

>>> d={'name':'gopi','age':'21'}

>>> name.extend(d)

>>> name
['gopi', 'raj', 'sathish', 'kumar', 'name', 'age']

>>> s={'hai','hellow','hais'}

>>> name=['gopi','raj','sathish','kumar']

>>> name.extend(s)

>>> name
['gopi', 'raj', 'sathish', 'kumar', 'hellow', 'hai', 'hais']

>>> s={'hai','hellow','hai'}

>>> name=['gopi','raj','sathish','kumar']

>>> name.extend(s)

>>> name
['gopi', 'raj', 'sathish', 'kumar', 'hellow', 'hai']


>>> #different between append() and  extend()

>>> city=['mumbai','landon','tamilnadu']
>>> 
>>> fruits=['apple','oringe','banana']
>>> 
>>> objec=['pen','pencil','slat']

>>> city.extend(fruits)

>>> city
['mumbai', 'landon', 'tamilnadu', 'apple', 'oringe', 'banana']

>>> fruits.append(objec)

>>> fruits
['apple', 'oringe', 'banana', ['pen', 'pencil', 'slat']]


>>> #-------------------------------------------------------------------
>>>                                      #Python List index() - Get Index of Element
>>> 



>>> #list.index() method return the index position of the first ocurens of the spacified item



>>> name=['gopi','raj','sathish','kumar']

>>> name.index('kumar')
3

>>> cities = ['Mumbai', 'London', 'Paris', 'New York','Delhi','Chennai','Paris']

>>> position=cities.index('Paris')

>>> print('first ocurens of paris in list :',position)

first ocurens of paris in list : 2

>>> cities = ['Mumbai', 'London', 'Paris', 'New York','Delhi','Chennai','Paris','salem','paris']

>>> cities.index('Paris')
2

>>> cities = ['Mumbai', 'London', 'Paris', 'New York','Delhi','Chennai','Paris','salem','Paris']

>>> cities.count('Paris')
3
>>> s=cities.index('Paris')

>>> s
2

>>> s=cities.index('Paris',s+1)

>>> s
6

>>> s=cities.index('Paris',s+1)

>>> s
8

>>> s=cities.index('Paris',s+1)
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    s=cities.index('Paris',s+1)
ValueError: 'Paris' is not in list

>>> s
8



>>> #------------------------------------------------------------------------------
>>>                     #Python List insert() - Insert Element At Specified Position

>>> #list.insert() method used to insert a value ar give posion in the list

>>> cities = ['Mumbai', 'London', 'Paris', 'New York','Delhi']

>>> cities.insert(0,'salem')

>>> cities
['salem', 'Mumbai', 'London', 'Paris', 'New York', 'Delhi']


>>> cities.insert(10,'salem')

>>> cities
['salem', 'Mumbai', 'London', 'Paris', 'New York', 'Delhi', 'salem']

>>> set={'gopi','raj'}

>>> d={'name':'gopi','age':'21'}

>>> t=('hi','hello')

>>> s='string'

>>> cities = ['Mumbai', 'London', 'Paris']

>>> cities.insert(0,s)

>>> cities
['string', 'Mumbai', 'London', 'Paris']

>>> cities
['string', 'string', 'Mumbai', 'London', 'Paris']

>>> cities.insert(0,set)

>>> cities
[{'raj', 'gopi'}, 'string', 'string', 'Mumbai', 'London', 'Paris']

>>> cities = ['Mumbai', 'London', 'Paris']

>>> cities.insert(10,d)

>>> cities
['Mumbai', 'London', 'Paris', {'name': 'gopi', 'age': '21'}]

>>> cities.insert(10,t)

>>> cities
['Mumbai', 'London', 'Paris', {'name': 'gopi', 'age': '21'}, ('hi', 'hello')]


>>> #-------------------------------------------------------

>>>                           #python pop(index) method

>>> # list.pop() method returns an item from the spacified position of the list and removes .If no index spacifed atomatically remove last index inter remove.

>>> cities = ['Mumbai', 'London', 'Paris', 'New York','Delhi']

>>> cities.pop(1)
'London'

>>> cities
['Mumbai', 'Paris', 'New York', 'Delhi']

>>> cities.pop()
'Delhi'

>>> cities
['Mumbai', 'Paris', 'New York']

>>> cities = ['Mumbai', 'London', 'Paris', 'New York','Delhi']

>>> cities.pop(10)

Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    cities.pop(10)
IndexError: pop index out of range

>>> #---------------------------------------------------------------
>>>                                           #python remove(item) method

>>> # list.remove() method remove the first ocurens of the spacifies item in list.it raise value error ,if spaified iterm does not exist in list

>>> cities = ['Mumbai', 'London', 'Paris', 'New York','Delhi']

>>> cities.remove('London')

>>> cities
['Mumbai', 'Paris', 'New York', 'Delhi']

>>> cities.remove('London')
Traceback (most recent call last):
  File "<pyshell#287>", line 1, in <module>
    cities.remove('London')
ValueError: list.remove(x): x not in list

>>> 

>>> cities.remove()
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    cities.remove()
TypeError: list.remove() takes exactly one argument (0 given)

>>> #-----------------------------------------------------------------------------
>>>                                              #python reverse() method


>>> #list.reverse() method reverse the position of elements in list

>>> cities = ['Mumbai', 'London', 'Paris', 'New York','Delhi']

>>> cities.reverse()

>>> cities
['Delhi', 'New York', 'Paris', 'London', 'Mumbai']

>>> cities.reverse()

>>> cities
['Mumbai', 'London', 'Paris', 'New York', 'Delhi']

>>> cities[::]
['Mumbai', 'London', 'Paris', 'New York', 'Delhi']


>>> cities[::-1]
['Delhi', 'New York', 'Paris', 'London', 'Mumbai']


 