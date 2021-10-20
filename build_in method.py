Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # abs() method


>>> z='''
           Syntax:
                   abs(num)


          Parameters:
                    num: An int, float, or complex number.
'''

>>> print('absolute value of 10',abs(10))
absolute value of 10 10

>>> print('absolute value of -10:   ',abs(-10))
absolute value of -10:    10

>>> print('absolute value of -10:   ',abs(-10.32))
absolute value of -10:    10.32

>>> print('absolute value of -10.32:   ',abs(-10.32))
absolute value of -10.32:    10.32

>>> print('absolute value of -100:   ',abs(-100))
absolute value of -100:    100

>>> print('absolute value of 12.333:   ',abs(12.333))
absolute value of 12.333:    12.333

>>> print('absolute value of 2+3j:   ',abs(2+3j))
absolute value of 2+3j:    3.605551275463989

>>> print('absolute value of -2-3j:   ',abs(-2-3j))
absolute value of -2-3j:    3.605551275463989

>>> print('absolute value of -2+3j:   ',abs(-2+3j))
absolute value of -2+3j:    3.605551275463989

>>> print('absolute value of 2-3j:   ',abs(2-3j))
absolute value of 2-3j:    3.605551275463989

>>> bin(123)
'0b1111011'

>>> oct(244)
'0o364'

>>> hex(35)
'0x23'

>>> print('absolute value of bin od 123:   ',abs(0b1111011))
absolute value of bin od 123:    123

>>> print('absolute value of oct of 244:   ',abs(0o364))
absolute value of oct of 244:    244

>>> print('absolute value of hex of 35:   ',abs(0x23))
absolute value of hex of 35:    35



>>> #----------------------------------------------------------------------


>>> # all() method
>>> z='''
          all() Syntax:
                      all(iterable)


            Parameters:
                       iterable: A list, tuple, string, set, or dictionary object.
                       '''

>>> l=[]

>>> print('list of all() mehtod :  ',all(l))
list of all() mehtod :   True

>>> l=[1,2,3,4,5]

>>> print('list of all() mehtod :  ',all(l))
list of all() mehtod :   True

>>> l=[1,2,3,4,5,0]

>>> print('list of all() mehtod :  ',all(l))
list of all() mehtod :   False

>>> l=[1,2,3,4,5,False]

>>> print('list of all() mehtod :  ',all(l))
list of all() mehtod :   False

>>> s=set()

>>> print('set of all():   ',all(s))
set of all():    True

>>> s={'gopi','sathish'}

>>> print('set of all():   ',all(s))

set of all():    True

>>> s={'gopi','sathish',0}

>>> print('set of all():   ',all(s))
set of all():    False

>>> s={'gopi','sathish',False}

>>> print('set of all():   ',all(s))
set of all():    False

>>> s={'gopi','sathish',False,True}

>>> print('set of all():   ',all(s))
set of all():    False

>>> d={}

>>> print('dict of all():   ',all(d))
dict of all():    True

>>> d={'name':'gopi'}

>>> print('dict of all():   ',all(d))
dict of all():    True

>>> d={1:'gopi'}

>>> print('dict of all():   ',all(d))
dict of all():    True

>>> d={0:'gopi'}

>>> print('dict of all():   ',all(d))
dict of all():    False

>>> d={False:'gopi'}

>>> print('dict of all():   ',all(d))

dict of all():    False

>>> s=''

>>> print('string of all():   ',all(s))
string of all():    True

>>> s='hi hellow '

>>> print('string of all():   ',all(s))
string of all():    True

>>> s='       '

>>> print('string of all():   ',all(s))
string of all():    True

>>> s=False

>>> print('string of all():   ',all(s))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print('string of all():   ',all(s))
TypeError: 'bool' object is not iterable
>>> 
>>> #-----------------------------------------------------------

>>> z='''
        Syntax:
               any(iterable)

    Parameters:
              iterable: An iterable (list, tuple, string, set, dictionary).

              '''
>>> l=[]

>>> print(any(l))
False

>>> l=[1,2,3]

>>> print(any(l))
True

>>> l=[1,2,3,0]

>>> print(any(l))
True

>>> l=[1,2,3,0,False,True]

>>> print(any(l))
True

>>> l=[False]

>>> print(any(l))
False

>>> l=[0]

>>> print(any(l))
False

>>> l=[0]

>>> l=[0,1]

>>> print(any(l))
True

>>> s=''

>>> print(any(s))
False

>>> s=' '

>>> print(any(s))
True

>>> s='gopi '

>>> print(any(s))
True

>>> s='False'

>>> print(any(s))
True
>>> s=set()

>>> print(any(s))
False

>>> s={'gopi','raj'}

>>> print(any(s))
True

>>> s={0,False}

>>> print(any(s))
False

>>> s={0,False,True}

>>> print(any(s))
True

>>> d={}

>>> print(any(d))
False

>>> d={1}

>>> print(any(d))
True

>>> d={0}

>>> print(any(d))
False

>>> d={0,1}

>>> print(any(d))
True
>>> 
