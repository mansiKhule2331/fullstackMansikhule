from collections import deque

def solve_number_transformation(start, target):
    # Queue stores tuples of (current_number, path_taken)
    queue = deque([(start, [start])])
    # Set to keep track of visited numbers to avoid infinite loops
    visited = {start}
    
    while queue:
        current, path = queue.popleft()
        
        # Check if we reached our target
        if current == target:
            return path
            
        # Generate next possible states from the current number
        next_states = [current + 1, current * 2]
        
        for state in next_states:
            # Only process numbers that haven't been visited yet
            # Also ensure we don't overshoot the target unnecessarily
            if state not in visited and state <= target:
                visited.add(state)
                queue.append((state, path + [state]))

# Execute the BFS
start_num = 1
target_num = 10
shortest_path = solve_number_transformation(start_num, target_num)

print(f"Shortest path from {start_num} to {target_num}: {shortest_path}")