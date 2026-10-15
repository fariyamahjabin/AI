# Implementing DFS (Depth-First Search)

def dfs(tree, root, visited=None):
    if visited is None:
        visited = set()

    visited.add(root)
    print(root, end=" ")

    for child in tree[root]:
        if child not in visited:
            dfs(tree, child, visited)


#Input Tree
tree ={
    'F': ['A'],
    'A': ['R'],
    'R': ['I'],
    'I': ['Y'],
    'Y': []
}

print("DFS Traversal Result:")
dfs(tree, 'F')
print()