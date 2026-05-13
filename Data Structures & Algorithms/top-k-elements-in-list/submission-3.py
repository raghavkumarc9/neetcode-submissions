class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        
        new_dict = sorted(my_dict.items(), key=lambda item:item[1], reverse=True)
        return_list = [i[0] for i in new_dict[:k]]

        return return_list
        


