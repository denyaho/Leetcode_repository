package main

type quePoint struct {
	row int
	col int
}

func BFS(grid [][]byte, row, col int, seen [][]int) {
	dirs := []quePoint{
		{-1, 0},
		{1, 0},
		{0, -1},
		{0, 1},
	}
	que := []quePoint{{row, col}}
	seen[row][col] = 1
	for len(que) > 0 {
		nque := que[0]
		row = nque.row
		col = nque.col
		que = que[1:]
		for _, dir := range dirs {
			nr := row + dir.row
			nc := col + dir.col
			if nr < 0 || nr >= len(grid) || nc < 0 || nc >= len(grid[0]) {
				continue
			}
			if seen[nr][nc] == 1 {
				continue
			}
			if grid[nr][nc] == '1' {
				que = append(que, quePoint{nr, nc})
				seen[nr][nc] = 1
			}
		}
	}

}

func numIslands(grid [][]byte) int {
	m := len(grid)
	n := len(grid[0])

	result := 0
	seen := make([][]int, m)
	for i := range seen {
		seen[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if seen[i][j] != 0 {
				continue
			}
			if grid[i][j] == '0' {
				continue
			}
			BFS(grid, i, j, seen)
			result += 1
		}
	}
	return result
}



