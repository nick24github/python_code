#Q.1) What is docstring ?

# It is a string literal that appear right after the definition of function, class, module.

def add(n1, n2):
    """This is my function"""
    # '''This is also a docstring '''
    return n1+n2 
print(add.__doc__) # we can access the doc string by __doc__ attribute.

#Docstrings and purpose 

# Function :- arguments and return values.

# Class :- Attributes and methods

# Modules :- List of classes and functions

# Package :- List of modules with functionality


# Q.2) What is difference between comments and docstrings ?

# Comments are ignored by interpreter. But, docstring are not ignored.

# Memory is allocated for docstrings.

# Comments are description of code and docstrings are purpose of code.
