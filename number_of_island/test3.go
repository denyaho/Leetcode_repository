package main

type unionFind struct {
	par []int
	siz []int
}

func NewunionFind(n int) unionFind {
	par := make([]int, n)
	siz := make([]int, n)
	for i := range n {
		par[i] = -1
		siz[i] = 1
	}
	return unionFind{par: par, siz: siz}
}

func (uf unionFind) root(x int) int {
	if uf.par[x] == -1 {
		return x
	}
	uf.par[x] = uf.root(uf.par[x])
	return uf.par[x]
}

func (uf unionFind) issame(x, y int) bool {
	if uf.root(x) == uf.root(y) {
		return true
	}
	return false
}

func (uf unionFind) unite(x, y int) bool {
	x = uf.root(x)
	y = uf.root(y)
	if x == y {
		return false
	}
	if uf.siz[x] < uf.siz[y] {
		x, y = y, x
	}
	uf.par[y] = x
	uf.siz[x] += uf.siz[y]
	return true
}

func numIslands(grid [][]byte) int {
	m := len(grid)
	n := len(grid[0])

	uf := NewunionFind(m * n)
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			if grid[row][col] == '0' {
				continue
			}
			cur := row*n + col
			if col+1 < n && grid[row][col+1] == '1' {
				uf.unite(cur, cur+1)
			}
			if row+1 < m && grid[row+1][col] == '1' {
				uf.unite(cur, cur+n)
			}
		}
	}

	result := 0
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			cur := row*n + col
			if grid[row][col] == '0' {
				continue
			}
			if uf.root(cur) == cur {
				result += 1
			}
		}
	}
	return result
}
