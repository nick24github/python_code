# You are given a set of numbers and you can arrange them in any order but this pays a penalty
# equal to the sum of the absolute difference between contiguous numbers

# You are needed to return the minimum penalty that should be paid 
# Input Format
# Input 1: Size of the array of integer number(2<input<10001)
# Input 2: Integer array(1<=input<=10000)

# Example 1:
# Input1: 3
# Input2: {1,3,2}
# Output: 2
def min_penalty(size, arr):
    if size < 2:
        return 0
    
    # Initialize the penalty array
    penalty = [[float('inf')] * 101 for _ in range(size)]
    
    # Base case: for the first element
    for j in range(101):
        penalty[0][j] = abs(arr[0] - j)
    
    # Fill the penalty array
    for i in range(1, size):
        for j in range(101):
            for k in range(101):
                penalty[i][j] = min(penalty[i][j], penalty[i-1][k] + abs(j - arr[i]))
    
    # Find the minimum penalty in the last row
    min_penalty = float('inf')
    for j in range(101):
        min_penalty = min(min_penalty, penalty[size-1][j])
    
    return min_penalty

# Example usage:
if __name__ == "__main__":
    size = 3
    arr = [1, 3, 2]
    print(min_penalty(size, arr))  # Output: 2