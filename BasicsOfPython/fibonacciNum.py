#1)1st way to show fibonacci series

# prev1 = 0
# prev2 = 1

# for fibo in range(18):
#     newFibo = prev1 + prev2
#     print(newFibo)
#     prev1 = prev2
#     prev2 = newFibo

#)2nd way by using recursion

# print(0)
# print(1)
# count = 2

# def fibonacci(prev1, prev2):
#     global count
#     if count <= 19:
#         newFibo = prev1 + prev2
#         print(newFibo)
#         prev1 = prev2
#         prev2 = newFibo
#         count +=1
#         fibonacci(prev1, prev2)
#     else:
#         return
    
# fibonacci(0, 1)

#) nth fibonacci number series using recursion

def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1) + F(n-2)
print(F(19))