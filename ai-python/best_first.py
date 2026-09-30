import heapq

graph_relation = {
    "S": ["A", "B", "C"],
    "A": ["D", "E", "G"],
    "B": ["G"],
    "C": ["G"],
    "E": [],
    "D": [],
    "G": [],
}

heuristic = {"S": 8, "A": 8, "B": 2, "C": 3, "D": -1, "E": -1, "G": 0}


def best_first_search(graph, start, goal, heuristic):
    graph = graph_relation
    heuristic = heuristic

    start = "S"
    goal = "G"

    queue = [(heuristic[start], start)]

    came_from = {}
    came_from[start] = None

    while queue:
        _, peak_node = heapq.heappop(queue)

        if peak_node == goal:
            break

        for neighbor in graph[peak_node]:
            if neighbor not in came_from:
                heapq.heappush(queue, (heuristic[neighbor], neighbor))
                came_from[neighbor] = peak_node

    return came_from


start_node = "S"
goal_node = "G"

came_from = best_first_search(graph_relation, start_node, goal_node, heuristic)

print(came_from)
node = goal_node
path = [node]

while node != start_node:
    node = came_from[node]
    path.append(node)

path.reverse()

print("BFS path from start-node to goal-node:", path)
