#Question1

t1=(3,56,34,23,69,'true',64,89,'true',35.4,6,)
print('tuple',t1)
t1=set(t1)
t2=tuple(t1)
print('removing duplicates',t1)

#Question2
print("-------------------------------------------")
l1=[[2,3,4],[5,7,6],[9,8,10]]
l2=[i for j in l1 for i in j]
print('flattened list',l2)

#Question3
print("-------------------------------------------")    
t2=(3,5,8,22,10,88,65,47,9,12,11)

t2=sorted(t2)
print('minimum value:',t2[0])
print('maximum value:',t2[-1])

#Question4
print("-------------------------------------------")
l2=[(i,i**3)for i in range(1,6)]
print('tuple of numbers and their cubes:',l2)
