package main

func subarraySum(nums []int, k int) int {
	prefix := 0
	subarrayMap := make(map[int]int)
	subarrayMap[0] = 1
	result := 0
	for _, num := range nums {
		prefix += num
		result += subarrayMap[prefix-k]
		subarrayMap[prefix] += 1
	}
	return result
}
