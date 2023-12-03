from functools import reduce
with open('data.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

    sum = 0
    lims = {'red': 12, 'green': 13, 'blue': 14}

    def g(x): return not int(x.split(' ')[0]) > lims[x.split(' ')[1]]
    def red(x, y): return x and y

    def recRed(x):
        res = reduce(red, x)
        if type(res) == bool:
            return res
        else:
            return recRed(res)

    for line in lines:
        [_id, rest] = line.split(':')
        runs = rest.split(';')
        res = [recRed([g(x.strip()) for x in y.split(',')])
               for y in rest.split(';')]
        if res:
            sum += int(_id.split(' ')[1])
    print(sum)
