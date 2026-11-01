package main

type toPath struct {
	row int
	col int
}

func DFS(grid [][]byte, row, col int, visited [][]bool) {
	visited[row][col] = true
	dirs := []toPath{
		{-1, 0},
		{1, 0},
		{0, -1},
		{0, 1},
	}
	for _, dir := range dirs {
		nr := row + dir.row
		nc := col + dir.col
		if nr < 0 || nr >= len(grid) || nc < 0 || nc >= len(grid[0]) {
			continue
		}
		if visited[nr][nc] == true {
			continue
		}
		if grid[nr][nc] == '1' {
			DFS(grid, nr, nc, visited)
		}
	}
}

func numIslands(grid [][]byte) int {
	m := len(grid)
	n := len(grid[0])

	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	var count int
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			if visited[row][col] == true {
				continue
			}
			if grid[row][col] == '0' {
				continue
			}
			DFS(grid, row, col, visited)
			count++
		}
	}
	return count
}
