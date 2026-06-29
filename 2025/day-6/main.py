
def part_two(number_rows, operators):
    transposed = [list(row) for row in zip(*number_rows)]
    i = 0
    total = 0
    
    for operator in operators:
        all_space = False
        curr_total = 0
        if operator == "*":
            curr_total = 1
        while i < len(transposed):
            str_int = ""
            for c in transposed[i]:
                if c != " ":
                    str_int += c
            i += 1
            if len(str_int) == 0:
                break
            val_int = int(str_int)
            if operator == "*":
                curr_total *= val_int
            else:
                curr_total += val_int
        total += curr_total

    print(f"{total=}")
    # for j in range(len(transposed)):
    #     max_length = max(len(str(val)) for val in transposed[j])
    #     operation = operators[j]
    #     for i in range(len(transposed[j])):
    #         val = transposed[j][i]
    #         diff = max_length - len(str(val))
    #         if diff > 0: 
    #             to_add = diff * "0"
    #             if operation == "*":
    #                 transposed[j][i] = to_add + str(val)
    #             else: 
    #                 transposed[j][i] = str(val) + to_add

    #     calculation = [list(row)for row in zip(*transposed[j])]

    #     curr_total = 0
    #     if operation == "*":
    #         curr_total += 1

    #     for val in calculation:
    #         number = ""
    #         for num in val:
    #             if num != "0":
    #                 number = number + str(num)
    #         if operation == "*":
    #             curr_total *= int(number)
    #         else:
    #             curr_total += int(number)
    #     total += curr_total












if __name__ == "__main__":
    with open("./input.txt", 'r') as file:
        lines = [line for line in file if line.strip()]
        operators =  [val for val in lines[-1] if val != " "]
        number_rows = [[val for val in row[:-1]] for row in lines[:-1]]

    part_two(number_rows, operators)

    