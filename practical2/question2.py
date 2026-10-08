from collections import deque

def bfs(start, target):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, moves = queue.popleft()

        if current == target:
            return moves

        next_num = current * 2

        if next_num not in visited and next_num <= target:
            visited.add(next_num)
            queue.append((next_num, moves + 1))

    return -1


result = bfs(1, 16)

print("Minimum number of moves:", result)