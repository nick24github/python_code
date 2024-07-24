#Ques-1: What is the output?
print(10.3//3) # Output: 3.0
print(10//3.0) # Output: 3.0

#Ques-2: Guess the output?
num = 2E3 # it is exponential representation it comes in float data type .
print(type(num))#<class>float
print(num)

#Ques-3: Guess the output?
# for i in 765<1:
    # print(i) # it will give type error

#Ques-4: What is Ternary Operator in programming?
# What is Ternary Operator in python?
# -------Types of Operators---------
# Unary Operator: works on 1 operand
# Binary Operator: works on 2 operand
# Ternary Operator: works on 3 operand

# Ques-5: What is PEP8?
# Stant for Python Interprise Proposal
# ------------OR-----------
# Python Enhancement Proposal
# A document that provides guidelines and best practices on how to write Python code.
# It was written in 2001 by Guido Van Rossum.
# These guidelines are helpful to enhance the readability and consistency of programs.

# Ques-6: What is a Walrus Operator? (:=)
# By using this operation we can assign a value within an expression.
print((a:=100)+1)
# Example-2
data = [10,20,30,40,50,60]
i = -1
while (i:=i+1)<(n:=len(data)):
    print(data[i])
# Example-3
# data1 = [10,20,30,40,50,60]
# n = len(data1)
# while n>0:
#     print(data1.pop())
#     n-=1
# print(data1)
data1 = [10,20,30,40,50,60]
while (n:=len(data1))>0:
    print(data1.pop())
    n-=1
print(data1)
# Example-4
# while True:
#     ans = input("Do you want to continue(y/n):").lower()
#     if ans!='y':
#         break
#     print("process the request")
while (ans:=input("Do you want to continue(y/n) ").lower())=='y':
    print("process the request")
