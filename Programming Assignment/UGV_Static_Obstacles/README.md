# UGV Navigation Using A* Algorithm

## Aim

To design a path-finding algorithm for an Unmanned Ground Vehicle (UGV) moving through a 70 x 70 grid while avoiding known obstacles.

The program uses the A* search algorithm to find a shortest path from a starting position to a goal position.

## Problem

The UGV starts at the top-left corner of the grid:

```text
Start = (0, 0)
```

and has to reach:

```text
Goal = (69, 69)
```

Some cells contain obstacles. The obstacles are generated before the search starts, so they are known to the UGV.

The program tests three obstacle densities:

- Low = 10%
- Medium = 20%
- High = 30%

## Files

```text
UGV_Static_Obstacles/
├── ugv_astar.py
└── README.md
```

## Requirements

Python 3 is required.

No external Python libraries are needed.

The program uses:

- `random` for generating obstacles
- `heapq` for the priority queue
- `time` for measuring execution time

## How to Run

Open the terminal in the project folder and run:

```text
python ugv_astar.py
```

The program automatically runs the algorithm for all three obstacle densities.

## Grid Symbols

The output uses:

```text
S = Starting position
G = Goal position
# = Obstacle
* = Path taken by the UGV
. = Free cell
```

## A* Algorithm

A* selects the cell that has the lowest estimated total cost.

The formula is:

```text
f(n) = g(n) + h(n)
```

where:

- `g(n)` = distance travelled from the start
- `h(n)` = estimated distance from the current cell to the goal
- `f(n)` = total estimated cost

Manhattan distance is used as the heuristic:

```text
h(n) = |x1 - x2| + |y1 - y2|
```

The UGV can move:

- Up
- Down
- Left
- Right

Diagonal movement is not allowed.

## Algorithm Steps

1. Create a 70 x 70 grid.
2. Randomly place obstacles.
3. Keep the start and goal cells free.
4. Put the starting cell in the priority queue.
5. Select the cell with the lowest A* cost.
6. Check its neighbouring cells.
7. Calculate the cost of moving to each neighbour.
8. Continue until the goal is reached.
9. Reconstruct the path.
10. Display the path and performance values.

## Measures of Effectiveness

The program measures the following:

### 1. Path Length

The number of cells travelled by the UGV.

A shorter path means less distance travelled.

### 2. Nodes Checked

The number of cells examined by the A* algorithm.

Fewer checked cells generally means less search work.

### 3. Execution Time

The time taken by the program to find the path.

### 4. Success

The program checks whether the UGV can reach the goal.

## Result Table

After running the program, the results can be recorded as follows:

| Obstacle Density | Path Found | Path Length | Nodes Checked | Time |
|---|---|---:|---:|---:|
| Low (10%) | ___ | ___ | ___ | ___ |
| Medium (20%) | ___ | ___ | ___ | ___ |
| High (30%) | ___ | ___ | ___ | ___ |

Because the obstacles are generated randomly, the exact results can be different each time the program is executed.

## Advantages

- A* finds a shortest path for this grid when the goal is reachable.
- It avoids cells marked as obstacles.
- It uses a heuristic to guide the search toward the goal.
- It can be tested with different obstacle densities.

## Limitations

- Obstacles are randomly generated.
- The UGV can move only up, down, left and right.
- All movements have the same cost.
- The environment is static, so obstacles do not move after the grid is created.

## Conclusion

The A* algorithm can be used to navigate a UGV through a grid containing known obstacles. The algorithm uses both the distance already travelled and the estimated distance to the goal. By changing the obstacle density, the effect of obstacles on path length and search effort can also be studied.
