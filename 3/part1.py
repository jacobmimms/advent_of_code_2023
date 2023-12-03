with open('data.txt', 'r') as f:
    lines = [list(x.strip()) for x in f.readlines()]
    def is_symbol(x): return not x.isnumeric() and not x == '.'

    symbol_indices = []
    number_start_indices = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            current = lines[i][j]
            if current.isnumeric() and not (lines[i][j-1]).isnumeric():
                number_start_indices.append((i, j))
            if is_symbol(current):
                symbol_indices.append((i, j))

    def create_adjacent(i, j):
        return [(i+y, j+x) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]

    def adjacent_symbol(i, j):
        adjacent = create_adjacent(i, j)
        for item in adjacent:
            if item in symbol_indices:
                return True
        return False

    def get_number(i, j):
        number = lines[i][j]
        next = j+1
        while next < len(lines[0]) and (lines[i][next]).isnumeric():
            number += lines[i][next]
            next += 1
        return int(number)

    def check_adjacent_number(i, j, number):
        length = len(str(number))
        any_adjacent = True in [adjacent_symbol(i, j+x) for x in range(length)]
        return any_adjacent

    sum = 0
    for (i, j) in number_start_indices:
        number = get_number(i, j)
        if check_adjacent_number(i, j, number):
            sum += number

    print(sum)
