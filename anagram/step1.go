import (
	"sort"
)

func groupAnagrams(strs []string) [][]string {
	sortStrTolistStr := make(map[string][]string)
	for _, elem := range strs {
		byteStr := []byte(elem)
		sort.Slice(byteStr, func(i, j int) bool { return byteStr[i] < byteStr[j] })
		sortStrTolistStr[string(byteStr)] = append(sortStrTolistStr[string(byteStr)], elem)
	}
	result := make([][]string, 0, len(sortStrTolistStr))
	for _, v := range sortStrTolistStr {
		result = append(result, v)
	}
	return result
}