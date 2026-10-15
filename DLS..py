 # Implementing DLS (Depth-Limited Search)

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

print("DLS Traversal Result:")
dls(tree, 'F', 2)
print()