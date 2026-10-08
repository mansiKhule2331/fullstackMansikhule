from collections import deque


def min_moves_bfs(start, target):
  # Queue stores tuples of (current_number, moves_count)
  queue = deque([(start, 0)])
  visited = {start}

  while queue:
    curr, moves = queue.popleft()

    # If we reached the target, return the number of moves
    if curr == target:
      return moves

    # Allowed move: multiply current number by 2
    next_num = curr * 2

    # Avoid values exceeding target unnecessarily or already visited
    if next_num <= target and next_num not in visited:
      visited.add(next_num)
      queue.append((next_num, moves + 1))

  return -1


start_val = 1
target_val = 16
result = min_moves_bfs(start_val, target_val)
print(f'Minimum moves required to reach {target_val} from {start_val}: {result}')