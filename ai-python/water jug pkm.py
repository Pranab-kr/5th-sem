def water_jug(jugA, jugB, maxA, maxB, target, visited):

    if (jugA, jugB) in visited:
        return False

    visited.add((jugA, jugB))

    print("Jug A =", jugA, ", Jug B =", jugB)

    if jugA == target or jugB == target:
        print("Target achieved!")
        return True

    if water_jug(maxA, jugB, maxA, maxB, target, visited):
        return True

    if water_jug(jugA, maxB, maxA, maxB, target, visited):
        return True

    if water_jug(0, jugB, maxA, maxB, target, visited):
        return True

    if water_jug(jugA, 0, maxA, maxB, target, visited):
        return True

    transfer = min(jugA, maxB - jugB)

    if water_jug(jugA - transfer, jugB + transfer, maxA, maxB, target, visited):
        return True

    transfer = min(jugB, maxA - jugA)

    if water_jug(jugA + transfer, jugB - transfer, maxA, maxB, target, visited):
        return True

    return False


maxA = int(input("Enter maximum capacity of Jug A: "))
maxB = int(input("Enter maximum capacity of Jug B: "))
target = int(input("Enter the quantity to obtain: "))

if target > maxA and target > maxB:
    print("Target cannot be obtained in either jug.")
else:
    print("\nSteps:")

    visited = set()

    if not water_jug(0, 0, maxA, maxB, target, visited):
        print("No solution exists.")
