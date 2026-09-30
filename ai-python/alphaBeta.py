import math


# Alpha-Beta Pruning implementation
def alpha_beta_pruning(depth, nodeIndex, maximizingPlayer, values, alpha, beta):

    # Terminal node (leaf node)
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        maxEval = -math.inf

        # Recursively call the function for the next depth
        for i in range(2):
            eval = alpha_beta_pruning(
                depth + 1, nodeIndex * 2 + i, False, values, alpha, beta
            )

            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)

            # Beta pruning
            if beta <= alpha:
                break

        return maxEval

    else:
        minEval = math.inf

        # Recursively call the function for the next depth
        for i in range(2):
            eval = alpha_beta_pruning(
                depth + 1, nodeIndex * 2 + i, True, values, alpha, beta
            )

            minEval = min(minEval, eval)
            beta = min(beta, eval)

            # Alpha pruning
            if beta <= alpha:
                break

        return minEval


# Test the Alpha-Beta Pruning algorithm
if __name__ == "__main__":

    # Example: leaf nodes of a game tree
    values = [3, 5, 6, 9, 1, 2, 0, -1]

    # Initialize alpha and beta
    alpha = -math.inf
    beta = math.inf

    # Start at depth 0, with node index 0 (root node)
    # and maximizing player
    result = alpha_beta_pruning(0, 0, True, values, alpha, beta)

    print(f"The optimal value is: {result}")
