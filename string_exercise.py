
>>> string='hellow world im gopi raj thish is python world'

>>> print(string)
hellow world im gopi raj thish is python world

>>> string='\nhellow world im gopi raj thish is python world'


>>> print(string)

hellow world im gopi raj thish is python world

>>> string='\nhellow world \nim gopi raj thish is python world'

>>> print(string)

hellow world 
im gopi raj thish is python world


>>> s='''gopi
          raj
          satish
          kuamr'''



>>> print(s)
gopi
          raj
          satish
          kuamr

>>> s='gopiraj'

>>> s
'gopiraj'

>>> s[-1]
'j'

>>> len(s)
7

>>> s[-7]
'g'


>>> s[-1]
'j'


>>> s[7]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s[7]
IndexError: string index out of range

>>> s[6]
'j'

>>> len(s)
7

>>> ~7
-8

>>> ~7-1
-9

>>> ~7+11
3

>>> ~7+1
-7


>>> for i in range(len(s)):
	print(s[i],end='')

	
gopiraj

>>> for i in range(len(s)):
	print(s[i],end=' ')

	
g o p i r a j 

>>> s[0]
'g'

>>> s[-1]
'j'

>>> s[-7]
'g'

>>> s[6]
'j'

>>> s='gopi raj satish kuamr'

>>> s[0]
'g'

>>> s[2]
'p'

>>> s[5]
'r'

>>> s[4]
' '

>>> s[4]
' '


>>> s
'gopi raj satish kuamr'

>>> len(s)
21

>>> s[0:12]
'gopi raj sat'

>>> s[0:19]
'gopi raj satish kua'

>>> s[0:15]
'gopi raj satish'

>>> slice(s)
slice(None, 'gopi raj satish kuamr', None)

>>> s[0:-4]
'gopi raj satish k'

>>> s[0:-4:2]
'gp a aihk'


>>> s[0:-4:1]
'gopi raj satish k'

>>> s[0:-4:-1]
''

>>> s[0:-4:-2]
''

>>> s
'gopi raj satish kuamr'

>>> s[3]
'i'

>>> del s[3]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    del s[3]
TypeError: 'str' object doesn't support item deletion

>>> del s

>>> s
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s
NameError: name 's' is not defined



>>> print('I\'m \'\"gopi\"')
I'm '"gopi"

>>> print('I\'m \"gopi\"')
I'm "gopi"

>>> print("I'm \"gopi\"")
I'm "gopi"



>>> s="C:\\python\\geek\\"

>>> print(s)
C:\python\geek\


>>> hex(Gopi)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    hex(Gopi)
NameError: name 'Gopi' is not defined

>>> print('\x47\x65\x65\x6b\x73')
Geeks


>>> hex(2)
'0x2'


>>> 0x2
2


>>> 'x47'
'x47'

>>> '\x47'
'G'

>>> hex('G')
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    hex('G')
TypeError: 'str' object cannot be interpreted as an integer

>>> print('{} {} {}'.format('gopi','raj','sathish'))
gopi raj sathish

>>> print('{2} {1} {0}'.format('gopi','raj','sathish'))
sathish raj gopi

>>> print('{}{}{}'.format(name='gopi',age='21',city='salem'))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    print('{}{}{}'.format(name='gopi',age='21',city='salem'))
IndexError: Replacement index 0 out of range for positional args tuple

>>> print('{name}{age}{city}'.format(name='gopi',age='21',city='salem'))
gopi21salem

>>> print('{name} :{age} :{city}'.format(name='gopi',age='21',city='salem'))

gopi :21 :salem

>>> 1/6
0.16666666666666666

>>> string='{}'.format(1/6)

>>> print(string)

0.16666666666666666

>>> string='{0:0.3}'.format(1/6)

>>> print(string)
0.167

>>> string='{:0.3}'.format(1/6)

>>> print(string)
0.167


>>> string='{1:0.3}'.format(1/6,1.2345)

>>> print(string)
1.23

>>> string='{0:0.3f}'.format(1/6)

>>> print(string)
0.167

>>> s='{:>10}{:^10}{:<10}'.format('gopi','raj','sathish')

>>> print(s)
      gopi   raj    sathish   

>>> print('{:^16} and his born {:>13}'.format('gopiraj',1999))
    gopiraj      and his born          1999

>>> s
'      gopi   raj    sathish   '

>>> s.capitalize
<built-in method capitalize of str object at 0x000001E7B36A81C0>


>>> s=''

>>> print(repr(s))
''

>>> print(s)


>>> print(s)


>>> # logical operator on string in python



>>> s1=''

>>> s2='gopi'

>>> s1 and s2
''

>>> s2 and s1
''

>>> s2 or s1
'gopi'

>>> s1 or s2
'gopi'

>>> s1='gopi'

>>> s2='raj'

>>> s1 and s2
'raj'

>>> s2 and s1
'gopi'


>>> s1 or s2
'gopi'

>>> s1 or s2
'gopi'

>>> s2 or s1
'raj'

>>> s=''

>>> s=' '

>>> not s
False

>>> s=''

>>> not s
True


>>> s='gopi'

>>> not s
False

>>> import string

>>> import string as s

>>> s.Formatter

<class 'string.Formatter'>

>>> t=s.Template('x is $x')

>>> print(t.substitute({'x':1}))
x is 1


>>> print(t.substitute({'x':'gopi'}))
x is gopi

>>> d=s.Template('hi hellow $name ')

>>> l=['gopi','sathish']



>>> for i in l:
	print(i)

	
gopi
sathish


>>> for i in l:
	print(d.substitute(name=i))

	
hi hellow gopi 
hi hellow sathish 

>>> l=[('gopi',12),('sathish',23),('parimala',34)]

>>> t=s.Template('hellow mr $name and you got $mark mark')

>>> for i in l:
	print(t.substitute(name=i[0],	mark=i[1]))

	
hellow mr gopi and you got 12 mark
hellow mr sathish and you got 23 mark
hellow mr parimala and you got 34 mark

>>> a=s.Template('hellow mr $name and his compeny %compeny')

>>> print(a.safe_substitute(name='sathish kuamr',compeny='hemex DX'))
hellow mr sathish kuamr and his compeny %compeny

>>> a=s.Template('hellow mr $name and his compeny $compeny')

>>> print(a.safe_substitute(name='sathish kuamr',compeny='hemex DX'))
hellow mr sathish kuamr and his compeny hemex DX


>>> t='$name is good boy and is age $age'

>>> t=s.Template('$name is good boy and is age $age')

>>> print(t.template())
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    print(t.template())
TypeError: 'str' object is not callable

>>> print(t.template)
$name is good boy and is age $age


>>> t=s.Template('$$ is sympal of $name')

>>> print(t.substitute(name='gopi'))
$ is sympal of gopi

>>> t=s.Template('$$ is sympal of $name and $(name)y')

>>> print(t.substitute(name='gopiraj'))
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    print(t.substitute(name='gopiraj'))
  File "C:\Users\gopir\AppData\Local\Programs\Python\Python39\lib\string.py", line 121, in substitute
    return self.pattern.sub(convert, self.template)
  File "C:\Users\gopir\AppData\Local\Programs\Python\Python39\lib\string.py", line 118, in convert
    self._invalid(mo)
  File "C:\Users\gopir\AppData\Local\Programs\Python\Python39\lib\string.py", line 101, in _invalid
    raise ValueError('Invalid placeholder in string: line %d, col %d' %
ValueError: Invalid placeholder in string: line 1, col 27
>>> t=s.Template('$$ is sympal of $name and ${name}y')

>>> print(t.substitute(name='gopiraj'))
$ is sympal of gopiraj and gopirajy

>>> variable=12

>>> variable='12'

>>> string='Variable as string = %s'%(variable)

>>> print(string)
Variable as string = 12

>>> string='Variable as string = %r'%(variable)


>>> print(string)
Variable as string = '12'

>>> variable=int(variable)

>>> variable
12

>>> string='Variable as string = %d'%(variable)

>>> print(string)
Variable as string = 12

>>> string='Variable as string = %o'%(variable)

>>> print(string)
Variable as string = 14

>>> string='Variable as string = %x'%(variable)

>>> print(string)
Variable as string = c

>>> def funtion():
	'''Demonstrate triple  double  question
          docstrings and does  nothing realy'''
	return 'hellow world'



>>> funtion()
'hellow world'


>>> funtion.__doc__
'Demonstrate triple  double  question\n          docstrings and does  nothing realy'

>>> print(funtion.__doc__)
Demonstrate triple  double  question
          docstrings and does  nothing realy

>>> help(funtion.__doc__)
No Python documentation found for 'Demonstrate triple  double  question\n          docstrings and does  nothing realy'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.


>>> def funtion():
	"""
           Demonstrate triple  double  question
          docstrings and does  nothing realy  """
	return 'hellow world'

>>> funtion.__doc__
'\n           Demonstrate triple  double  question\n          docstrings and does  nothing realy  '

>>> print(funtion.__doc__)

           Demonstrate triple  double  question
          docstrings and does  nothing realy  

>>> help(funtion.__doc__)
No Python documentation found for 'Demonstrate triple  double  question\n          docstrings and does  nothing realy'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.


>>> class myclass:
	"""
    This is a class for mathematical operations on complex numbers.
      
    Attributes:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
    """
	def __init__(self):
		"""
        The constructor for ComplexNumber class.
  
        Parameters:
           real (int): The real part of complex number.
           imag (int): The imaginary part of complex number.   
        """
	def adding(self):
		"""
        The function to add two Complex Numbers.
  
        Parameters:
            num (ComplexNumber): The complex number to be added.
          
        Returns:
            ComplexNumber: A complex number which contains the sum.
        """
		return 'hellow world'

	

>>> myclass.__doc__
'\n    This is a class for mathematical operations on complex numbers.\n      \n    Attributes:\n        real (int): The real part of complex number.\n        imag (int): The imaginary part of complex number.\n    '

>>> print(myclass.__doc__)

    This is a class for mathematical operations on complex numbers.
      
    Attributes:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
    



>>> help(myclass)
Help on class myclass in module __main__:

class myclass(builtins.object)
 |  This is a class for mathematical operations on complex numbers.
 |    
 |  Attributes:
 |      real (int): The real part of complex number.
 |      imag (int): The imaginary part of complex number.
 |  
 |  Methods defined here:
 |  
 |  __init__(self)
 |      The constructor for ComplexNumber class.
 |      
 |      Parameters:
 |         real (int): The real part of complex number.
 |         imag (int): The imaginary part of complex number.
 |  
 |  adding(self)
 |      The function to add two Complex Numbers.
 |      
 |      Parameters:
 |          num (ComplexNumber): The complex number to be added.
 |        
 |      Returns:
 |          ComplexNumber: A complex number which contains the sum.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


>>> def checkEmpty(input, pattern): 
        
    # If both are empty  
    if len(input)== 0 and len(pattern)== 0: 
         return 'true'
    
    # If only pattern is empty 
    if len(pattern)== 0: 
         return 'true'
    
    while (len(input) != 0): 
  
        # find sub-string in main string 
        index = input.find(pattern) 
  
        # check if sub-string founded or not 
        if (index ==(-1)): 
          return 'false'
  
        # slice input string in two parts and concatenate 
        input = input[0:index] + input[index + len(pattern):]              
  
    return 'true'

>>> checkEmpty('Gopiraj','Gopi')
'false'

>>> checkEmpty('Gopiraj','Gopiraj')
'true'
>>> checkEmpty('Gopi','Gopiraj')
'false'

>>> input='gopi'

>>> len(input)
4

>>> patten='gopi'

>>> input.find(patten)
0

>>> patten='gopi raj'

>>> input.find(patten)
-1


>>> input = input[0:index] + input[index + len(patten):]
>>> input
'gop'

>>> input='gopiraj'

>>> patten='raj'

>>> index=input.find(patten)

>>> index
4

>>> input=input[0:index]

>>> input
'gopi'

>>> input[0]
'g'

>>> input[0:4]
'gopi'

>>> len(patten)
3
