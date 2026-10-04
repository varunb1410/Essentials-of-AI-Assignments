# Dijkstra Algorithm - Indian Cities

## Aim

To find the shortest road distance between Indian cities using Dijkstra's algorithm.

## Files

- `dijkstra.py` - Python program
- `india_roads.csv` - city and road-distance data
- `README.md` - project information

## How it works

Each city is treated as a node and each road is treated as an edge.

The road distance is used as the cost of the edge.

Dijkstra's algorithm starts from a selected city and finds the shortest distance to all other connected cities.

## How to run

Install Python and open the project folder in the terminal.

Run:

```text
python dijkstra.py
```

Enter a starting city when asked.

For example:

```text
Enter starting city: Hyderabad
```

The program displays the shortest distance from Hyderabad to the other cities.

It then asks for a destination city and displays the shortest route.

## Algorithm

1. Give the starting city a distance of 0.
2. Give all other cities an infinite distance.
3. Select the city with the smallest distance.
4. Check its neighbouring cities.
5. Calculate the new distance through the current city.
6. Update the distance if the new distance is smaller.
7. Repeat until all required cities are processed.

## Time Complexity

Using a priority queue, the time complexity is approximately:

`O((V + E) log V)`

where V is the number of cities and E is the number of road connections.

## Data

The CSV contains a small city-level road graph for demonstrating the algorithm. The road-network idea and open map data reference are based on OpenStreetMap.

OpenStreetMap India:
https://www.openstreetmap.in/

OpenStreetMap India Roads:
https://wiki.openstreetmap.org/wiki/India/Roads

The CSV is kept small so that the program is easy to understand and demonstrate. It is not intended to represent every road in India.

## Conclusion

Dijkstra's algorithm successfully finds the shortest distance from a selected source city to the reachable cities when the road distances are non-negative.
