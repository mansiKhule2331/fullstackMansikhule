from collections import deque

def find_shortest_sequence(start, target):
    # Queue stores tuples of (current_value, path_of_operations)
    queue = deque([(start, [str(start)])])
    # Set to keep track of visited numbers to prevent infinite loops
    visited = {start}

    while queue:
        current, path = queue.popleft()

        # Check if we have reached the target
        if current == target:
            return " -> ".join(path)

        # Generate next possible states
        next_states = [
            (current + 1, f"+1"),
            (current * 2, f"x2")
        ]

        for next_val, op in next_states:
            # Optimization: No need to process numbers way larger than target
            if next_val not in visited and next_val <= target + 1:
                visited.add(next_val)
                queue.append((next_val, path + [f"({op}) {next_val}"]))

    return "No sequence found"

# Run the program
start_num = 2
target_num = 9
result = find_shortest_sequence(start_num, target_num)
print(f"Shortest sequence from {start_num} to {target_num}:")
print(result)