from math import sqrt

def part1(arr):
    # find shortet distance between two points
    for i in range(len(arr)):
        x2, y2, z2 = arr[i][0], arr[i][1], arr[i][2]
        shortest = float("inf")
        shortest_pos = None
        for j in range(i + 1, len(arr)):
            x1, y1, z1 = arr[j][0], arr[j][1], arr[j][2]
            d = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            if d < shortest:
                shortest = d 
                shortest_pos = j




if __name__ == "__main__":
    with open("./test.txt", 'r') as file:
        lines = [[int(c.strip()) for c in line.split(",")] for line in file if line.strip()]
    print(part1(lines))