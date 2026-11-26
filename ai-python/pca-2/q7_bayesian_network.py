"""
Question 7: Exact Inference in a Bayesian Belief Network (A -> B -> C).
Defines Conditional Probability Tables (CPTs) for binary nodes A, B, and C,
calculates P(A = True | C = True) using enumeration, and displays the numeric result.
"""

# Bayesian Network structure: A -> B -> C
VARIABLES = ["A", "B", "C"]
PARENTS = {"A": [], "B": ["A"], "C": ["B"]}

# Conditional Probability Tables (CPTs): P(node = True | parent values)
CPTS = {
    "A": {(): 0.3},
    "B": {(True,): 0.8, (False,): 0.2},
    "C": {(True,): 0.9, (False,): 0.1},
}


def prob_given_parents(var, val, evidence):
    parent_vals = tuple(evidence[p] for p in PARENTS[var])
    p_true = CPTS[var][parent_vals]
    return p_true if val else (1.0 - p_true)


def enumerate_all(variables, evidence):
    if not variables:
        return 1.0
    first, rest = variables[0], variables[1:]
    if first in evidence:
        return prob_given_parents(first, evidence[first], evidence) * enumerate_all(rest, evidence)
    total = 0.0
    for val in (True, False):
        extended = dict(evidence)
        extended[first] = val
        total += prob_given_parents(first, val, extended) * enumerate_all(rest, extended)
    return total


def enumeration_ask(query_var, evidence):
    dist = {}
    for val in (True, False):
        extended = dict(evidence)
        extended[query_var] = val
        dist[val] = enumerate_all(VARIABLES, extended)
    norm = sum(dist.values())
    return {val: prob / norm for val, prob in dist.items()}, dist


posterior, unnormalized = enumeration_ask("A", {"C": True})

print("CPTs:")
print("P(A=True) = 0.3, P(A=False) = 0.7")
print("P(B=True | A=True) = 0.8, P(B=True | A=False) = 0.2")
print("P(C=True | B=True) = 0.9, P(C=True | B=False) = 0.1")
print(f"\nP(A=True, C=True)  = {unnormalized[True]:.6f}")
print(f"P(A=False, C=True) = {unnormalized[False]:.6f}")
print(f"P(C=True)          = {unnormalized[True] + unnormalized[False]:.6f}")
print(f"\nP(A = True | C = True) = {posterior[True]:.6f}")
