"""
Question 8: Basic Operations on Fuzzy Sets and Fuzzy Relations.
Matches lab style for Union, Intersection, Complement, Difference,
Cartesian Product, and Max-Min Composition.
"""

# Define two fuzzy sets
A = [0.2, 0.4, 0.6, 0.8]
B = [0.3, 0.5, 0.7, 0.9]


# 1. Union of two fuzzy sets
def fuzzy_union(A, B):
    return [max(a, b) for a, b in zip(A, B)]


# 2. Intersection of two fuzzy sets
def fuzzy_intersection(A, B):
    return [min(a, b) for a, b in zip(A, B)]


# 3. Complement of a fuzzy set
def fuzzy_complement(A):
    return [round(1 - a, 4) for a in A]


# 4. Difference of two fuzzy sets
def fuzzy_difference(A, B):
    return [round(min(a, 1 - b), 4) for a, b in zip(A, B)]


# 5. Cartesian Product of two fuzzy sets
def cartesian_product(A, B):
    return [[min(a, b) for b in B] for a in A]


# 6. Max-Min Composition of two fuzzy relations
def max_min_composition(R, S):
    rows = len(R)
    cols = len(S[0])
    common = len(S)
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = max(min(R[i][k], S[k][j]) for k in range(common))
            row.append(value)
        result.append(row)
    return result


# Display results
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)

print("\n1. Union:", fuzzy_union(A, B))
print("2. Intersection:", fuzzy_intersection(A, B))
print("3. Complement of A:", fuzzy_complement(A))
print("4. Difference (A - B):", fuzzy_difference(A, B))

print("\n5. Cartesian Product:")
for row in cartesian_product(A, B):
    print(row)

# Fuzzy Relations for Max-Min Composition
R = [
    [0.2, 0.7, 0.5],
    [0.6, 0.4, 0.8],
]
S = [
    [0.5, 0.9],
    [0.7, 0.3],
    [0.6, 0.8],
]

print("\n6. Max-Min Composition (R o S):")
for row in max_min_composition(R, S):
    print(row)
