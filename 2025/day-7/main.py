
from functools import cache

def part_one(arr):
    count = 0 
    def path_finder(row, col):
        nonlocal count
        row += 1
        while arr[row][col] == "." and row < len(arr) - 1:
            arr[row][col] = "|"
            row += 1

        if row == len(arr):
            print(row)
            return 

        if arr[row][col] == "^":
            count += 1
            path_finder(row, col + 1)
            path_finder(row, col - 1)
    # find S
    i = 0
    while i < len(arr[0]):
        if arr[0][i] == "S":
            break
        i += 1
    
    path_finder(0, i)
    print(count)

def part_two(arr):
    @cache 
    def path_finder(row, col):
        row += 1
        
        while row < len(arr) and arr[row][col] == ".":
            row += 1

        if row == len(arr):
            return 1
            
        if arr[row][col] == "^":
            right_branch = path_finder(row, col + 1)
            left_branch = path_finder(row, col - 1)
            return right_branch + left_branch
        
        return 0

    try:
        i = arr[0].index("S")
    except ValueError:
        i = 0
    
    # Start the recursion (notice we no longer pass 'count=0')
    total_timelines = path_finder(0, i)
    return total_timelines


if __name__ == "__main__":
    with open("./input.txt", 'r') as file:
        lines = [[c for c in line.strip()] for line in file if line.strip()]
    print(part_two(lines))

    