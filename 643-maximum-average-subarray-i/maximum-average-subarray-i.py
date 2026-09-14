class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        s = sum(nums[left:left+k])
        maxi = s
        left+=1
        while(left+k-1<len(nums)):
            s = s-nums[left-1]+nums[left+k-1]
            maxi = max(maxi,s)
            
            #print(left,maxi,s)
            left+=1
        if k>len(nums):
            maxi = sum(nums)
        return maxi/k