from collections import deque

def bfs(tree, root):
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for child in tree[vertex]:
                if child not in visited:
                    queue.append(child)


# Input Tree
tree = {
    'F': ['A1', 'R'],
    'A1': ['I', 'Y'],
    'R': ['A2'],
    'I': [],
    'Y': [],
    'A2': []
}

print("BFS Traversal:")
bfs(tree, 'F')

