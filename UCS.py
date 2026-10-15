import heapq

def ucs(tree, root):
    visited = set()
    queue = [(0, root)]

    while queue:
        cost, node = heapq.heappop(queue)

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for child, edge_cost in tree[node]:
                heapq.heappush(queue, (cost + edge_cost, child))

tree = {
    'F': [('A', 1)],
    'A': [('R', 2)],
    'R': [('I', 3)],
    'I': [('Y', 4)],
    'Y': []
}

print("UCS Traversal Result:")
ucs(tree, 'F')
print()