class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r  = 0 , len(numbers)-1 
        
        while l < r:
            totalSum = numbers[l] + numbers[r]/problems/two-sum-ii-input-array-is-sorted/
            if totalSum > target:
                r = r -1
            if totalSum < target:
                l = l +1 
            if totalSum == target:
                return [l+1 , r+1]
                

