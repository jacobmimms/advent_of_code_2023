from functools import reduce
with open('data.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

    sum = 0

    def red(x, y): return x and y

    for line in lines:
        lims = {'red': 0, 'green': 0, 'blue': 0}

        def g(x):
            # takes color, pair string e.g. "10 blue"
            num, color = x.split(' ')
            if (int(num) > lims[color]):
                lims[color] = int(num)
        [_id, rest] = line.split(':')
        runs = rest.split(';')
        res = [[g(x.strip()) for x in y.split(',')]
               for y in rest.split(';')]
        # print(res)
        print(lims)
        res = lims['red'] * lims['green'] * lims['blue']
        sum += res
    print(sum)
