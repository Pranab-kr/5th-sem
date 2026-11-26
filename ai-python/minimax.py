import math


def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # base case : targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        print("in if loop")

        amaxturn = minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth)

        print("__________under amaxturn_______")
        print("amaxturn value is", amaxturn)
        print(curDepth, nodeIndex, targetDepth)
        print("now move to bmaxturn")

        bmaxturn = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)

        print("__________under bmaxturn_______")
        print("bmaxturn value is", bmaxturn)
        print(curDepth, nodeIndex, targetDepth)

        maxturn = max(amaxturn, bmaxturn)
        return maxturn

    else:
        print("in else part")

        aminturn = minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth)

        print("__________under aminturn_______")
        print("aminturn value is", aminturn)
        print(curDepth, nodeIndex, targetDepth)
        print("approaching towards the bminturn")

        bminturn = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)

        print("__________under bminturn_______")
        print("bminturn value is", bminturn)
        print(curDepth, nodeIndex, targetDepth)

        minturn = min(aminturn, bminturn)
        return minturn


# Driver code
if __name__ == "__main__":
    scores = [3, 5, 2, 9, 12, 5, 23, 23]

    if len(scores) == 0 or (len(scores) & (len(scores) - 1)) != 0:
        raise ValueError("Number of leaf scores must be a non-zero power of 2.")

    treeDepth = int(math.log2(len(scores)))

    optimal_value = minimax(0, 0, True, scores, treeDepth)
    print("The optimal value is :", optimal_value)
