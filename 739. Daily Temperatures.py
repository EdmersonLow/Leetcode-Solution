class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] *len(temperatures)
        stack = [] #temperate and index

        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                stackTemp ,stackIndex = stack.pop()
                result[stackIndex]= i -stackIndex
            
            stack.append((n,i))
        return result

