>>>#================================================================

>>> hex(12)
'0xc'

>>> hex(120)
'0x78'

>>> oct(78)
'0o116'

>>> oct(1120)
'0o2140'

>>> oct(120)
'0o170'

>>> bin(2)
'0b10'

>>> hex(12)
'0xc'
>>> float.hex(12.1)
'0x1.8333333333333p+3'

>>> hex(123)
'0x7b'

>>> number=123

>>> print("Hexadecimal form of " + str(number) +
       " is " + hex(number).lstrip("0x").rstrip("L"))
Hexadecimal form of 123 is 7b

>>> print("Hexadecimal form of " + str(number) +
       " is " + hex(number).lstrip("0x"))
Hexadecimal form of 123 is 7b

>>> #=========================================================


>>> #  hasattr()  method

>>> str='this is string'

>>> hasattr(str,"zfill")
True

>>> hasattr(str,"strip")
True

>>> hasattr(str,"strim")
False

>>> class myclass():
	name='gopiraj'
	age=21

	
>>> myobj=myclass()

>>> hasattr(myobj,'name')
True

>>> hasattr(myobj,'age')
True

>>> hasattr(myobj,'__namea__')
False

>>> hasattr(myobj,'__name__')
False

>>> #===============================================================

>>> #   id()  method

>>> n=12

>>> id(12)

1785191164560

>>> id(n)
1785191164560

>>> 21
21

>>> id(21)
1785191164848

>>> s=12

>>> id(s)
1785191164560

>>> id(n)
1785191164560

>>> l=[1,2,3,4,5]

>>> id(l)
1785233509696

>>> s=(1,2,3,4,5)

>>> id(s)
1785232703712

>>> a=[1,2,3,4,5]

>>> id(a)
1785233514624

>>> id(l)
1785233509696

>>> class myclass:
	name='gopiraj'
	age=21

	
>>> s=myclass()

>>> id(s)
1785232672848

>>> s2=myclass()

>>> id(s)
1785232672848

>>> s3=myclass()

>>> id(s3)
1785233322384

>>> id(s)==id(s)
True

>>> id(s)==id(s)==id(s3)
False

>>> s=myclass()

>>> s1=myclass()

>>> id(s)==id(s1)
False

>>> id(s)
1785233325408

>>> id(s1)
1785232672848

>>> id(s)
1785233325408

>>> id(s)
1785233325408

>>> id(s2)
1785233632704

>>> s=myclass()


>>> id(s)
1785233325744

>>> s.name='sathish kumar'

>>> id(s)
1785233325744

>>> id(s.name)
1785233463024

>>> s=myclass()

>>> id(s.name)
1785233447856

>>> id(s.name)
1785233447856


>>> s.name='kumar'

>>> id(s.name)
1785233459760


>>> #==================================================================

>>> #  int()  method

>>> oct(123)
'0o173'

>>> int('173',8)
123

>>> int('173')
173

>>> int(0o173)
123

>>> bin(123)
'0b1111011'

>>> int('0b1111011',2)
123

>>> int('0b1111011',2)
123

>>> hex(123)
'0x7b'

>>> int('7b',16)
123

>>> int('0x7b',16)
123


>>> int(123)
123

>>> x=12

>>> int([x])

>>> i=int(12.3)

>>> i
12

>>> i=int('12')

>>> i
12

>>> i
12

>>> bin(123)
'0b1111011'

>>> int('0b1111011')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int('0b1111011')
ValueError: invalid literal for int() with base 10: '0b1111011'

>>> int('0b1111011',2)
123

>>> int(0b1111011)
123

>>> oct(123)
'0o173'

>>> int('0o173',8)
123

>>> int(0o173)
123

>>> hex(123)
'0x7b'

>>> int('0x7b',16)
123

