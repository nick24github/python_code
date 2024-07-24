# Interview problems on dictionary

student = {'ajay':10000, 'raj':12000, 'vijay':14000}
keys_list = list(student.keys())
print(keys_list[-1], '-->', student[keys_list[-1]])

# convert list to string

list1 = ['A', 'B', 'C']
string = ":".join(list1)
print(string)

# join() :-
# The join() method takes all items in an iterable and joins them into one string.
# syntax :- "separator".join(iterable)
# Iterable :- object capable of returning it's member one at a time.
# Examples of iterables :- list, tuple, set, string

l =  ['p', 'y', 't', 'h', 'o', 'n']
print(''.join(l))

lang = {'java', 'python', 'c++'} # set is unordered collection of items. There is no specific order
lang1 = "-->".join(lang)
print(lang1)


# Split function :- 
# The split() method breaks up a string at specified separator and returns a list of strings.
# Syntax:- string.split(separator,maxsplit)
# separator :- separator for splitting string. Bydefault, whitespace is a separator.
# maxsplit :- How many splits to do.
msg = "i want to become python programmer"
words = msg.split()
print(len(words))
# print(words)
# print(msg.count)
countories = "india,pakistan,australia,srilanka,america,england"
coun_lst = countories.split(",",3)
print(coun_lst)
# print(len(coun_lst))
for country in coun_lst:
    print(country)


#Q.5) write a python program to reverse internal content of each word.
# input:- "python is easy"
# output:- "nohtyp si ysae" 

str1 = input("Enter the input :")
l = str1.split()
l1 = []
for word in l:
    #print(word[::-1]) # this is slicing approach to reverse the word or string
    l1.append(word[::-1])
output = " ".join(l1)
print(output)

# write a python program to print duplicates present in list

    
