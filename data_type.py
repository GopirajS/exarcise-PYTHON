
                                                   # data type
                                     #str                  
>>> s='hellow world'
>>> print(type(s))
<class 'str'>
>>> print(s)
hellow world
>>> 


>>>                             #int
>>> i=243
>>> print(type(i))
<class 'int'>
>>> print(i)
243
>>> 



>>>                            # float
                           
>>> f=1313.344
>>> print(type(f))
<class 'float'>
>>> print(f)
1313.344
>>> 



>>>                             #complex
>>> c=12+23j
>>> print(type(c))
<class 'complex'>
>>> print(c)
(12+23j)
>>> 





>>>                             #list
>>> l=['apple','oringe','banana','cherry']
>>> print(type(l))
<class 'list'>
>>> print(l)
['apple', 'oringe', 'banana', 'cherry']
>>> 







>>>                            #tuple
>>> t=('county fruit','oringe','pamkin')
>>> print(type(t))
<class 'tuple'>
>>> print(t)
('county fruit', 'oringe', 'pamkin')
>>> 



>>>                               #range
>>> x=range(6)

>>> print(x)
range(0, 6)
>>> print(type(x))
<class 'range'>
>>> 






>>>                                  #dict
>>> d={'name':'gopiraj','age':21,'city':'ssalem'}
>>> print(type(d))
<class 'dict'>
>>> print(d)
{'name': 'gopiraj', 'age': 21, 'city': 'ssalem'}
>>> 







>>>                                   #set
>>> s={'pen','rupper','pencil','table','chackpies'}
>>> print(type(s))
<class 'set'>
>>> print(s)
{'pen', 'rupper', 'table', 'pencil', 'chackpies'}
>>> 






>>>                                      # frozenset

>>> x = frozenset({"apple", "banana", "cherry"})

>>> print(type(x))
<class 'frozenset'>
>>> print(x)
frozenset({'apple', 'banana', 'cherry'})
>>> 






>>>                                       #byte
>>> s=b'hellow'
>>> print(type(s))
<class 'bytes'>
>>> print(s)
b'hellow'
>>> 
>>> 




>>>                                          #bytearray
>>> x=bytearray(5)
>>> print(x)
bytearray(b'\x00\x00\x00\x00\x00')
>>> print(type(x))
<class 'bytearray'>





>>>                                   #    memoryview
                                  
>>> x = memoryview(bytes(5))
>>> print(x)
<memory at 0x0000022809172040>
>>> print(type(x))
<class 'memoryview'>
>>> 