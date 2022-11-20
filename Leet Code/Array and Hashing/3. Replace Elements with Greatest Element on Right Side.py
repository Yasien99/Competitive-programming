class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Very Time Consuming Solution 
        # arr_len = len(arr)
        # out_arr = []
        # for i in range (arr_len):
        #     if (i+1) == arr_len:
        #         out_arr.append(-1)
        #         return out_arr
        #     else:
        #         out_arr.append(max(arr[i+1:]))
        
        ############################################################
        arr_len = len(arr)
        out_arr = []
        right_max = -1 
        for i in range (arr_len-1, -1 ,-1):
            new_max = max(right_max, arr[i])
            arr[i]= right_max
            right_max = new_max
        
        return arr