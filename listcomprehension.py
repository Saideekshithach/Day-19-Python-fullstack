#list comprehension
'''a=["codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]'''
#print(a.upper())
'''b=str(a)
print(b.upper())'''
'''for i in a:
print(i)'''
'''for i in a:
print(i.upper(),end=" ")'''
#syntax
#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

a=["python","java","ds"]
'''b=[i.capitalize() for i in a]
print(b)'''
'''b=[i.title() for i in a]
print(b)'''

'''a=[1,2,4,6,8,12,13]
c=[i**2 for i in a]
print(c)
c=[pow(i,2) for i in a]
print(c)
c=[i*i for i in a]
print(c)'''

#if usage in list comprehension
#even numbers
'''b=[i for i in range(21) if i%2==0]
print(b)'''
#odd numbers
'''a=[i for i in range(21) if i%2!=0]
print(a)'''

'''a=[i**2 for i in range(21) if i%2==0]
print(a)'''

a=["apple","banana","grapes","kiwi","dragon","blueberry"]
'''b=[i for i in a if 'a' in i]
print(b)'''

'''b=[i for i in a if 'a' not in i]
print(b)'''

#no elif usage in list comprehension

#if-else usage in list comprehension

b=[i**2 if i%2==0 else i*5 for i in range(16)]
print(b)







