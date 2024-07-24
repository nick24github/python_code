#--------------------------- Interview-Questions---------------------------
# Ques-1:
data = {} # use to create a empty dictionary.
print(type(data)) #Output: <class>dict
s = set() # use to create a empty set
print(type(s)) #Output: <class>set

# Ques-2:
print(-10//3) #Output: -4

#Ques-3: Print below statement:
#"""conversation - He said,"Shantanu's explanation is very good " and I subscribed channel"""
print('''"""conversation - He said,"Shantanu's explanation is very good " and I subscribed channel"""''')
#Or
print("\"\"\"conversation - He said,\"Shantanu\'s explanation is very good \" and I subscribed channel\"\"\"")

#Ques-4: What is the output?
print(2**3**2) #Exponential operator has heightest precedence of associativity .
#in thi case: Here is conflict in the of operator so the precedence will check right to left.

#Ques-5: Print the below statement:
# "python uses \n for newline"
print('\"python uses \\n for newline\"')

#Ques-6: Print below
# /\/\/\/\/\/\
print("/\\/\\/\\/\\/\\/\\")

#Ques-7: What is an Output?
# name = "shantanu"
#print(name[2:8:-2])
name = "shantanu"
print(name[2:8:-2])

#Ques-8:what's the output for below senario
# my_dict =  {"jay":89,"viru":81,'jay':52}
#print(len(my_dict))
my_dict =  {"jay":89,"viru":81,'jay':52} # in dict dublicate keys are not allow if we give 
# the same key again it will update the value in already existing key.
print(len(my_dict)) #Output : 2

#Ques-10:Merge three list:
# a=[1,4,7]
# b=[2,5,8]
# c=[3,6,9]
# output:[(1,4,7),(2,5,8),(3,6,9)] : for this we have to use zip() function.
a=[1,4,7]
b=[2,5,8]
c=[3,6,9]
d = list(zip(a,b,c))
print(d)
