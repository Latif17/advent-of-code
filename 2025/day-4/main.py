with open("./input.txt") as inputfile:
    arr = []
    for line in inputfile:
        curr = []
        content = line.strip()
        for pos in content:
            curr.append(pos)
        arr.append(curr)
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1), # Top-left, Top, Top-right
        ( 0, -1),          ( 0, 1), # Left, Right
        ( 1, -1), ( 1, 0), ( 1, 1)  # Bottom-left, Bottom, Bottom-right
    ]

    rows = len(arr)
    cols = len(arr[0])
    total_removed = 0
    
    while True:
        removed = 0
        removed_pos = []
        for r in range(rows):
            for c in range(cols):
                curr = arr[r][c]
                if curr == ".":
                    continue
                count = 0

                for dr, dc in directions:
                    nr = r + dr 
                    nc = c + dc 
                    
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if arr[nr][nc] == '@' or arr[nr][nc] == 'x':
                            count += 1
                    
                    if count >= 4:
                        break

                if count < 4:
                    arr[r][c] = 'x'
                    removed_pos.append((r, c))
                    removed += 1
        if removed == 0:
            break
        total_removed += removed
        for r, c in removed_pos:
            arr[r][c] = "."
    print(arr)
    print(total_removed)
