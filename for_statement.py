Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> #  for
>>> l=[1,2,3,4,5,6,7,8]
>>> for i in l:
	print(i)

	
1
2
3
4
5
6
7
8
>>> t=(1,2,3,4,5,6)
>>> for i in t:
	print(i)

	
1
2
3
4
5
6
>>> name='gopiraj'
>>> for i in name:
	print(i)

	
g
o
p
i
r
a
j
>>> 
>>> 
>>> d={'name':}
SyntaxError: invalid syntax
>>> 
>>> d={'name':'gopi','age':'21'}
>>> for i in d:
	print(i)

	
name
age
>>> for i in d.items():
	print(i)

	
('name', 'gopi')
('age', '21')
>>> d.values()
dict_values(['gopi', '21'])
>>> for i in d.values():
	print(i)

	
gopi
21
>>> 
>>> 
>>> for i in range(10):
	print(i,end=' ')

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(10):
	if i==5:
		break
	print(i)

	
0
1
2
3
4
>>> for i in range(10):
	if i==5:
		continue
	print(i)

	
0
1
2
3
4
6
7
8
9
>>> 
>>> 
>>> if True:
	print('hi')
else:
	print('hellow')

	
hi
>>> for i in range(2):
	print('hi')
else:
	print('hellow')

	
hi
hi
hellow

>>> for i in  range(10):
	for j in range(i):
		print('i=',i,'j=',j)

		
i= 1 j= 0
i= 2 j= 0
i= 2 j= 1
i= 3 j= 0
i= 3 j= 1
i= 3 j= 2
i= 4 j= 0
i= 4 j= 1
i= 4 j= 2
i= 4 j= 3
i= 5 j= 0
i= 5 j= 1
i= 5 j= 2
i= 5 j= 3
i= 5 j= 4
i= 6 j= 0
i= 6 j= 1
i= 6 j= 2
i= 6 j= 3
i= 6 j= 4
i= 6 j= 5
i= 7 j= 0
i= 7 j= 1
i= 7 j= 2
i= 7 j= 3
i= 7 j= 4
i= 7 j= 5
i= 7 j= 6
i= 8 j= 0
i= 8 j= 1
i= 8 j= 2
i= 8 j= 3
i= 8 j= 4
i= 8 j= 5
i= 8 j= 6
i= 8 j= 7
i= 9 j= 0
i= 9 j= 1
i= 9 j= 2
i= 9 j= 3
i= 9 j= 4
i= 9 j= 5
i= 9 j= 6
i= 9 j= 7
i= 9 j= 8


>>> for i in  range(5):
	for j in range(i):
		print('i=',i,'j=',j)

		
i= 1 j= 0
i= 2 j= 0
i= 2 j= 1
i= 3 j= 0
i= 3 j= 1
i= 3 j= 2
i= 4 j= 0
i= 4 j= 1
i= 4 j= 2
i= 4 j= 3


>>> for i in range(1,7):
	for j in range(i):
		print(i)

		
1
2
2
3
3
3
4
4
4
4
5
5
5
5
5
6
6
6
6
6
6
>>> for i in range(1,7):
	for j in range(i):
		print(i,end=' ')

		
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 



>>> for i in range(1,7):
	for j in range(i):
		print(i,end=' ')
	print('\n')

	
1 

2 2 

3 3 3 

4 4 4 4 

5 5 5 5 5 

6 6 6 6 6 6 



>>> for i in range(5,0,-1):
	for j in range(i):
		print(i,end=' ')
	print('\n')

	
5 5 5 5 5 

4 4 4 4 

3 3 3 

2 2 

1 

>>> n=0
>>> for i in range(5,0,-1):
	n+=1
	for j in range(i):
		
		print(n,end=' ')
	print('\n')

	
1 1 1 1 1 

2 2 2 2 

3 3 3 

4 4 

5 



>>> for i in range(1,7):
	for j in range(i):
		print(j,end=' ')
	print('')

	
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 
0 1 2 3 4 5 




>>> for i in range(1,7):
	for j in range(1,i):
		print(j,end=' ')
	print(' \n')

	
 

1  

1 2  

1 2 3  

1 2 3 4  

1 2 3 4 5  

>>> for i in range(5,0,-1):
	for j in range(i):
		print(i,end=' ')
	print('\n')

	
5 5 5 5 5 

4 4 4 4 

3 3 3 

2 2 

1 
>>> for i in range(0,7):
	for j in range(i,0,-1):
		print(j,end=' ')
	print(' \n')

	
 

1  

2 1  

3 2 1  

4 3 2 1  

5 4 3 2 1  

6 5 4 3 2 1  

>>> for i in range(6):
	print(i)

	
0
1
2
3
4
5

>>> for i in range(6):
	print(i,end=' ')

	
0 1 2 3 4 5 
>>> for i in range(6,0,-1):
	for j in range(0,i,1):
		print(j,end=' ')
	print('\n')

	
0 1 2 3 4 5 

0 1 2 3 4 

0 1 2 3 

0 1 2 

0 1 

0 

>>> for i in range(10):
	print(i,end='')

	
0123456789
>>> for i in range(10):
	print(i,end=' ')

	
0 1 2 3 4 5 6 7 8 9 

>>> c=0
>>> step=2
>>> for i in range(3):
	for j in range(1,step):
		print(c,end=' ')
		c+=1
	print('')
	step+=2

	
0 
1 2 3 
4 5 6 7 8 


>>> for i in range(5):
	print('gopi')

	
gopi
gopi
gopi
gopi
gopi

>>> words = ['cat', 'window', 'defenestrate']

>>> for i in words:
	print(i)

	
cat
window
defenestrate

>>> for i in words:
	print(i,len(i))

	
cat 3
window 6
defenestrate 12
>>> 
>>> 
>>> d={'name':'gopi','age':'21','city':'salem'}
>>> for x,y in d.items():
	print(x,y)

	
name gopi
age 21
city salem
>>> for i in d:
	i

	
'name'
'age'
'city'
>>> 
>>> 
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> 
>>> for i in range(len(a)):
	print(i,a[i])

	
0 Mary
1 had
2 a
3 little
4 lamb
>>> for i in range(len(a)):
	print(len(a[i]),a[i])

	
4 Mary
3 had
1 a
6 little
4 lamb

>>> # table

>>> n=5

>>> for i in range(1,11):
	print(i,'x',n,'=',n*i,end=' ')

	
1 x 5 = 5 2 x 5 = 10 3 x 5 = 15 4 x 5 = 20 5 x 5 = 25 6 x 5 = 30 7 x 5 = 35 8 x 5 = 40 9 x 5 = 45 10 x 5 = 50 
>>> for i in range(1,11):
	print(i,'x',n,'=',n*i)

	
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50

>>> n=6

>>> for i in range(1,11):
	print(i,'x',n,'=',n*i)

	
1 x 6 = 6
2 x 6 = 12
3 x 6 = 18
4 x 6 = 24
5 x 6 = 30
6 x 6 = 36
7 x 6 = 42
8 x 6 = 48
9 x 6 = 54
10 x 6 = 60

>>> for i in range(1,11):
	print(i ,' x ',n,'=',n*i)

	
1  x  6 = 6
2  x  6 = 12
3  x  6 = 18
4  x  6 = 24
5  x  6 = 30
6  x  6 = 36
7  x  6 = 42
8  x  6 = 48
9  x  6 = 54
10  x  6 = 60

>>> for i in range(7):
	print(i,)

	
0
1
2
3
4
5
6
>>> for i in range(7):
	print(i,)
else:
	print('else part')

	
0
1
2
3
4
5
6
else part
>>> for i in range(7):
	print(i,)
else:
	print(i)

	
0
1
2
3
4
5
6
6
