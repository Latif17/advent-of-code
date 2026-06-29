
# take line seperatd input
# split by first char and val
# if val > 99 % 99 = val
# if diff to zero > val, start from 99
# if diff to right zero < val starts from 0


pos = 50
password_count = 0

with open("./input.txt") as inputfile:
    for line in inputfile:
        line = line.strip()
        if not line:
            continue

        dir, val = line[:1], int(line[1:])
        
        if dir == "R":
            password_count += (pos + val) // 100
            pos = (pos + val) % 100
        else:
            dist_to_first_zero = pos if pos != 0 else 100
            if val >= dist_to_first_zero:
                password_count += 1 + ((val - dist_to_first_zero) // 100)
            pos = (pos - val) % 100

        print(f"{pos=},{val=}, {dir=}, {password_count=}")

print(password_count)


















