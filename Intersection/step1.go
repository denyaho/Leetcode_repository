package main

import (
	"slices"
)

func intersection(nums1 []int, nums2 []int) []int {
	nums1ToCount := make(map[int]int)
	nums2ToCount := make(map[int]int)

	for _, num := range nums1 {
		nums1ToCount[num] += 1
	}
	for _, num := range nums2 {
		nums2ToCount[num] += 1
	}

	result := make([]int, 0, max(len(nums1ToCount), len(nums2ToCount)))

	for _, num := range nums1 {
		if nums1ToCount[num] != 0 && nums2ToCount[num] != 0 {
			if !slices.Contains(result, num) {
				result = append(result, num)
			}
		}
	}
	return result
}
