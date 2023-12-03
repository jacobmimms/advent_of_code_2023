with open('data.txt', 'r') as f:
    lines = [list(x.strip()) for x in f.readlines()]
    def is_gear(x): return x == '*'

    gear_indices = []
    number_start_indices = []
    number_index_id = {}
    id_to_number = {}

    def get_number(i, j):
        number = lines[i][j]
        next = j+1
        while next < len(lines[0]) and (lines[i][next]).isnumeric():
            number += lines[i][next]
            next += 1
        return int(number)

    def set_number_id(i, j, id):
        number_index_id[(i, j)] = id
        id_to_number[id] = get_number(i, j)
        next = j+1
        while next < len(lines[0]) and (lines[i][next]).isnumeric():
            number_index_id[(i, next)] = id
            next += 1
        return id

    id = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            current = lines[i][j]
            if current.isnumeric() and not (lines[i][j-1]).isnumeric():
                number_start_indices.append((i, j))
                set_number_id(i, j, id)
                id += 1
            if is_gear(current):
                gear_indices.append((i, j))

    # print(number_index_id)
    print(id_to_number)

    def create_adjacent(i, j):
        return [(i+y, j+x) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]

    def adjacent_number_product(i, j):
        adjacent = create_adjacent(i, j)
        number_ids = set()
        for item in adjacent:
            if item in number_index_id.keys():
                id = number_index_id[item[0], item[1]]
                number_ids.add(id)
        if len(list(number_ids)) != 2:
            return 0
        res = 1
        for id in list(number_ids):
            res *= id_to_number[id]
        return res

    sum = 0
    for (i, j) in gear_indices:
        sum += adjacent_number_product(i, j)

    print(sum)
