import math


# Alpha-Beta Pruning implementation
def alpha_beta_pruning(
    depth, nodeIndex, maximizingPlayer, values, alpha, beta, targetDepth=None
):
    if targetDepth is None:
        n = len(values)
        if n == 0 or (n & (n - 1)) != 0:
            raise ValueError("Number of leaf values must be a non-zero power of 2.")
        targetDepth = int(math.log2(n))

    # Terminal node (leaf node)
    if depth == targetDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        maxEval = -math.inf

        # Recursively call the function for the next depth
        for i in range(2):
            val = alpha_beta_pruning(
                depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, targetDepth
            )

            maxEval = max(maxEval, val)
            alpha = max(alpha, val)

            # Beta pruning
            if beta <= alpha:
                break

        return maxEval

    else:
        minEval = math.inf

        # Recursively call the function for the next depth
        for i in range(2):
            val = alpha_beta_pruning(
                depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, targetDepth
            )

            minEval = min(minEval, val)
            beta = min(beta, val)

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
