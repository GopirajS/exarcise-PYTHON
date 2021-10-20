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
