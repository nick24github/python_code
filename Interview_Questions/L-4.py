# Q.1)Input: "sky is blue"
#   Output: "blue is sky"
# str1="sky is blue"
# mylist = str1.split()
# print(mylist)
# mylist=mylist[::-1]
# print(mylist)
# str2 = " ".join(mylist)
# print(str2)

# In short

str1 = "sky is blue"
print(" ".join(str1.split()[::-1]))


# Q.2)Input:List=[1,2,2,3,3,4,5,5,5,6,6]
#   Output: [1,4]
List = [1,2,2,3,3,4,5,5,5,6,6]
new_list = []
for num in List:
    if List.count(num)==1:
        new_list.append(num)
print(new_list)

# by list comprehension
print([num for num in List if List.count(num)==1])

# Q.3)Input:mystr="a,a,a,b,b,c,c,c"
#   Output:-a:3,b:2,c:3
mystr="a,a,a,b,b,c,c,c"
mylist = mystr.split(',')
visited = []
final_list = []
# print(mylist)

for ch in mylist:
    if ch not in visited:
        final_list.append(f"{ch}:{mylist.count(ch)}")
        visited.append(ch)
print(final_list)
print(",".join(final_list))

