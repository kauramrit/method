#Q.1- Reverse the whole list using list methods.

a=int(input("enter total no u want in list"))
b=[]
for i in range(a):
    c=int(input("enter those no"))
    b.append(c)
# 1st method using reverse:
b.reverse()
print(b)
# 2nd method using slice operator:
b[: : -1]
print(b)

#Q.2- Print all the uppercase letters from a string.

a=input("enter string")
for i in a:
    if i>='A' and i<='Z':
        print(i)

#Q.3- Split the user input on comma's and store the values in a list as integers.

a=input("enter no")
b=a.split(',')
c=[]
for i in b:
    c.append(int(i))
print(c)

#Q.4- Check whether a string is palindromic or not.

a=input("enter string")
b=a[::-1]
print(b)
if(a==b):
    print("string is palindrome")
else:
    print("string is not palindrome")

#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.

import copy as c
#DEEP COPY:-
#in deep copy any changes made to the copy of object do not reflect in the original object.
#example:
l1=[2,4,[9,7],5]
l2=c.deepcopy(l1)
l1[2][0]='amrit'
print(l1)
print(l2)
#SHALLOW COPY:-
#in shallow copy any changes made to the copy of object get reflected in the original object.
#example:
list1=[1,2,[4,5],7]
list2=c.copy(list1)
list1[2][0]='amrit'
print(list1)
print(list2)

