# Question1 
l1=['comunity','tasks','bro','component','hat','comunication','mat']
l2=[i for i in l1 if len(i)<4]
print(l2)

#Question2
print("-------------------------------------------")
l3=[i for i in range(20)]
l4=['odd' if i % 2 != 0 else 'even' for i in l3]
print(l4)

#Question3
print("-------------------------------------------")
l5=[i for i in range(1,1001)]
l6=[i for i in l5 if i%7==0]
print(l6)

#Question4
print("-------------------------------------------")
l5=['I am a Ritish Thakur','I love to play football','I am a software engineer','but i dont like it']
spaces=0
for i in l5:
    spaces += i.count(' ')  
print("Total spaces:", spaces)

#Question5
print("-------------------------------------------")
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
list_c=[i for i in list_a for j in list_b if i == j]
print("Common elements", list_c)