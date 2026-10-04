import random
import heapq
import time

SIZE = 70

# 0 = free cell, 1 = obstacle


def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def create_grid(density, start, goal):
    grid = []

    for i in range(SIZE):
        row = []

        for j in range(SIZE):
            if random.random() < density:
                row.append(1)
            else:
                row.append(0)

        grid.append(row)

    # Start and goal should not be obstacles
    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0

    return grid


def get_neighbours(position, grid):
    row, col = position

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbours = []

    for move_row, move_col in moves:
        new_row = row + move_row
        new_col = col + move_col

        if 0 <= new_row < SIZE and 0 <= new_col < SIZE:
            if grid[new_row][new_col] == 0:
                neighbours.append((new_row, new_col))

    return neighbours


def a_star(grid, start, goal):
    start_time = time.time()

    queue = []
    heapq.heappush(queue, (0, start))

    cost = {start: 0}
    parent = {start: None}

    nodes_checked = 0

    while queue:
        current_f, current = heapq.heappop(queue)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            run_time = time.time() - start_time

            return path, nodes_checked, run_time

        nodes_checked += 1

        for next_cell in get_neighbours(current, grid):

            new_cost = cost[current] + 1

            if next_cell not in cost or new_cost < cost[next_cell]:
                cost[next_cell] = new_cost
                parent[next_cell] = current

                f = new_cost + heuristic(next_cell, goal)

                heapq.heappush(queue, (f, next_cell))

    run_time = time.time() - start_time

    return None, nodes_checked, run_time


def show_grid(grid, path, start, goal):
    path = set(path) if path else set()

    for i in range(SIZE):
        line = ""

        for j in range(SIZE):
            position = (i, j)

            if position == start:
                line += "S "
            elif position == goal:
                line += "G "
            elif position in path:
                line += "* "
            elif grid[i][j] == 1:
                line += "# "
            else:
                line += ". "

        print(line)


# Start and goal positions
start = (0, 0)
goal = (SIZE - 1, SIZE - 1)

# Three obstacle densities
densities = {
    "Low": 0.10,
    "Medium": 0.20,
    "High": 0.30
}

for name, density in densities.items():

    print("\n" + "=" * 50)
    print(name, "Obstacle Density")
    print("=" * 50)

    grid = create_grid(density, start, goal)

    path, nodes, run_time = a_star(
        grid,
        start,
        goal
    )

    if path:
        print("Path found")
        print("Path length:", len(path) - 1)
        print("Nodes checked:", nodes)
        print("Time:", round(run_time, 6), "seconds")

        print("\nGrid:")
        show_grid(grid, path, start, goal)

    else:
        print("No path found")
        print("Nodes checked:", nodes)
        print("Time:", round(run_time, 6), "seconds")
