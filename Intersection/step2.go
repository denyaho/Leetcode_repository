package main

import (
	"sort"
	"slices"
)

func intersection(nums1 []int, nums2 []int) []int {
	nums1Sorted := slices.Clone(nums1)
	nums2Sorted := slices.Clone(nums2)
	sort.Ints(nums1Sorted)
	sort.Ints(nums2Sorted)

	i := 0
	j := 0
	n := len(nums1Sorted)
	m := len(nums2Sorted)
	intersection := make([]int, 0, min(n, m))
	for i < n && j < m {
		if nums1Sorted[i] < nums2Sorted[j] {
			i += 1
			continue
		}
		if nums2Sorted[j] < nums1Sorted[i] {
			j += 1
			continue
		}
		commonNum := nums1Sorted[i]
		intersection = append(intersection, commonNum)
		for i < n && nums1Sorted[i] == commonNum {
			i += 1
		}
		for j < m && nums2Sorted[j] == commonNum {
			j += 1
		}
	}
	return intersection
}