# Heuristic values
heuristic = {"A": 11, "B": 6, "C": 99, "D": 1, "E": 7, "G": 0}


# Weighted graph
graph = {
    "A": [("B", 2), ("E", 3)],
    "B": [("A", 2), ("C", 1), ("G", 9)],
    "C": [("B", 1)],
    "D": [("E", 6), ("G", 1)],
    "E": [("A", 3), ("D", 6)],
    "G": [("B", 9), ("D", 1)],
}


def get_neighbors(node):
    return graph.get(node, [])


def a_star(start_node, stop_node):

    open_set = {start_node}
    closed_set = set()

    g = {}
    parent = {}

    # Cost from start node
    g[start_node] = 0

    # Parent of start node is itself
    parent[start_node] = start_node

    while open_set:

        # Find node with minimum f(n) = g(n) + h(n)
        n = min(open_set, key=lambda node: g[node] + heuristic[node])

        # Goal reached
        if n == stop_node:

            path = []

            while parent[n] != n:
                path.append(n)
                n = parent[n]

            path.append(start_node)
            path.reverse()

            print("Path found:", path)
            print("Path cost:", g[stop_node])

            return path

        # Get neighbors
        neighbors = get_neighbors(n)

        for m, weight in neighbors:

            new_cost = g[n] + weight

            # If node is discovered for the first time
            if m not in open_set and m not in closed_set:

                open_set.add(m)

                parent[m] = n
                g[m] = new_cost

            # If we found a better path
            elif new_cost < g.get(m, float("inf")):

                g[m] = new_cost
                parent[m] = n

                # If node was already closed,
                # reopen it
                if m in closed_set:
                    closed_set.remove(m)

                open_set.add(m)

        # Move current node from open to closed
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None


# Start and goal
start_node = "A"
goal_node = "G"

# Run A*
a_star(start_node, goal_node)
