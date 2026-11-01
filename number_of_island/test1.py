from collections import deque
from typing import List

class Solution:
    def BFS(self, grid, i, j, seen):
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        que = deque([(i, j)])
        seen[i][j] = 1
        while que:
            row, col = que.popleft()
            for dr, dc in dirs:
                nextRow = row + dr
                nextCol = col + dc
                if nextRow < 0 or nextRow >= len(grid) or nextCol < 0 or nextCol >= len(grid[0]):
                    continue
                if seen[nextRow][nextCol] != -1:
                    continue
                if grid[nextRow][nextCol] == "1":
                    que.append((nextRow, nextCol))
                    seen[nextRow][nextCol] = 1


    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[-1 for _ in range(n)] for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if seen[i][j] != -1:
                    continue
                if grid[i][j] == "0":
                    continue
                self.BFS(grid, i, j, seen)
                result += 1
        return result