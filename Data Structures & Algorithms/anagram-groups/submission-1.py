class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs: List[str]):
        final_list = []
        temp_list = []
        for i in range(len(strs)):
            temp_list.append(sorted(strs[i]))
            # print(temp_list)
        # return temp_list
        my_dict = {}
        for k in range(len(strs)):
            temp_str = str(temp_list[k])
            if temp_str not in my_dict:
                my_dict[temp_str] = [strs[k]]
            else:
                my_dict[temp_str].append(strs[k])
        # return my_dict
        for l in my_dict.keys():
            final_list.append(my_dict[l])
        return final_list