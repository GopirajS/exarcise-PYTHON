>>> # listoof comprehension

>>> s=[]   # empyt list

>>> for i in range(21):
	if i%2==0:
		s.append(i)

		
>>> s
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

>>> for i in range(21):
	if i%2!=0:
		s.append(i)

		
>>> s
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


>>> [x for x in range(21) if x%2==0]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

>>> [x+1 for x in range(21) if x%2==0]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

>>> [str(x) for x in range(21) if x%2==0]
['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20']

>>> names = ['Steve', 'Bill', 'Ram', 'Mohan', 'Abdul']

>>> [s for s in names if 's' in s]
[]

>>> [s for s in names if 'a' in s]
['Ram', 'Mohan']

>>> [s for s in names if 'e' in s]
['Steve']


>>> n1=[1,2,3,4]

>>> n2=[5,6,7,8]

>>> [(x,y) for x in n1 for y in n2]
[(1, 5), (1, 6), (1, 7), (1, 8), (2, 5), (2, 6), (2, 7), (2, 8), (3, 5), (3, 6), (3, 7), (3, 8), (4, 5), (4, 6), (4, 7), (4, 8)]

>>> n1=[1,2,3]

>>> n2=[5,6,7]

>>> [(x,y) for x in n1 for y in n2]
[(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]

>>> [(x,y) for x in n2 for y in n1]
[(5, 1), (5, 2), (5, 3), (6, 1), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3)]

>>> [x for x in range(21) if x%2==0 if x%3==0 ]
[0, 6, 12, 18]


>>> [x for x in range(21) if x%2==0 ]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


>>> [('even',x) for x in range(21) if x%2==0]
[('even', 0), ('even', 2), ('even', 4), ('even', 6), ('even', 8), ('even', 10), ('even', 12), ('even', 14), ('even', 16), ('even', 18), ('even', 20)]

>>> [('even',x) for x in range(18) if x%2==0]
[('even', 0), ('even', 2), ('even', 4), ('even', 6), ('even', 8), ('even', 10), ('even', 12), ('even', 14), ('even', 16)]

>>> [('even',x) for x in range(15) if x%2==0]
[('even', 0), ('even', 2), ('even', 4), ('even', 6), ('even', 8), ('even', 10), ('even', 12), ('even', 14)]

>>> [('even',x) for x in range(10) if x%2==0]
[('even', 0), ('even', 2), ('even', 4), ('even', 6), ('even', 8)]



>>> [str(x)+'=even' if x%2==0 else str(x)+'=odd' for x in range(10)]
['0=even', '1=odd', '2=even', '3=odd', '4=even', '5=odd', '6=even', '7=odd', '8=even', '9=odd']


>>> for i in [str(x)+'=even' if x%2==0 else str(x)+'=odd' for x in range(10)]:
	i

	
'0=even'
'1=odd'
'2=even'
'3=odd'
'4=even'
'5=odd'
'6=even'
'7=odd'
'8=even'
'9=odd'

>>> d=[str(x)+'=even' if x%2==0 else str(x)+'odd' for x in range(10)]

>>> for i in d:
	i
	
'0=even'
'1odd'
'2=even'
'3odd'
'4=even'
'5odd'
'6=even'
'7odd'
'8=even'
'9odd'

>>> matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


>>> [num for row in matrix for num in row]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> s=[1,2,3,[4,5,6],[7,8,9,[10,11,12]]]

>>> for i in s:
	i

	
1
2
3
[4, 5, 6]
[7, 8, 9, [10, 11, 12]]




>>> nestedlist = [ [1, 2, 3, 4], ["Ten", "Twenty", "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]



>>> for i in nestedlist:
	for j in i:
		print(j)

		
1
2
3
4
Ten
Twenty
Thirty
1.1
10.0
(1+2j)
20.55
3.142



>>> [j for i in nestedlist for j in i]
[1, 2, 3, 4, 'Ten', 'Twenty', 'Thirty', 1.1, 10.0, (1+2j), 20.55, 3.142]

