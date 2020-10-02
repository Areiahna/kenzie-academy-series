def is_island(matrix, row, col):
    # returns true if this particular row,col is an island
    return matrix[row][col] == 1


def is_on_matrix(matrix, row, col):
    # returns true if the passed in row and column is an actual position on the board
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def get_neighbor_islands(matrix, row, col):
    # returns the list of islands immediately horizontally or vertically positioned to the passed in (row,col) pair
    valid_islands = []
    if is_on_matrix(matrix, row, col - 1) and is_island(matrix, row, col - 1):  # check left
        valid_islands.append((row, col - 1))
    if is_on_matrix(matrix, row, col + 1) and is_island(matrix, row, col + 1):  # check right
        valid_islands.append((row, col + 1))
    if is_on_matrix(matrix, row - 1, col) and is_island(matrix, row - 1, col):  # check right
        valid_islands.append((row - 1, col))
    if is_on_matrix(matrix, row + 1, col) and is_island(matrix, row + 1, col):  # check right
        valid_islands.append((row + 1, col))
    return valid_islands


def dfs(matrix, visited, row, col):
    # standard Depth-First Search
    visited.add((row, col)) # add the the visited set so we don't keep going back to elements we've seen already
    for (neighbor_row, neighbor_col) in get_neighbor_islands(matrix, row, col): # get all islands next to current (r,c)
        if (neighbor_row, neighbor_col) not in visited: # we only want to continue the DFS if it's a *new* location
            dfs(matrix, visited, neighbor_row, neighbor_col) # continue DFS because it's a new location


def bfs(matrix, visited, row, col):
    q = [(row, col)]        # add starting point to our queue
    visited.add((row, col)) # make sure starting point is marked as visited since we've seen it
    while q: # keep going until we run out of new places to visit
        cur_row, cur_col = q.pop() # pop off the first available element in the queue to work with
        for neighbor_row, neighbor_col in get_neighbor_islands(matrix, cur_row, cur_col):# get islands next to current (r,c)
            if (neighbor_row, neighbor_col) not in visited: # we only want to continue the DFS if it's a *new* location
                visited.add((neighbor_row, neighbor_col)) # we only want to continue the DFS if it's a *new* location
                q.append((neighbor_row, neighbor_col)) # continue DFS because it's a new location


def count_islands_with_dfs(matrix):
    num_islands = 0
    visited = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_island(matrix, row, col) and (row, col) not in visited:
                visited.add((row, col))
                dfs(matrix, visited, row, col)
                num_islands += 1
    return num_islands


def count_islands_with_bfs(matrix):
    num_islands = 0
    visited = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_island(matrix, row, col) and (row, col) not in visited:
                visited.add((row, col))
                bfs(matrix, visited, row, col)
                num_islands += 1
    return num_islands


# DFS
print("DFS Test Cases")
print(count_islands_with_dfs( [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], ]) == 6)
print(count_islands_with_dfs( [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], ]) == 1)
print(count_islands_with_dfs([[1, 1, 0, 1, 1], ]) == 2)
print(count_islands_with_dfs([[1], ]) == 1)
print(count_islands_with_dfs([[0], ]) == 0)

print("\nBFS Test Cases")
# BFS
print(count_islands_with_bfs( [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], ]) == 6)
print(count_islands_with_bfs( [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], ]) == 1)
print(count_islands_with_bfs([[1, 1, 0, 1, 1], ]) == 2)
print(count_islands_with_bfs([[1], ]) == 1)
print(count_islands_with_bfs([[0], ]) == 0)
