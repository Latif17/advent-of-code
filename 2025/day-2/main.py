total = 0
with open("./input.txt") as inputfile:
    content = inputfile.read().strip()
    arr = content.split(",")


for val in arr:
    lim = val.split("-")

    lower = int(lim[0])
    higher = int(lim[1])

    start_len = len(str(lower))
    end_len = len(str(higher))

    ids_found = set()

    for length in range(start_len, end_len + 1):
        for k in range(1, (length // 2) + 1):
            if length % k != 0:
                continue

            N = length // k
            
            start_base = 10**(k - 1)
            end_base = 10**k
            
            multiplier = sum(10**(i * k) for i in range(N))
            
            for base in range(start_base, end_base):
                generated_val = base * multiplier

                if generated_val > higher:
                    break
                    
                if generated_val >= lower:
                    ids_found.add(generated_val)

    total += sum(ids_found)
print(total)

