from collections import deque

def find_shortest_path_bfs(start, target):
    # Store the path as a list of nodes directly inside the queue: (current_node, path_taken)
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        current, path = queue.popleft()
        
        # If we reached the target, return the accumulated path
        if current == target:
            return path
            
        # Generate valid neighbors where the difference is exactly 1
        # Also constraint the bounds between 1 and 10 for efficiency
        for neighbor in (current - 1, current + 1):
            if 1 <= neighbor <= 10 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None

# Execution
start_node = 1
target_node = 10
shortest_path = find_shortest_path_bfs(start_node, target_node)

print(f"Shortest path from {start_node} to {target_node}: {shortest_path}")