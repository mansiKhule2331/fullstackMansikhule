from collections import deque

def bfs(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Start or destination is blocked
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1

    queue = deque([(0, 0, 0)])  # row, column, distance
    visited = set([(0, 0)])

    # Up, Down, Left, Right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c, distance = queue.popleft()

        # Reached bottom-right
        if r == rows - 1 and c == cols - 1:
            return distance

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] == 0 and
                (nr, nc) not in visited):

                visited.add((nr, nc))
                queue.append((nr, nc, distance + 1))

    return -1


# 2×2 grid
grid = [
    [0, 0],
    [1, 0]
]

result = bfs(grid)

print("Shortest path length:", result)