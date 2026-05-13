class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a copy list
        copy_list = [0]*len(strs)
        hahs_map = {}
    
        for listElements in range(len(strs)):
            tempStr = list(strs[listElements])
            temp_str =str(''.join(sorted(tempStr)))
            copy_list[listElements] = temp_str

        for i in range(len(copy_list)):
            if copy_list[i] not in hahs_map:
                temp = strs[i]
                hahs_map[copy_list[i]] = [] #create a new dict row 
                hahs_map[copy_list[i]].append(temp)
            elif copy_list[i] in hahs_map:
                temp1 = strs[i]
                hahs_map[copy_list[i]].append(temp1)

        # print(hahs_map.values())
        return hahs_map.values()
                