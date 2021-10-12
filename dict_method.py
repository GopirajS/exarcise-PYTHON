Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>>            #dict.clear()

>>> romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5 }

>>> print(romanNums)
{'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}

>>> romanNums.clear()

>>> print('after calling clear() mehtod :',romanNums)
after calling clear() mehtod : {}

>>> numdict = {1:'one',2:'two',3:'three',4:'four',5:'five'}

>>> print(numdict)
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

>>> numdict.clear()

>>> numdict
{}

>>> #--------------------------------------------------
>>> #                              dict.copy()

>>> numdict = {1:'one',2:'two',3:'three',4:'four',5:'five'}

>>> copy_dict=numdict.copy()

>>> copy_dict

{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

>>> s=copy_dict

>>> s
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

>>> copy_dict
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

>>> #-------------------------------------------------------------
>>> #              dictionary.fromkeys(sequence, value)

>>> key={'name'}

>>> value={'gopi'}

>>> d=dict.fromkeys(key,value)

>>> d
{'name': {'gopi'}}

>>> value='gopi'

>>> d=dict.fromkeys(key,value)

>>> d
{'name': 'gopi'}

>>> keys = {'Mumbai','Bangalore','Chicago','New York'}

>>> value='city'

>>> d=dict.fromkeys(keys,value)

>>> d
{'New York': 'city', 'Bangalore': 'city', 'Chicago': 'city', 'Mumbai': 'city'}

>>> key=(1,2,3,4,5)

>>> value='number'

>>> d=dict.fromkeys(key,value)

>>> d
{1: 'number', 2: 'number', 3: 'number', 4: 'number', 5: 'number'}
>>> #------------------------------------------------------------

>>> #                       dict.get(key, value)

>>> numdict = {1:'one',2:'two',3:'three',4:'four',5:'five'}

>>> numdict.get(1)
'one'

>>> numdict.get(3)
'three'

>>> numdict.get(5)
'five'
>>> numdict.get(4564)

>>> s=numdict.get(4564)

>>> s


>>> #-----------------------------------------------------------

>>> #                               dict.items()

>>> numdict = {1:'one',2:'two',3:'three',4:'four',5:'five'}

>>> numdict.items()
dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])

>>> s=numdict.items()

>>> s
dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])

>>> type(s)
<class 'dict_items'>

>>> #---------------------------------------------

>>> #dict.keys()

>>> numdict = {1:'one',2:'two',3:'three',4:'four',5:'five'}

>>> numdict.keys()
dict_keys([1, 2, 3, 4, 5])

>>> for i in numdict.keys():
	i

	
1
2
3
4
5

>>> #----------------------------------------


>>> #numdict = {1:'one',2:'two',3:'three',4:'four',5:'five'}
>>> #                     dict.pop(key, default)

>>> numdict = {1:'one',2:'two',3:'three',4:'four',5:'five'}

>>> numdict.pop(1)
'one'
>>> 

>>> print(numdict)
{2: 'two', 3: 'three', 4: 'four', 5: 'five'}

>>> numdict.pop(3)
'three'

>>> print(numdict)
{2: 'two', 4: 'four', 5: 'five'}

>>> 

>>> numdict.pop(7)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    numdict.pop(7)
KeyError: 7

>>> numdict.pop(7,'not found')
'not found'

>>> #                          dict.popitem()

>>> 

>>> romanNums = {'I':1, 'II':2, 'III':3 }

>>> print(romanNums.popitem())
('III', 3)

>>> print(romanNums.popitem())
('II', 2)

>>> print(romanNums.popitem())
('I', 1)

>>> print(romanNums.popitem())
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    print(romanNums.popitem())
KeyError: 'popitem(): dictionary is empty'

>>>             #    dict.setdefault(key, defaultValue)
            
>>> s=romanNums.setdefault('IV')

>>> s

>>> print(s)
None

>>> romanNums
{'IV': None}

>>> romanNums = {'I':1, 'II':2, 'III':3 }

>>> s=romanNums.setdefault('IV')

>>> s

>>> romanNums
{'I': 1, 'II': 2, 'III': 3, 'IV': None}

>>> s=romanNums.setdefault('IV',4)


>>> romanNums
{'I': 1, 'II': 2, 'III': 3, 'IV': None}

>>> value=romanNums.setdefault('name','gopi')

>>> value
'gopi'

>>> romanNums
{'I': 1, 'II': 2, 'III': 3, 'IV': None, 'name': 'gopi'}

>>> romanNums = {'I':1, 'II':2, 'III':3 }

>>> romanNums.setdefault('IV',4)
4
>>> romanNums
{'I': 1, 'II': 2, 'III': 3, 'IV': 4}
>>> #---------------------------------------------------------

>>> 

>>> #               dict.update(iterable)
>>> 

>>> romanNums = {'I':1,'III':3,'V':5}


>>> evenRomanNums = {'II':2,'IV':4}

>>> 

>>> romanNums.update(evenRomanNums)

>>> romanNums
{'I': 1, 'III': 3, 'V': 5, 'II': 2, 'IV': 4}

>>> romanNums = {'I':1,'III':3,'V':5}

>>> print(romanNums)
{'I': 1, 'III': 3, 'V': 5}

>>> romanNums.update()

>>> romanNums
{'I': 1, 'III': 3, 'V': 5}
>>> 

>>> #-------------------------------------------------
>>> #                      dict.values()

>>> 
>>> romanNums = {'I':1,'III':3,'V':5}
>>> romanNums.values()
dict_values([1, 3, 5])
>>> for i in romanNums.values():
	i

	
1
3
5
>>> 