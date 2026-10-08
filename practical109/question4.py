from collections import deque


def shortest_path_binary_matrix(grid):
  rows = len(grid)
  cols = len(grid[0])

  # Check if start or end is blocked ('I')
  if grid[0][0] == 'I' or grid[rows - 1][cols - 1] == 'I':
    return -1

  # Queue stores tuples of (r, c, distance)
  queue = deque([(0, 0, 1)])
  visited = set([(0, 0)])

  # Four cardinal directions: up, down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  while queue:
    r, c, dist = queue.popleft()

    # If we reached the bottom-right cell
    if r == rows - 1 and c == cols - 1:
      return dist

    for dr, dc in directions:
      nr, nc = r + dr, c + dc

      # Check boundaries, empty cells ('0'), and visited status
      if 0 <= nr < rows and 0 <= nc < cols:
        if grid[nr][nc] == '0' and (nr, nc) not in visited:
          visited.add((nr, nc))
          queue.append((nr, nc, dist + 1))

  # If queue is exhausted and destination is not reached
  return -1


# Example 2x2 grid test:
# 0 represents empty, 'I' represents blocked
grid = [['0', '0'], ['I', '0']]

print(ShortestPath := shortest_path_binary_matrix(grid))