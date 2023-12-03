from functools import reduce
print(reduce(lambda x, y: x+y, [int(line[min([x for x in [line.find(str(number))
                                                          for number in range(0, 10)] if x >= 0])] + line[max([x for x in [line.rfind(str(number))
                                                                                                                           for number in range(0, 10)] if x >= 0])]) for line in [line.strip() for line in open('values.txt', 'r').readlines()]]))
