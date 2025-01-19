# pathfinder.py
from collections import deque
from typing import List, Tuple

class PathFinder:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
    def find_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        queue = deque([[start]])
        visited = {start}
        
        if start == end:
            return [start]
            
        while queue:
            path = queue.popleft()
            row, col = path[-1]
            
            # Check all 4 directions
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if (new_row >= 0 and new_row < self.rows and 
                    new_col >= 0 and new_col < self.cols and 
                    self.grid[new_row][new_col] != 1 and 
                    (new_row, new_col) not in visited):
                    
                    if (new_row, new_col) == end:
                        return path + [(new_row, new_col)]
                        
                    queue.append(path + [(new_row, new_col)])
                    visited.add((new_row, new_col))
        
        return []  # No path found

# Example usage
if __name__ == "__main__":
    # 0 represents empty cell, 1 represents wall
    maze = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    pathfinder = PathFinder(maze)
    start = (0, 0)
    end = (4, 4)
    
    path = pathfinder.find_path(start, end)
    print(f"Path found: {path}")