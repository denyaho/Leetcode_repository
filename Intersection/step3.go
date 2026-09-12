package main

func intersection(nums1 []int, nums2 []int) []int {
	set1 := make(map[int]struct{}, len(nums1))
	for _, n := range nums1 {
		set1[n] = struct{}{}
	}

	intersection := make([]int, 0)
	seen := make(map[int]struct{})
	for _, n := range nums2 {
		if _, exists := set1[n]; exists {
			if _, added := seen[n]; !added {
				intersection = append(intersection, n)
				seen[n] = struct{}{}
			}
		}
	}
	return intersection
}

// pythonにおけるsetを模倣するには struct{}を値と持つmapを使う
// boolでもいいがstructを使うことで0バイトメモリで済む
