# Alex is given a number N. He has to check wheater the number is a Meta number or not.
#     Meta number are the numbers that are divisible by 1,2,4 and 8 but not by 10.
#     Your task is to find a number of Meta numbers in the range 1 to N.
    
#     Input Format:
#     The input consist of a single lines :
#     ->The line contains a single integer N.

def is_meta_number(num):
    # Check divisibility conditions
    if num % 1 == 0 and num % 2 == 0 and num % 4 == 0 and num % 8 == 0 and num % 10 != 0:
        return True
    return False

def count_meta_numbers(N):
    count = 0
    for i in range(1, N + 1):
        if is_meta_number(i):
            count += 1
    return count

# Taking input from user
N = int(input().strip())

# Counting meta numbers in the range 1 to N
result = count_meta_numbers(N)

# Output the result
print(result)