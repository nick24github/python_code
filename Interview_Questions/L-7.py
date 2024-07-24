lang1 = ['marathi', 'hindi', 'gujrati', 'urdu']
lang2 = ['english', 'french', 'japanese']
# for l in lang2:
    # lang1.append(l)
# print(lang1)

# Instead of this we can use extent()
# extend() method is us to append multiple item in the current list, tuple, set , etc.
# syntax:- list1.extend(iterable)
# This method does not return any value rather modifies the list . Means, it returns 'None'.
lang1.extend(lang2)
print(lang1)

# Q.1)What is diff b/w append() and extend() in list?

# Q.2)How will you append multiple elements in list?

# ** List Comprehension :

# What is comprehension ?
# It is a way f writing compact code in python.
# For Exp:
lst = []
for i in range(1,4):
    for j in range(5,7):
        lst.append(i*j)
print(lst)
# You can write in 1 line
print([i*j for j in range(5,7) for i in range(1,4)])

# Type of Comprehension
# 1)List Comprehension
nums = [3,6,8,12,14,15]  #sq of all number of list
# Normal code
sq = []
for num in nums:
    sq.append(num*num)
print(sq)

# By List Comprehension :
# syntax-01:-Normal: [expression for variable in iterable]
print([num*num for num in nums])
# syntax-02:-If Condition: [expression for variable in iterable if condi]
print([num*num for num in nums if num%2==0])
# syntax-03:-Nested if: [expression for variable in iterable if condi-1 if condi-2]
print([num*num for num in nums if num%2==0 if num%3==0])
# syntax-04:-If-else: [expression if condi else expression for variable in iterable]
print([num*num if num%2==0 else num*num*num for num in nums])
#syntax-05:-Nested for:- [expression if condi else expression for var in iterable]
print([i*j for i in range(3,6) for j in range(5,7) ])

# Note :- Every comprehension code can be converted into normal code but every normal code can 
#           not be converted into comprehension code.
# Advantages:-
# Compact & elegant Code
# Less code 
# Fast execution
# Disadvantages:-
# Your code gets less readable.
# 2)Set Comprehension
# 3)Dictionary Comprehension