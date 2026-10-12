def find_symbol(maze, symbol):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == symbol:
                return row, col
    return None


def solve_maze(maze):
    start = find_symbol(maze, "S")
    end = find_symbol(maze, "E")
    if start is None or end is None:
        return False, None
    distances = []
    for row in maze:
        distances.append([-1] * len(row))
    distances[start[0]][start[1]] = 0
    queue = [start]
    head = 0
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while head < len(queue):
        row, col = queue[head]
        head += 1
        if (row, col) == end:
            return True, distances[row][col]
        for d_row, d_col in moves:
            new_row = row + d_row
            new_col = col + d_col
            if new_row < 0 or new_row >= len(maze):
                continue
            if new_col < 0 or new_col >= len(maze[new_row]):
                continue
            if maze[new_row][new_col] == "#":
                continue
            if distances[new_row][new_col] != -1:
                continue
            distances[new_row][new_col] = distances[row][col] + 1
            queue.append((new_row, new_col))
    return False, None


def parse_maze(text):
    maze = []
    for line in text.strip().split("\n"):
        maze.append(line.split())
    return maze


maze_1 = parse_maze("""
# # # # # #
# S . . . #
# # # . # #
# . . . . #
# . # # E #
# # # # # #
""")

maze_2 = parse_maze("""
# # # # # #
# S . # . #
# # # # # #
# . . . E #
# # # # # #
""")

maze_3 = parse_maze("""
# # # # #
# . . . #
# . . . #
# # # # #
""")

for number, maze in enumerate((maze_1, maze_2, maze_3), 1):
    found, length = solve_maze(maze)
    print("Лабиринт", number)
    if found:
        print("Путь найден, длина пути:", length)
    elif length is None and (find_symbol(maze, "S") is None or find_symbol(maze, "E") is None):
        print("В лабиринте нет начала или конца")
    else:
        print("Пути нет")
    print()