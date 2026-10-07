package main

func firstUniqChar(s string) int {
	var countChar [26]int
	for _, str := range s {
		countChar[str-'a'] += 1
	}
	for i, str := range s {
		if countChar[str-'a'] == 1 {
			return i
		}
	}
	return -1
}
