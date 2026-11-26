from collections import deque


def water_jug(maxA, maxB, target):
    if maxA < 0 or maxB < 0 or target < 0:
        print("Capacities and target must be non-negative integers.")
        return False

    if target > maxA and target > maxB:
        print("Target cannot be obtained in either jug.")
        return False

    start = (0, 0)
    queue = deque([start])
    parent = {start: None}
    goal_state = None

    while queue:
        jugA, jugB = queue.popleft()

        if jugA == target or jugB == target:
            goal_state = (jugA, jugB)
            break

        pour_A_to_B = min(jugA, maxB - jugB)
        pour_B_to_A = min(jugB, maxA - jugA)

        next_states = [
            (maxA, jugB),
            (jugA, maxB),
            (0, jugB),
            (jugA, 0),
            (jugA - pour_A_to_B, jugB + pour_A_to_B),
            (jugA + pour_B_to_A, jugB - pour_B_to_A),
        ]

        for state in next_states:
            if state not in parent:
                parent[state] = (jugA, jugB)
                queue.append(state)

    if goal_state is None:
        print("No solution exists.")
        return False

    path = []
    cur = goal_state
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    print("\nSteps:")
    for jugA, jugB in path:
        print("Jug A =", jugA, ", Jug B =", jugB)
    print("Target achieved!")
    return True


if __name__ == "__main__":
    try:
        maxA = int(input("Enter maximum capacity of Jug A: "))
        maxB = int(input("Enter maximum capacity of Jug B: "))
        target = int(input("Enter the quantity to obtain: "))
        water_jug(maxA, maxB, target)
    except ValueError:
        print("Please enter valid integer values.")

# Enter maximum capacity of Jug A: 4
# Enter maximum capacity of Jug B: 3
# Enter the quantity to obtain: 2

# Steps:
# Jug A = 0 , Jug B = 0
# Jug A = 0 , Jug B = 3
# Jug A = 3 , Jug B = 0
# Jug A = 3 , Jug B = 3
# Jug A = 4 , Jug B = 2
# Target achieved!