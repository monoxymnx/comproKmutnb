from collections import deque
def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    conveyor_dir = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    if not start or not end:
        return {"distance": -1, "path": []}
    q = deque([(start, 0, [list(start)])])
    visited = set([start])
    while q:
        (r, c), dist, path = q.popleft()
        if (r, c) == end:
            return {"distance": dist, "path": path}
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if maze[nr][nc] == '#':
                continue
            new_path = path.copy()
            new_path.append([nr, nc])
            while (0 <= nr < rows and 0 <= nc < cols and 
                maze[nr][nc] in conveyor_dir):
                drc, dcc = conveyor_dir[maze[nr][nc]]
                nr, nc = nr + drc, nc + dcc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    nr, nc = None, None
                    break
                if maze[nr][nc] == '#':
                    nr, nc = None, None
                    break
                new_path.append([nr, nc])
            if nr is None:
                continue
            new_pos = (nr, nc)
            if new_pos not in visited:
                visited.add(new_pos)
                q.append(((nr, nc), dist + 1, new_path))
    return {"distance": -1, "path": []}

if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 2, 'path': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]}

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {"distance": -1, "path": []}


    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 7, 'path': [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 4]]}