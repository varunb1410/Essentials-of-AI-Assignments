# UGV Navigation with Dynamic Obstacles

## Aim

To design a simple navigation algorithm for an Unmanned Ground Vehicle (UGV) when obstacles can appear or move during navigation.

Unlike the previous problem, the obstacles are not completely known in advance. Therefore, the UGV must check its surroundings and calculate a new path when the current path is blocked.

## Files

```text
UGV_Dynamic_Obstacles/
├── ugv_dynamic.py
└── README.md
```

## Requirements

Python 3 is required.

No external Python packages are required.

The program uses:

- `random`
- `heapq`
- `time`

## How to Run

Open the terminal in the project folder and run:

```text
python ugv_dynamic.py
```

The UGV starts at:

```text
(0, 0)
```

and tries to reach:

```text
(29, 29)
```

## Main Idea

The UGV first uses A* to find a path.

While moving, a new obstacle can appear.

If the new obstacle blocks the next planned movement, the UGV stops and runs A* again from its current position.

This process continues until the UGV reaches the goal or no path is available.

## A* Formula

The program uses:

```text
f(n) = g(n) + h(n)
```

where:

- `g(n)` is the distance already travelled.
- `h(n)` is the estimated distance to the goal.
- `f(n)` is the total estimated cost.

Manhattan distance is used as the heuristic:

```text
h(n) = |x1 - x2| + |y1 - y2|
```

## Dynamic Obstacle

A new obstacle is randomly created during the UGV's movement.

If it blocks the next planned position, the program calculates another path.

This is called **replanning**.

## Algorithm

1. Create the grid.
2. Place some initial obstacles.
3. Set the start and goal.
4. Run A* to find a path.
5. Move the UGV one step.
6. Simulate a new obstacle appearing.
7. Check whether the new obstacle blocks the planned movement.
8. If it blocks the path, run A* again.
9. Continue until the goal is reached.

## Measures of Effectiveness

### 1. Total Distance

The number of movements made by the UGV.

### 2. Number of Replans

The number of times A* had to calculate a new path.

### 3. Execution Time

The total time taken by the program.

### 4. Goal Success

Whether the UGV successfully reaches the goal.

### 5. Collision Avoidance

The UGV should not move into a cell containing an obstacle.

## Grid Symbols

```text
U = UGV
G = Goal
# = Obstacle
* = Path
. = Empty cell
```

## Static vs Dynamic Environment

In a static environment, the obstacles are known before planning and normally do not change.

In a dynamic environment, obstacles can appear or change while the UGV is moving. Therefore, the UGV needs to update its map and replan its path.

## Possible Improvement

For a larger real-world problem, instead of running A* from the beginning every time, algorithms such as D* or D* Lite can be used. They are designed for situations where the environment changes and the previous path needs to be updated.

## Conclusion

A* can be combined with replanning to navigate a UGV in an environment where obstacles can change. The UGV first finds a path, moves through the environment, and calculates a new path whenever a newly detected obstacle blocks its movement.
