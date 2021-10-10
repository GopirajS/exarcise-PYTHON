Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>>                          # tuple

>>> tpl=()  # empty tuple

>>> tpl
()

>>> tpl=('gopi','raj','sathish','kumar','gopal')

>>> tpl
('gopi', 'raj', 'sathish', 'kumar', 'gopal')

>>> tpl=(1,2,3,4,5,6,7)

>>> tpl
(1, 2, 3, 4, 5, 6, 7)

>>> s=1,2,3,4,5,

>>> s
(1, 2, 3, 4, 5)

>>> d='gopi','sathish'

>>> d
('gopi', 'sathish')

>>> type(d)
<class 'tuple'>

>>> name=('gopi raj')  #cosider string

>>> name
'gopi raj'

>>> type(name)
<class 'str'>

>>> name=('gopi raj',)  #cosider tuple

>>> type(name)
<class 'tuple'>

>>> 
>>> # access element in tuple

>>> tpl=('gopi','raj','sathish','kumar','gopal')

>>> tpl[0]
'gopi'

>>> tpl[1]
'raj'

>>> tpl[2]
'sathish'

>>> tpl[3]
'kumar'

>>> tpl[4]
'gopal'

>>> tpl[5] # throung  the error ,out off range of index
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    tpl[5] # throung  the error ,out off range of index
IndexError: tuple index out of range


>>>                        # negative index

>>> tpl=('gopi','raj','sathish','kumar','gopal')

>>> tpl[-1]
'gopal'

>>> tpl[-2]
'kumar'

>>> tpl[-3]
'sathish'

>>> tpl[-4]
'raj'

>>> tpl[-5]
'gopi'

>>> tpl[-6]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    tpl[-6]
IndexError: tuple index out of range

>>> a,b,c,d,e=tpl

>>> print(a,b,c,d,e)
gopi raj sathish kumar gopal

>>>                       #update and delete tuple elements

>>> tpl=('gopi','raj','sathish','kumar','gopal')

>>> tpl[0]
'gopi'

>>> tpl[0]='Gopi'
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    tpl[0]='Gopi'
TypeError: 'tuple' object does not support item assignment

>>> del tpl[0]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    del tpl[0]
TypeError: 'tuple' object doesn't support item deletion

>>> del tpl

>>> print(tpl)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(tpl)
NameError: name 'tpl' is not defined

>>>            #using tuple() constucter to  used convert all iterable to tuple type

>>> tpl=tuple('hellow')  # string convert to tuple


>>> tpl
('h', 'e', 'l', 'l', 'o', 'w')


>>> tpl=tuple([1,2,3,4,5])

>>> tpl
(1, 2, 3, 4, 5)


>>> tpl=tuple({'gopi','raj',23}) # convert set to tuple

>>> tpl
('raj', 'gopi', 23)

>>> tpl = tuple({1:"One",2:"Two"}) # converts dictionary to tuple

>>> tpl
(1, 2)



>>>                   #tuple operation +,*,[],[:],in,not in


>>> t=('gopi','raj',)

>>> s=('sathish','kumar')

>>> t+s
('gopi', 'raj', 'sathish', 'kumar')

>>> s=(1,2,3,4,5,6,7,8,9)

>>> t=('gopi','raj','sathish','kumar','gopal')

>>> s+t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 'gopi', 'raj', 'sathish', 'kumar', 'gopal')


>>> t*2
('gopi', 'raj', 'gopi', 'raj')


>>> tpl=('gopi','raj','sathish','kumar','gopal')

>>> tpl[3]
'kumar'

>>> tpl[2]
'sathish'

>>> tpl[-1]
'gopal'

>>> tpl[--4]
'gopal'
>>> tpl[4]
'gopal'


>>> s=(1,2,3,4,5,6,7,8,9)

>>> s[:]
(1, 2, 3, 4, 5, 6, 7, 8, 9)

>>> s[2:6]
(3, 4, 5, 6)

>>> s[2:8]
(3, 4, 5, 6, 7, 8)

>>> s[2:8]
(3, 4, 5, 6, 7, 8)

>>> s[2:9]
(3, 4, 5, 6, 7, 8, 9)

>>> s[2:10]
(3, 4, 5, 6, 7, 8, 9)

>>> s[2:12]
(3, 4, 5, 6, 7, 8, 9)
>>> 

>>>                        # in operation

>>> s=(1,2,3,4,5,6,7,8,9)

>>> 5 in s
True

>>> 9 in s
True

>>> 29 in s
False

>>> 28 not in s
True

>>> 228 not in s
True

>>> 500 not in s
True

>>> 5 not in s
False
>>> 