
>>>                                          # string
>>> print('gopi raj')
gopi raj
>>> print("gopi raj")
gopi raj
>>> "i don't want this pen"
"i don't want this pen"
>>> print("i don't want this pen")
i don't want this pen
>>> 'i don't want this pen'
SyntaxError: invalid syntax
>>> 'i don\'t want this pen'
"i don't want this pen"
>>> print('i don\'t want this pen')
i don't want this pen
>>> '"Isn\'t," they said'
'"Isn\'t," they said'
>>> print('"Isn\'t," they said')
"Isn't," they said
>>> 'im gopiraj'
'im gopiraj'
>>> print('im gopiraj')
im gopirajs
>>> print('im "gopiraj"')
im "gopiraj"
>>> print('i"m "gopiraj"')
i"m "gopiraj"
>>> print('i\'m "gopiraj"')
i'm "gopiraj"
>>> 
>>> 
>>> 'first line \n second line'
'first line \n second line'
>>> print('first line \n second line')
first line 
 second line
>>> print('first line \nsecond line')
first line 
second line
>>> s='first line \n second line'
>>> print(s)
first line 
 second line
>>> 
>>> 
>>> # you can see raw string adding an r before first quests
>>> 

>>> s='c\app\name\firstpro'
>>> print(s)
cpp
ameirstpro
>>> print(r'c\app\name\firstpro')
c\app\name\firstpro
>>> """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
'Usage: thingy [OPTIONS]\n     -h                        Display this usage message\n     -H hostname               Hostname to connect to\n'
>>> print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

>>> print()

>>> print("""\

               name              =          gopiraj
               age               =          22
               sex               =          male
               height            =          174cm
""")

               name              =          gopiraj
               age               =          22
               sex               =          male
               height            =          174cm

  



>>> 
>>> prefix='py'
>>> prefix 'thon'
SyntaxError: invalid syntax
>>> prefix + 'thon'
'python'
>>> ('un' * 3)
'ununun'
>>> ('un' * 3)'imm'
SyntaxError: invalid syntax
>>> ('un' * 3)+'imm'
'unununimm'
>>> 
>>> 
>>> word='python'
>>> word[0]  # string first character
'p'
>>> word[1]
'y'
>>> word[5]
'n'
>>> word[-1] # last-first character
'n'
>>> word[-2] # last-first character
'o'
>>> word[-2] # last-second character
'o'
>>> word[-6] # negative last  character
'p'
>>> word[0:3]
'pyt'
>>> word[0:5]
'pytho'
>>> word[0:6:2]
'pto'
>>> word[0:6:-1]
''
>>> word[::-1]
'nohtyp'
>>> word[-6:-1:-1]
''
>>> word[-1:-6:-1]
'nohty'
>>> word[-1:-7:-1]
'nohtyp'
>>> word[-1:-7]
''
>>> word[-1:-6]
''
>>> word[-1:-6:1]
''
>>> word[-6]
'p'
>>> word[-6::]
'python'
>>> word[-6::-1]
'p'
>>> word[-6:-1:-1]
''
>>> word[-6:-1:1]
'pytho'
>>> word[-6::1]
'python'
>>> word[-6::-1]
'p'
>>> word
'python'
>>> word[0]='j'
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    word[0]='j'
TypeError: 'str' object does not support item assignment
>>> 
