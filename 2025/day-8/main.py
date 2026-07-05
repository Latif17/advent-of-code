from math import sqrt

def part1(arr):    
    routes = []
    for i in range(len(arr)):
        x2, y2, z2 = arr[i][0], arr[i][1], arr[i][2]
        for j in range(i + 1, len(arr)):
            x1, y1, z1 = arr[j][0], arr[j][1], arr[j][2]
            d = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            routes.append((d, (x1, y1, z1), (x2, y2, z2)))

    routes.sort()
    
    circuits = []
    junction_position = {}

    for _, pos1, pos2 in routes[:1000]:
        print(pos1, pos2)
        if pos1 in junction_position and pos2 in junction_position:
            index_one = junction_position[pos1]
            index_two = junction_position[pos2]
            if index_one != index_two:
                print("merge", index_one, junction_position[pos2])
                circuits[index_one].update(circuits[index_two])
                for pos in circuits[index_two]:
                    junction_position[pos] = index_one
                circuits[index_two].clear()
            else:
                print("exists in same circuit")
        elif pos1 in junction_position:
            print("add to", junction_position[pos1])
            circuits[junction_position[pos1]].add(pos2)
            junction_position[pos2] = junction_position[pos1]
        elif pos2 in junction_position:
            print("add to", junction_position[pos2])
            circuits[junction_position[pos2]].add(pos1)
            junction_position[pos1] = junction_position[pos2]
        else:
            print("new", len(circuits))
            circuits.append(set([pos1, pos2]))
            junction_position[pos1] = len(circuits) - 1
            junction_position[pos2] = len(circuits) - 1

    
    len_circutes =  []
    for circuit in circuits:
        if len(circuit) > 0:
            len_circutes.append(len(circuit))
    
    len_circutes.sort()

    print(len_circutes[-1] * len_circutes[-2] * len_circutes[-3])



    
        


        
if __name__ == "__main__":
    with open("./input.txt", 'r') as file:
        lines = [[int(c.strip()) for c in line.split(",")] for line in file if line.strip()]
    part1(lines)
