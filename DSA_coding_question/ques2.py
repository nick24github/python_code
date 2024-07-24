# A function accept an array and length , implement the function to find the maximum element 
# of array and print maximum element and its index .

# The maximum element and its index should be printed in next line.
# Condition:
# 1)Array index start with 0.
# 2)Maximum element and its index should be saperated by new line
# 3)Assume their is only 1 maximum element in array.

# Sample Input:
# Input: 1,2,3,4,5,6,7
# Output: 7
#         6
# Example 2: 23 45 82 71
# Output: 82
#         2

def find_max_element_and_index(arr):
    max_element = float('-inf')  # Initialize max_element to a very small number
    max_index = -1
    
    # Iterate through the array to find maximum element and its index
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i
    
    # Print maximum element and its index
    print(max_element)
    print(max_index)

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    find_max_element_and_index(arr)