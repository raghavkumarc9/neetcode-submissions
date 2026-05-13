class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #defining hash map to store it
        my_dict = {}
        for i in nums:
            if i not in my_dict.keys():
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        # print(dict)
        
        # for key in dict.keys():
        new_dict = dict(sorted(my_dict.items(), key=lambda item:item[1], reverse=True))
        # print(type(new_dict))
        # print(new_dict)
        return_list = []
        for i in new_dict.keys():
            print(len(return_list))
            if len(return_list) < k:
                return_list.append(i)

        return return_list
        


