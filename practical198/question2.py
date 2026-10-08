def find_minimum_platforms(arrivals, departures):
  arrivals.sort()
  departures.sort()

  n = len(arrivals)
  i = 1
  j = 0
  current_platforms = 1
  max_platforms = 1

  while i < n and j < n:
    if arrivals[i] <= departures[j]:
      current_platforms += 1
      i += 1
    else:
      current_platforms -= 1
      j += 1
    max_platforms = max(max_platforms, current_platforms)

  return max_platforms


# Test with the sample input
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(find_minimum_platforms(arr, dep))  # Output: 3