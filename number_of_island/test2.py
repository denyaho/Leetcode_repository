class UnionFind:
    def __init__(self, n: int):
        self.par = [-1 for _ in range(n)]
        self.siz = [1 for _ in range(n)]

    def root(self, x: int):
        if (self.par[x] == -1):
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x: int, y: int):
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m * n)
                    
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '0':
                    continue
                cur = row * n + col
                if col + 1 < n and grid[row][col + 1] == '1':
                    uf.unite(cur, cur + 1)
                if row + 1 < m and grid[row + 1][col] == '1':
                    uf.unite(cur, cur + n)
        result = 0
        for row in range(m):
            for col in range(n):
                cur = row * n + col
                if grid[row][col] == '0':
                    continue
                if uf.root(cur) == cur:
                    result += 1                
        return result