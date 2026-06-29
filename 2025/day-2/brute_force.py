total = 0
with open("./input.txt") as inputfile:
    content = inputfile.read().strip()
    arr = content.split(",")


for val in arr:
    lim = val.split("-")

    lower = int(lim[0])
    higher = int(lim[1])
    
    for val in range(lower, higher + 1): # iterate through all ranges unneccesarily
        s_val = str(val)
        digits = len(s_val)
        if digits % 2 != 0:
            continue
        first, second = s_val[:digits // 2], s_val[digits // 2:]   
        if first == second:
            total += val


print(total)