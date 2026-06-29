with open("./input.txt") as inputfile:
    fresh_range = []
    available = []
    line_break = False
    for line in inputfile:
        curr = []
        content = line.strip()
        if content == "": 
            line_break = True 
            continue

        if line_break:
            available.append(int(content))
        else:
            lower, upper = content.split('-')
            fresh_range.append(tuple([int(lower), int(upper)]))


def find_count_of_fresh():
    count = 0

    for item in available:
        for lower, upper in fresh_range:
            if lower <= item <= upper:
                count += 1
                break

    print(count)

    # 

def get_count_of_fresh():
    print(fresh_range)
    fresh_range.sort(key=lambda x: x[0])

    merged = [list(fresh_range[0])]

    for curr in fresh_range[1:]:
        last_merged = merged[-1]
        if curr[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], curr[1])
        else:
            merged.append(list(curr))
    
    count = 0

    for lower, upper in merged:
        count += (upper - lower + 1)
    
    print(count)

            



get_count_of_fresh()
