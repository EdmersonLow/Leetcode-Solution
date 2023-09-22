class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0 ,len(height)-1
        area = 0
        
        while l<r: 
            result = (r-l) * min(height[l], height[r])
            area = max(area ,result)

            if height[l]<height[r]:
                l = l+1
            else:
                r = r-1
        return area
        