Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>                                 #tuple
>>> 

>>> thistuple = ("apple", "banana", "cherry", "apple", "cherry")

>>> thistuple
('apple', 'banana', 'cherry', 'apple', 'cherry')

>>> print(len(thistuple))
5



>>>                                 #to creat one iterm with tuple

>>> t=('apple',)

>>> print(type(t))
<class 'tuple'>

>>> t=('gopi','raj','sathish','kumar')

>>> print(type(t))
<class 'tuple'>

>>> print(t)
('gopi', 'raj', 'sathish', 'kumar')

>>> t=(1,2,3,4,5)

>>> print(t)
(1, 2, 3, 4, 5)

>>> t=(True,False,None)

>>> print(type(t))
<class 'tuple'>

>>> print(t)
(True, False, None)

>>> print(*t)
True False None

>>> t=('gopi','raj','sathish','kumar')

>>> print(*t)
gopi raj sathish kumar

>>> t=('gopi',23,True,23.33,"$",False)


>>> print(type(t))
<class 'tuple'>




>>>                                             # update tuple


>>> t=('gopi','raj','sathish','kumar')

>>> t[0]
'gopi'

>>> t[0]="Gopi"
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t[0]="Gopi"
TypeError: 'tuple' object does not support item assignment

>>> t=('gopi','raj','sathish','kumar')

>>> s=list(t)

>>> s[0]
'gopi'

>>> s[0]="Gopi"

>>> t=tuple(s)

>>> t
('Gopi', 'raj', 'sathish', 'kumar')




>>>                                       #add items
>>> 

>>> t=('gopi',23,True,23.33,"$",False)

>>> d=list(t)

>>> d.append('gopal')

>>> d
['gopi', 23, True, 23.33, '$', False, 'gopal']


>>> t=tuple(d)


>>> t
('gopi', 23, True, 23.33, '$', False, 'gopal')

>>> fruits = ("apple", "banana", "cherry")


>>> a,b,c=fruits

>>> a
'apple'

>>> b
'banana'

>>> c
'cherry'

>>> fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

>>> (a,b,*c)=fruits

>>> a
'apple'

>>> b
'banana'

>>> c
['cherry', 'strawberry', 'raspberry']

>>> (a,*b,c)=fruits

>>> a
'apple'

>>> b
['banana', 'cherry', 'strawberry']

>>> c
'raspberry'




>>>                              # tuple mehtod
>>>                               #cout() and index()


>>> thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)


>>> thistuple.count(5)
2

>>> thistuple.index(5)
5

