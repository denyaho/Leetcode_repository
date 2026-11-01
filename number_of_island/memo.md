#　問題
https://leetcode.com/problems/number-of-islands/description/


## step1

### 方針
問題では、1として表示される陸地と０で表示される海があって陸地がそれぞれ何個あるかを出力するように求められる。

gridとしてm*nの二次元配列が与えられる。

そこで、今回の問題では、m*nサイズのseenという配列を用意し、
gridの各要素に対し探索アルゴリズム(BFS, DFS)を適用する。
一回の探索を行うことで陸地を全てvisited状態にできるので、
何回探索を実行したかが今回の問題の解答となる。

- BFSを利用して実装

時間計算量 O(M×N)
空間計算量 O(M×N)

```
from collections import deque


class Solution:
    def visit_adjacent_lands(self, grid, row, col, seen):
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        que = deque([(row, col)])
        seen[row][col] = 1
        while que:
            currentRow, currentCol = que.popleft()
            for dr, dc in dirs:
                nextRow = currentRow + dr
                nextCol = currentCol + dc
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
        for row in range(m):
            for col in range(n):
                if seen[row][col] != -1:
                    continue
                if grid[row][col] == "0":
                    continue
                self.visit_adjacent_lands(grid, row, col, seen)
                result += 1
        return result
```

- DFSの実装

時間計算量 O(M×N)
空間計算量 O(M×N)
```
class Solution:
    def visit_adjacent_lands(self, grid, row, col, seen):
        seen[row][col] = 1
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for dr, dc in dirs:
            nextRow = row + dr
            nextCol = col + dc
            if nextRow < 0 or nextRow >= len(grid) or nextCol < 0 or nextCol >= len(grid[0]):
                continue
            if seen[nextRow][nextCol] != -1:
                continue
            if grid[nextRow][nextCol] == "1":
                self.DFS(grid, nextRow, nextCol, seen)

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
                self.visit_adjacent_lands(grid, i, j, seen)
                result += 1
        return result
```

## step2

https://github.com/garunitule/coding_practice/pull/17

Union-findの実装

uniteにおいて、union by sizeと
rootにおいて経路圧縮を行い計算量を短縮
```
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
```



## 参考資料
・Pythonのスタックとキューには何を使えばいいのか（各データ構造の速度比較）
https://qiita.com/saba/items/107c4237206e31acdbef

スレッド並列性について
このコードではローカルにseenという変数を記述しているのでスレッドセーフ
self.seenとかにしてしまうとスレッドセーフではなくなる？
https://github.com/colorbox/leetcode/pull/31/changes#r1881098955

