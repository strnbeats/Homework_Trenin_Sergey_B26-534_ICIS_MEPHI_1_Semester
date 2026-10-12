def get_ring_cells(layer, n, clockwise):
    low = layer
    high = n - 1 - layer
    if low == high:
        return [(low, low)]
    cells = []
    for col in range(low, high):
        cells.append((low, col))
    for row in range(low, high):
        cells.append((row, high))
    for col in range(high, low, -1):
        cells.append((high, col))
    for row in range(high, low, -1):
        cells.append((row, low))
    if not clockwise:
        first = cells[0]
        rest = cells[1:]
        rest.reverse()
        cells = [first] + rest
    return cells


def build_matrix(n):
    if n <= 0:
        return []
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    number = 1
    layers = (n + 1) // 2
    for layer in range(layers):
        clockwise = layer % 2 == 0
        cells = get_ring_cells(layer, n, clockwise)
        for row, col in cells:
            matrix[row][col] = number
            number += 1
    return matrix


def print_matrix(matrix):
    width = len(str(len(matrix) * len(matrix)))
    for row in matrix:
        line = ""
        for value in row:
            line += str(value).rjust(width + 1)
        print(line)


for size in (3, 4, 5):
    if size % 2 == 1:
        kind = "нечетный"
    else:
        kind = "четный"
    print("n =", size, "(" + kind + ")")
    print_matrix(build_matrix(size))
    print()