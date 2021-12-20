
>>> s=[]

>>> type(s)
<class 'list'>

>>> s=dict[(1,'gopi'),(2,'sathish')]

>>> s
dict[(1, 'gopi'), (2, 'sathish')]

>>> type(s)
<class 'types.GenericAlias'>

>>> s={1:'gopi',2:'sathish',3:'kumar',4:'raj'}

>>> s
{1: 'gopi', 2: 'sathish', 3: 'kumar', 4: 'raj'}


>>> s={'name':'gopiraj','list':[1,2,3,4,5,6]}

>>> s
{'name': 'gopiraj', 'list': [1, 2, 3, 4, 5, 6]}


>>> s['list']
[1, 2, 3, 4, 5, 6]

>>> s.get('list')
[1, 2, 3, 4, 5, 6]

>>> s.items()
dict_items([('name', 'gopiraj'), ('list', [1, 2, 3, 4, 5, 6])])

>>> for i in s.items():
	print(i)

	
('name', 'gopiraj')
('list', [1, 2, 3, 4, 5, 6])

>>> for i in s.items():
	print(i[1])

	
gopiraj
[1, 2, 3, 4, 5, 6]


>>> d={'name':'gopi','age':'21','dict':{1:'one',2:'two',3:'three'}}

>>> d
{'name': 'gopi', 'age': '21', 'dict': {1: 'one', 2: 'two', 3: 'three'}}

>>> d.get('name')
'gopi'

>>> d.get('age')
'21'

>>> d.get('dict')
{1: 'one', 2: 'two', 3: 'three'}

>>> d.get('dict')[1]
'one'

>>> d.get('dict')[2]
'two'

>>> d.get('dict')[3]
'three'


>>> d={'dict1':{'name':'gopi'},'dict2':{'name':'sathish'}}


>>> d
{'dict1': {'name': 'gopi'}, 'dict2': {'name': 'sathish'}}

>>> d['dict1']
{'name': 'gopi'}

>>> d['dict2']
{'name': 'sathish'}


>>> d['dict1']['name']
'gopi'

>>> d={1:'one',2:'two',3:'three','d1':{'name':'gopi','age':'21'}}

>>> d
{1: 'one', 2: 'two', 3: 'three', 'd1': {'name': 'gopi', 'age': '21'}}

>>> d[1]
'one'

>>> d[2]
'two'

>>> d[3]
'three'

>>> d['d1']
{'name': 'gopi', 'age': '21'}


>>> d['d1']['name']
'gopi'

>>> d['d1']['age']
'21'

>>> d
{1: 'one', 2: 'two', 3: 'three', 'd1': {'name': 'gopi', 'age': '21'}}

>>> del d['d1']

>>> d
{1: 'one', 2: 'two', 3: 'three'}

>>> d.pop(1)
'one'

>>> d
{2: 'two', 3: 'three'}

>>> d={1:'one',2:'two',3:'three','d1':{'name':'gopi','age':'21'}}



>>> d
{1: 'one', 2: 'two', 3: 'three', 'd1': {'name': 'gopi', 'age': '21'}}


>>> d.popitem()
('d1', {'name': 'gopi', 'age': '21'})

>>> d
{1: 'one', 2: 'two', 3: 'three'}




>>> d={'name':'gopi','age':'21','city':'salem'}

>>> d
{'name': 'gopi', 'age': '21', 'city': 'salem'}


>>> d.pop('name')
'gopi'


>>> d.popitem()
('city', 'salem')

>>> d
{'age': '21'}

>>> d.popitem()
('age', '21')

>>> d
{}

>>> d={'name':'gopi','age':'21','city':'salem'}

>>> d.clear()


>>> d
{}

>>> c=d.copy()

>>> d
{}

>>> c
{}

>>> d==c
True

>>> d.clear()

>>> c
{}

>>> d
{}

>>> d={'name':'gopi','age':'21','city':'salem'}


>>> c=d.copy()



>>> c
{'name': 'gopi', 'age': '21', 'city': 'salem'}

>>> d
{'name': 'gopi', 'age': '21', 'city': 'salem'}

>>> c==d
True

>>> c.clear()


>>> c
{}


>>> d.fromkeys.__doc__
'Create a new dictionary with keys from iterable and values set to value.'

>>> s={1,2,3,4,5,6,7,8}


>>> d.fromkeys(s)
{1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}

>>> d.fromkeys(s,'nonw')
{1: 'nonw', 2: 'nonw', 3: 'nonw', 4: 'nonw', 5: 'nonw', 6: 'nonw', 7: 'nonw', 8: 'nonw'}

>>> d.fromkeys(s)
{1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None}

>>> s={('name','gopi'),('age','21'),('city','salem')}

>>> s
{('city', 'salem'), ('age', '21'), ('name', 'gopi')}

>>> d.fromkeys(s)
{('city', 'salem'): None, ('age', '21'): None, ('name', 'gopi'): None}


>>> seq={'a','b','c','d','e'}

>>> list=[2,3]

>>> d=dict.fromkeys(seq,list)


>>> d
{'c': [2, 3], 'b': [2, 3], 'e': [2, 3], 'd': [2, 3], 'a': [2, 3]}

>>> list.append(4)


>>> d=dict.fromkeys(seq,list)


>>> d
{'c': [2, 3, 4], 'b': [2, 3, 4], 'e': [2, 3, 4], 'd': [2, 3, 4], 'a': [2, 3, 4]}



>>> seq={'a','b','c','d','e'}

>>> lis1=[2,3]


>>> d
{'c': [2, 3, 4], 'b': [2, 3, 4], 'e': [2, 3, 4], 'd': [2, 3, 4], 'a': [2, 3, 4]}


>>> d.get('c')
[2, 3, 4]

>>> d.get('b')
[2, 3, 4]

>>> d={'name':'gopi','age':'21','city':'salem'}


>>> d.items()
dict_items([('name', 'gopi'), ('age', '21'), ('city', 'salem')])

>>> s=d.items()


>>> s
dict_items([('name', 'gopi'), ('age', '21'), ('city', 'salem')])


>>> d
{'name': 'gopi', 'age': '21', 'city': 'salem'}

>>> d.items()

dict_items([('name', 'gopi'), ('age', '21'), ('city', 'salem')])

>>> del d['name']


>>> d
{'age': '21', 'city': 'salem'}

>>> item=d.items()

>>> item
dict_items([('age', '21'), ('city', 'salem')])




>>> item
dict_items([('age', '21'), ('city', 'salem')])

>>> d1={'name':'gopi'}

>>> d2={'age':'21'}

>>> d1.update(d2)

>>> d1
{'name': 'gopi', 'age': '21'}


>>> d
{'age': '21', 'city': 'salem'}

>>> d.update({'age':22})

>>> d
{'age': 22, 'city': 'salem'}

>>> d.get('name')

>>> d
{'age': 22, 'city': 'salem'}

>>> d.get('city')
'salem'


>>> d.items()
dict_items([('age', 22), ('city', 'salem')])

>>> d.keys()
dict_keys(['age', 'city'])


>>> d.pop('age')
22

>>> d.popitem()
('city', 'salem')


>>> d
{}




>>> d.setdefault('name','gopi')
'gopi'

>>> d
{'name': 'gopi'}

>>> d.setdefault('name','gopi')
'gopi'

>>> d
{'name': 'gopi'}

>>> d.setdefault('namew','gopiw')
'gopiw'

>>> d
{'name': 'gopi', 'namew': 'gopiw'}

>>> d
{'name': 'gopi', 'namew': 'gopiw'}

>>> d.setdefault('name','gopi')
'gopi'



>>> d
{'name': 'gopi', 'namew': 'gopiw'}


>>> d.popitem()
('namew', 'gopiw')


>>> d.values
<built-in method values of dict object at 0x0000026B66A49580>


>>> d={'name':'gopi','age':'21','city':'salem'}

>>> d2={'name':"satish",'eduction':'BE'}

>>> d.update(d2)

>>> d
{'name': 'satish', 'age': '21', 'city': 'salem', 'eduction': 'BE'}





>>> new = type('New', (object, ),
      dict(var1 ='GeeksforGeeks', b = 2009))

>>> new
<class '__main__.New'>



>>> new = type('New', (object, ),
      dict(var1 ='GeeksforGeeks', b = 2009))

>>> new = type('New', (object, ),dict(var1 ='GeeksforGeeks', b = 2009))


>>> new = type('New', (object, ),dict(var1 ='GeeksforGeeks', b = 2009))



>>> new=type('string',(object,),dict(name='gopi'))


>>> d
{'name': 'satish', 'age': '21', 'city': 'salem', 'eduction': 'BE'}
