def bfs(grid, cur):
    queue = collections.deque([[cur]])
    visited = set([cur])
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        if grid[y][x] == '!':
            path.remove(path[0])
            return path
        elif grid[y][x] == 'o':
            path.remove(path[0])
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if grid[y2][x2] != '#' and (y2, x2) not in visited:
                queue.append(path + [[y2, x2]])
                visited.add((y2, x2))
