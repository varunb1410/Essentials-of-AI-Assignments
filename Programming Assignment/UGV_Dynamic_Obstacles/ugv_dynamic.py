import random
import heapq
import time

SIZE = 30


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def create_grid():
    grid = []

    for i in range(SIZE):
        row = []

        for j in range(SIZE):
            if random.random() < 0.10:
                row.append(1)
            else:
                row.append(0)

        grid.append(row)

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

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < SIZE and 0 <= new_col < SIZE:
            if grid[new_row][new_col] == 0:
                neighbours.append((new_row, new_col))

    return neighbours


def a_star(grid, start, goal):
    queue = []
    heapq.heappush(queue, (0, start))

    cost = {start: 0}
    parent = {start: None}

    while queue:
        current_f, current = heapq.heappop(queue)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        for next_cell in get_neighbours(current, grid):

            new_cost = cost[current] + 1

            if next_cell not in cost or new_cost < cost[next_cell]:
                cost[next_cell] = new_cost
                parent[next_cell] = current

                f = new_cost + heuristic(next_cell, goal)

                heapq.heappush(queue, (f, next_cell))

    return None


def add_dynamic_obstacle(grid, current, goal):
    # Find free cells where a new obstacle can appear
    free_cells = []

    for i in range(SIZE):
        for j in range(SIZE):
            cell = (i, j)

            if grid[i][j] == 0 and cell != current and cell != goal:
                free_cells.append(cell)

    if free_cells:
        obstacle = random.choice(free_cells)
        grid[obstacle[0]][obstacle[1]] = 1
        return obstacle

    return None


def show_grid(grid, path, current, goal):
    path = set(path) if path else set()

    for i in range(SIZE):
        line = ""

        for j in range(SIZE):
            position = (i, j)

            if position == current:
                line += "U "
            elif position == goal:
                line += "G "
            elif position in path:
                line += "* "
            elif grid[i][j] == 1:
                line += "# "
            else:
                line += ". "

        print(line)


# Start and goal
start = (0, 0)
goal = (SIZE - 1, SIZE - 1)

grid = create_grid()

# Make sure start and goal are free
grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0

current = start
total_distance = 0
replans = 0

start_time = time.time()

while current != goal:

    # Find a path from the current position
    path = a_star(grid, current, goal)

    if path is None:
        print("No path is available.")
        break

    # The next position is the second cell in the path
    if len(path) > 1:
        next_position = path[1]
    else:
        next_position = current

    # Simulate a new obstacle appearing
    if random.random() < 0.20:

        obstacle = add_dynamic_obstacle(
            grid,
            current,
            goal
        )

        if obstacle is not None:

            # If the new obstacle blocks our planned next cell,
            # the UGV must find a new path.
            if obstacle == next_position:
                print(
                    "New obstacle detected at",
                    obstacle,
                    "- Replanning..."
                )

                replans += 1
                continue

    # Move the UGV
    current = next_position
    total_distance += 1

    print("UGV moved to:", current)


if current == goal:
    print("\nGoal reached!")
else:
    print("\nUGV could not reach the goal.")

print("Total distance:", total_distance)
print("Number of replans:", replans)
print("Execution time:",
      round(time.time() - start_time, 6),
      "seconds")

print("\nFinal Grid:")
show_grid(grid, [], current, goal)
