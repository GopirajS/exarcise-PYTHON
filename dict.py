Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # dictionary

>>> d={}

>>> type(d)
<class 'dict'>

>>> d={'name':'sathish','city':'mumbai'}

>>> d={"USA":'washington DC','france':'paris','india':'new delhi'}


>>> item={1:'one',2:'two',3:'tree',4:'four'}

>>> num={1.5:'one and half',2.5:'two and half',3.5:'tree and half'}

>>> item={('parker','reynald','camlin'):'pen',('LG','whirpool','samsng'):'refrigirator'}

>>> item={'fruits':('apple','oringe'),'colore':('red','green')}

>>> d={"USA":'washington DC','france':'paris','india':'new delhi'}

>>> d['USA']
'washington DC'

>>> d
{'USA': 'washington DC', 'france': 'paris', 'india': 'new delhi'}


>>> d.items()
dict_items([('USA', 'washington DC'), ('france', 'paris'), ('india', 'new delhi')])

>>> for i in d.items():
	
('USA', 'washington DC')
('france', 'paris')
('india', 'new delhi')

>>> d['paris']
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d['paris']
KeyError: 'paris'

>>> d['france']
'paris'

>>> d['india']
'new delhi'

>>> d.get('india')
'new delhi'

>>> d.get('usa')

>>> d
{'USA': 'washington DC', 'france': 'paris', 'india': 'new delhi'}

>>> d.get('USA')
'washington DC'

>>> d={"USA":'washington DC','france':'paris','india':'new delhi'}

>>> for key in d:
	print('key',key,"is value", d[key])

	
key USA is value washington DC
key france is value paris
key india is value new delhi


>>> d={"USA":'washington DC','france':'paris','india':'new delhi'}

>>> d['india']='gopi'

>>> d
{'USA': 'washington DC', 'france': 'paris', 'india': 'gopi'}
>>> 

>>> d['southafrica']='plessing'

>>> d
{'USA': 'washington DC', 'france': 'paris', 'india': 'gopi', 'southafrica': 'plessing'}

>>> d.keys()
dict_keys(['USA', 'france', 'india', 'southafrica'])

>>> captains = {'England': 'Root', 'Australia': 'Paine', 'India': 'Virat', 'Srilanka': 'Jayasurya'}

>>> del captains['Srilanka']

>>> captains
{'England': 'Root', 'Australia': 'Paine', 'India': 'Virat'}

>>> captains.keys()
dict_keys(['England', 'Australia', 'India'])

>>> captains.values()
dict_values(['Root', 'Paine', 'Virat'])

>>> 'England' in captains
True

>>> 'France' in captains
False

>>> "USA" not in captains
True

>>> captains = {'England': 'Root', 'Australia': 'Paine', 'India': 'Virat', 'Srilanka': 'Jayasurya'}



>>> captains = {'England': 'Root', 'Australia': 'Paine', 'India': 'Virat', 'Srilanka': 'Jayasurya'}

>>> d1={'name':'gopi','age':21,'mark':60}
    
>>> d2={'name':'sathish','age':13,'mark':40}

>>> d3={'name':'gopal','age':12,'mark':56}

>>> student={1:d1,2:d2,3:d3}

>>> student
{1: {'name': 'gopi', 'age': 21, 'mark': 60}, 2: {'name': 'sathish', 'age': 13, 'mark': 40}, 3: {'name': 'gopal', 'age': 12, 'mark': 56}}

>>> student[1]['age']
21

>>> d={"USA":'washington DC','france':'paris','india':'new delhi'}

>>> d['france']
'paris'

>>> d={"USA":'washington DC','france':('paris','india','landon'),'india':'new delhi'}

>>> d['france']
('paris', 'india', 'landon')

>>> d['france'][1]
'india'

>>> d['france'][0]
'paris'

>>> l=[1,2,3,'gopi']
>>> d={'name':'gopi','age':21}
>>> t=('python','java','c++')
>>> s={'apple','oringe','banana'}

>>> ide={1:l,2.5:d,'pro':t,('red','oringe','yellow'):s}

>>> ide
{1: [1, 2, 3, 'gopi'], 2.5: {'name': 'gopi', 'age': 21}, 'pro': ('python', 'java', 'c++'), ('red', 'oringe', 'yellow'): {'oringe', 'banana', 'apple'}}

>>> ide.get(1)
[1, 2, 3, 'gopi']

>>> ide.get(2.5)
{'name': 'gopi', 'age': 21}
>>> ide.get('pro')
('python', 'java', 'c++')

>>> ide.get('red')

