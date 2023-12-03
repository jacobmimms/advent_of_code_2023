from functools import reduce

with open('values.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lookup = {
        'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
    }
    newlines = []
    for line in lines:
        newline = line
        for (k, v) in lookup.items():
            newline = newline.replace(k, v)
        newlines.append(newline)
    # print(newlines)
    print(reduce(lambda x, y: x+y, [int(line[min([x for x in [line.find(str(number))
                                                              for number in range(0, 10)] if x >= 0])] + line[max([x for x in [line.rfind(str(number))
                                                                                                                               for number in range(0, 10)] if x >= 0])]) for line in newlines]))
