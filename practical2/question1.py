from collections import deque
def bfs(start, target):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path

        # Operation +1
        next_num = current + 1
        if next_num <= target and next_num not in visited:
            visited.add(next_num)
            queue.append((next_num, path + [next_num]))

        # Operation ×2
        next_num = current * 2
        if next_num <= target and next_num not in visited:
            visited.add(next_num)
            queue.append((next_num, path + [next_num]))

    return None


path = bfs(1, 10)

print("Shortest path:", path)
print("Number of operations:", len(path) - 1)