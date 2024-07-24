# Given an array A[] of positive integer f size N , where each value represent the number of 
# Chocolates in a packet. Each packet can have a variable number of chocolates. There are N students
# the task is to distribute chocolate packets among M students such that:
# Each students get exactly one packet.
# The differece between maximum number of chocolates given to a student and minimum number of
# chocolates given to a student is minimum.

# Example 1: Input:
#            N = 8, M = 5
#            A = {3, 4, 1, 9, 56, 7, 9, 12}
#            Output:
#            Explanation : The minimum difference between maximum chocolates and minimum chocolates
#            is 9 - 3 = 6 by choosing following M packets:{3, 4, 9, 7, 9}.

# Example 2: Input:
#            N = 7, M = 3
#            A = {7, 3, 2, 4, 9, 12, 56}
#            Output: 2

def findMinDifference(A, N, M):
    # Sort the array A
    A.sort()
    
    # Initialize the minimum difference
    min_diff = float('inf')
    
    # Traverse through the array A and find the subarray of size M
    for i in range(N - M + 1):
        current_diff = A[i + M - 1] - A[i]
        if current_diff < min_diff:
            min_diff = current_diff
    
    return min_diff

# Example usage:
N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]
print("Minimum difference:", findMinDifference(A, N, M))  # Output: 6

N = 7
M = 3
A = [7, 3, 2, 4, 9, 12, 56]
print("Minimum difference:", findMinDifference(A, N, M))  # Output: 2