with open("./input.txt") as inputfile:
    banks = []
    for line in inputfile:
        banks.append(line.strip())

total = 0
for bank in banks:
    if len(bank) < 12:
        total += int(bank)
    arr = ""
    p1 = 0
    while p1 < len(bank) and len(arr) < 12:
        cell = int(bank[p1])
        items_needed = 12 - len(arr)
        for j in range(p1 + 1, len(bank)):
            comp = int(bank[j])
            items_available = len(bank) - j
            if comp > cell and items_available >= items_needed:
                cell = comp
                p1 = j
        p1 += 1
        arr += str(cell)
    total += int(arr)
print(total)
