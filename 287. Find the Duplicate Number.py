class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floyd's tortoise and hare algorithm
        slow  , fast = 0 ,0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
    
        slowpt2 =0
        while True:
            slow= nums[slow]
            slowpt2=nums[slowpt2]
            if slow==slowpt2:
                return slow or slowpt2 

    



