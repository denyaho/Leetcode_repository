class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(freq, left, right, pivot_index):
            sorted_index = left
            pivot_value = freq[pivot_index][0]
            freq[pivot_index], freq[right] = freq[right], freq[pivot_index]
            for i in range(left, right):
                value = freq[i][0]
                if value > pivot_value:
                    freq[i], freq[sorted_index] = freq[sorted_index], freq[i]
                    sorted_index += 1
            freq[sorted_index], freq[right] = freq[right], freq[sorted_index]
            return sorted_index

        def quick_select(freq, left, right, k):
            if left > right:
                return
            pivot_index = random.randint(left, right)
            sorted_index = partition(freq, left, right, pivot_index)
            if sorted_index == k:
                return
            elif sorted_index > k:
                quick_select(freq, left, sorted_index, k)
            else:
                quick_select(freq, sorted_index + 1, right, k)
            

        freq_dict = Counter(nums)
        freq_list = [ (count, num) for num, count in freq_dict.items()]
        quick_select(freq_list, 0, len(freq_list) - 1, k - 1)
        return [ num for count, num in freq_list[:k]]