Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fuction():
	print('hellow world')

	
>>> fuction()
hellow world
>>> 
>>> 
>>> def fuction(n):
	print('hellow world',name)

	
>>> fuction('gopi')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fuction('gopi')
  File "<pyshell#7>", line 2, in fuction
    print('hellow world',name)
NameError: name 'name' is not defined
>>> def fuction(n):
	print('hellow world',n)

	
>>> 
>>> fuction('gopi')
hellow world gopi
>>> fuction(n='gopi')
hellow world gopi

>>> 

>>> def fuction(*n):
	i=0
	print('hellow ',end='')
	while len(n)>i:
		print(n[i],end=' ')

		


>>> def fuction(*n):
	i=0
	print('hellow ',end='')
	while len(n)>i:
		print(n[i],end=' ')
		i+=1

		
>>> fuction('gopi','raj','sathish','kumar')
hellow gopi raj sathish kumar 

>>> def fuc(first,second):
	print('hellow',first,second)

	

>>> fuc(first='gopi',second='raj')
hellow gopi raj

>>> def fuct(**person):
	print('hellow',person[first],person[second])

	
>>> fuct(first='gopi',second='raj')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    fuct(first='gopi',second='raj')
  File "<pyshell#44>", line 2, in fuct
    print('hellow',person[first],person[second])
NameError: name 'first' is not defined

>>> def fuct(**person):
	print('hellow',person['first'],person['second'])

	
>>> fuct(first='gopi',second='raj')
hellow gopi raj


>>> def my_name(n):
	s='hellow ',n
	return s

>>> my_name('gopiraj')
('hellow ', 'gopiraj')

>>> def my_name(n):
	s='hellow ',n
	return s

>>> my_name('gopiraj')
('hellow ', 'gopiraj')
>>> 
>>> def my_name(n):
	return 'hellow'+ n

>>> my_name('gopiraj')
'hellowgopiraj'
>>> 
>>> 
>>> 
>>> def my_name(n):
	return 'hellow  '+ n

>>> my_name('gopiraj')
'hellow  gopiraj'
>>> 
>>> 
>>> 
>>> def my(d):
	if (d>0):
		result=d+my(k-1)
	else:
		result=0
	return result

>>> def my(d):
	if (d>0):
		result=d+my(d-1)
	else:
		result=0
	return result

>>> my(6)
21
>>> 