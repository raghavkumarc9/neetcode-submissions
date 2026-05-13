class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        min_index = nums.index(min(nums))
        subarray_1 = nums[:min_index]
        subarray_2 = nums[min_index:]

        def _index_finder(sub_array: list, target: int):
            low = 0
            high = len(sub_array)

            while low < high:
                mid = (low + high) // 2
                if sub_array[mid] == target:
                    return mid
                elif sub_array[mid] < target:
                    low = mid + 1
                else:
                    high = mid
                
            return -1

        output = _index_finder(subarray_1, target)
        if output != -1:
            return output
        output = _index_finder(subarray_2, target)
        if output != -1:
            return output + min_index
        return output

       


        