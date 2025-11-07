from queue import PriorityQueue

# Graph representation as an adjacency list
graph = {
    'A': [('B', 6), ('C', 3)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 4)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

# Heuristic values (estimated cost to reach goal)
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 0
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))  # (heuristic value, node)

    print("Best First Search Path:")

    while not pq.empty():
        _, current = pq.get()
        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            return

        visited.add(current)

        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

# Run the search
best_first_search('A', 'G')
