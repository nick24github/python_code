# 4 part of python interview questions

# 1) Mostly Asked Question (10)

#  Q.1) What is diff b/w list and tuple ?
# --------------------------------------------
# LIST:
# 1)list is mutable.
# 2)list is a container to contain different type of objects and is used to iterate object.
# 3)Syntax: list = ['a', 'b', 'c',1, 2,3]
# 4)list iteration is slower.
# 5)list consumes more memory.
# 6)Operations like insertion, deletion, are better performed.

# TUPLE:
# 1)tuple is immutale.
# 2)tuple is also same is  list but contains immutable objects.
# 3)Syntax: tuple = ('a', 'b', 'c' ,1 , 2)
# 4)tuple processing is faster than list.
# 5)tuple consumes less memory.
# 6)Elements can be accessed better.

# Q.2)What is decorator. Explain it with an example.
# ---------------------------------------------------
# A Decorator is just a function that takes another function as an argument, add some kind of 
# functionality and then returns another functions.
# All of this without altering the source code of the original function that you passed in.
# Example:-

# Q.3)What is diff b/w list and dict (list comprehension and dict comprehension)
# -------------------------------------------------------------------------------
# LIST COMPREHENSION:
# Syntax: [expression for item in iterable if conditional]
# DICT COMPREHENSION:
# Syntax: {key:value for(key,value) in iterable if condition}
# Q.4)How memory managed in python ?
# ------------------------------------
# Private Heap Memory
# Space Allocation
# Python Memory Manager
# Definition:
# 1)Memory management in python involves a private heap containing all Python objects
# and data structures. Interpretrer takes care of Python heap and that the programmer 
# has no access to it.
# 2)The allocation of heap space for Python objects is done by
# Python memory manager. The core API of Python provides some tools for the 
# programmer to code reliable and more robust program.
# 3)Python also has a build-in garbage collector which recycles all the unused memory.
# When an object is no longer referenced by the program, the heap space it occupies can 
# be freed. The garbage collector determines objects which are no longer referenced by the
# program frees the occupied memory and make it available to the heap space.
# 4)The gc module defines functions to enable/disable garbage collector.
# gc.enable() - Enables automatic garbage collection.
# gc.disable() - Disables automatic garbage collection.

# Q.5)What is difference between Generator & Iterator ?
# ----------------------------------------------------
# GENERATOR:
# 1)Generators are iterators which can execute only once.
# 2)Generator uses "yield" keyword.
# 3)Generators are mostly used in loops to generate an iterator by returning all the values in the loop
# without affecting the iteration of the loop.
# 4)Every generator is an iterator.
# ITERATOR:
# 1)An iterator is an object which containes a countable number of values and it is used to iterate
# over iterable objects like list, tuples, sets, etc.
# 2)Iterators are used mostly to iterate or convert other objects to an iterator using iter() function. 
# 3)Iterators uses iter() and next() function.
# 4)Every iterator is not a generator.

# Q.6)What is init keyword in python ?
# 1)__init__.py file:
# The __init__.py file lets the Python interpreter know that a directory contains code for a
# Python module. It can be blank. without one, you can not import modules from another folder
# into your project.
# The role of the __init__.py file is similar to the __init__.py function in a python class.
# The file essentially the constructor of your package or directory without it being called 
# such. It sets up how packages or functions will be imported into your other files.

#2)__init__() function
# The __init__ method is similar to constructors in C++ and Java, Constructors are used to 
# initialize the objects state.  


# 2) Commonly Asked Question (20)
# 3) Tricky Questions (10)
# 4) Advance Questions (12)