class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = sum(nums) # 1
        val = 0
        for i in nums:
            val += i    # -2 ; 1;-2;4;3;5;6
            maxi = max(val,i,maxi) # 1 ; 1;1;4;4;5;6
            if val<0:
                val = 0 # 0 ;_;0;_;_;_;_
        return maxi