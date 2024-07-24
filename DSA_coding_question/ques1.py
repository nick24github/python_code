# A startup wants to expand their empire so the CEO decided to purchase a plot at various locations.
# He has already figured out some plots and now he is busy.so he wants that you will select some plot 
# that are square shaped.

# Write a code, to help your CEO for finding the all square shaped plot.

# Input: First line of input will have the total shortlisted plots by the CEO.
#         Second line represents N space saperated integers denoting the area of the plots.

# Output: Find out how many plots are their to build a new office.

# Exp:
# Input: 6
#         64, 16, 38, 81, 50, 100

# Output: 4

import math

def count_square_plots(total_plots, plot_areas):
    count = 0
    
    for area in plot_areas:
        if math.isqrt(area) ** 2 == area:  # Check if area is a perfect square
            count += 1
    
    return count

# Example usage:
if __name__ == "__main__":
    total_plots = int(input().strip())  # Read total number of plots
    plot_areas = list(map(int, input().strip().split()))  # Read plot areas as integers
    
    result = count_square_plots(total_plots, plot_areas)
    print(result)

