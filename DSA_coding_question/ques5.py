# There are n farmers in an area. Each farmers owns 'X' number of land. Find the sum of lands
#    owned by all the farmers (1 based indexing), The number of land 'X' is the xor operation of
#    the land owner by his  previous farmer and his number.
   
#    Input Format : One line consist of 'N' which represents the number of farmer in the given 
#    area.
   
#    Output Format : Print total number of lands owned by n farmer.
   
#    Testcase:
#    i) n=1
#    Output--> 1
   
#    ii) n=3
#    Output--> 4
def total_lands_owned(n):
    total_lands = 0
    X = 0  # Initial value of X for the first farmer
    for i in range(1, n + 1):
        X = X ^ i  # Compute X using XOR with the current farmer's number i
        total_lands += X  # Add current X to the total lands owned
    
    return total_lands

# Example usage:
n = int(input().strip())
result = total_lands_owned(n)
print(result)