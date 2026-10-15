# Implementing IDDFS (Iterative Deepening DFS)

def dls(tree, root, limit, depth=0):
    print(root, end=" ")

    if depth == limit:
        return

    for child in tree[root]:
        dls(tree, child, limit, depth + 1)


# Input Tree
tree = {
    'F': ['A'],
    'A': ['R'],
    'R': ['I'],
    'I': ['Y'],
    'Y': []
}

print("IDDFS Traversal Result:")

for limit in range(5):
    print("\nDepth Limit", limit, ": ", end="")
    dls(tree, 'F', limit)

print()