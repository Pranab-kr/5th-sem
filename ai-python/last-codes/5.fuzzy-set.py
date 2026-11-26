A = [0.2, 0.4, 0.6, 0.8]
B = [0.3, 0.5, 0.7, 0.9]

def fuzzy_union(A, B):
    return [max(a, b) for a, b in zip(A, B)]

def fuzzy_intersection(A, B):
    return [min(a, b) for a, b in zip(A, B)]

def fuzzy_complement(A):
    return [1 - a for a in A]

def fuzzy_difference(A, B):
    return [min(a, 1 - b) for a, b in zip(A, B)]

def cartesian_product(A, B):
    return [[min(a, b) for b in B] for a in A]

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

print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("\n1. Union:", fuzzy_union(A, B))
print("2. Intersection:", fuzzy_intersection(A, B))
print("3. Complement of A:", fuzzy_complement(A))
print("4. Difference (A - B):", fuzzy_difference(A, B))

print("\n5. Cartesian Product:")
for row in cartesian_product(A, B):
    print(row)

R = [
    [0.2, 0.7, 0.5],
    [0.6, 0.4, 0.8]
]
S = [
    [0.5, 0.9],
    [0.7, 0.3],
    [0.6, 0.8]
]

print("\n6. Max-Min Composition (R o S):")
for row in max_min_composition(R, S):
    print(row)