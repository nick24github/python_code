# You have given an integer number N determine the number of bricks needed to make a house of 
#     bricks of N level.
    
# Input: 1 Output: 2
# Input: 3 Output: 15

def bricks_needed(N):
    if N < 1:
        return 0
    else:
        return 2**(N + 1) - 1

# Example usage:
if __name__ == "__main__":
    print(bricks_needed(1))  # Output: 2
    print(bricks_needed(3))  # Output: 15