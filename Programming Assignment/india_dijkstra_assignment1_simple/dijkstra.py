import csv
import heapq


def load_graph():
    graph = {}

    with open("india_roads.csv", "r") as file:
        data = csv.DictReader(file)

        for row in data:
            city1 = row["source"]
            city2 = row["destination"]
            distance = float(row["distance"])

            if city1 not in graph:
                graph[city1] = []

            if city2 not in graph:
                graph[city2] = []

            # Roads are considered two-way
            graph[city1].append((city2, distance))
            graph[city2].append((city1, distance))

    return graph


def dijkstra(graph, start):
    distance = {}

    for city in graph:
        distance[city] = float("inf")

    previous = {}

    for city in graph:
        previous[city] = None

    distance[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_city = heapq.heappop(queue)

        if current_distance > distance[current_city]:
            continue

        for next_city, road_distance in graph[current_city]:

            new_distance = current_distance + road_distance

            if new_distance < distance[next_city]:
                distance[next_city] = new_distance
                previous[next_city] = current_city

                heapq.heappush(
                    queue,
                    (new_distance, next_city)
                )

    return distance, previous


def get_path(previous, start, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)

        if current == start:
            break

        current = previous[current]

    path.reverse()

    if path[0] != start:
        return []

    return path


graph = load_graph()

print("Indian Cities - Dijkstra Algorithm")
print("-----------------------------------")

print("\nAvailable cities:")
print(", ".join(sorted(graph)))

start = input("\nEnter starting city: ").strip()

if start not in graph:
    print("City not found.")
else:
    distance, previous = dijkstra(graph, start)

    print("\nShortest distances from", start)
    print("-----------------------------------")

    for city in sorted(graph):
        if distance[city] == float("inf"):
            print(city, ": No route")
        else:
            path = get_path(previous, start, city)
            print(
                city,
                ":",
                distance[city],
                "km",
                "|",
                " -> ".join(path)
            )

    destination = input(
        "\nEnter destination city: "
    ).strip()

    if destination not in graph:
        print("City not found.")
    elif distance[destination] == float("inf"):
        print("No route found.")
    else:
        path = get_path(previous, start, destination)

        print("\nShortest path:")
        print(" -> ".join(path))
        print("Distance:", distance[destination], "km")
