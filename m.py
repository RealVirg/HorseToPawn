ip = ""

with open('in.txt') as f:
    ip = f.read().split('\n')


class Figure:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(dictionary[x])
        self.y = int(y)

    def __str__(self):
        return self.name + '(' + str(dictionary_2[self.x]) + ', ' + str(self.y) + ')'


def checker(point, v, p, c, pa):
    checkers = [(2, -1), (2, 1), (1, 2), (1, -2), (-2, -1), (-2, 1), (-1, 2), (-1, -2)]
    for check in checkers:
        b = (point[0] + check[0], point[1] + check[1])
        if (b not in v and 0 < point[0] < 9 and 0 < point[1] < 9
                and (point[0] + check[0] != pa.x + 1 and point[1] + check[1] != pa.y - 1)
                and (point[0] + check[0] != pa.x - 1 and point[1] + check[1] != pa.y - 1)):
            p.append(b)
            v.append(b)
            c[b] = point


def chain(point, c):
    a = [point]
    while c[point] != -1:
        a.append(c[point])
        point = c[point]
    a.reverse()
    return a


dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
dictionary_2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
horse = Figure('horse', ip[0][0], ip[0][1])
pawn = Figure('pawn', ip[1][0], ip[1][1])
print(horse)
print(pawn)
chaining_list = {(horse.x, horse.y): -1}
visited = [(horse.x, horse.y)]
pool = [(horse.x, horse.y)]

while len(pool) > 0:
    # print(pool)
    current = pool.pop()
    if current[0] == pawn.x and current[1] == pawn.y:
        print('good')
        answer = chain(current, chaining_list)
        print(answer)
        with open('out.txt', 'w') as f:
            for po in answer:
                f.write(dictionary_2[po[0]] + str(po[1]) + "\n")
        break
    checker(current, visited, pool, chaining_list, pawn)
print('bad')


