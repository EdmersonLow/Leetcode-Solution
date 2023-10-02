class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # l, r = 0 , len(s)-1
        # while l<r:
        #     s[l] , s[r] = s[r] , s[l]
        #     l+=1
        #     r-=1
        # stack = []
        # for c in s:
        #     stack.append(c)
        # i = 0

        # while stack:
        #     s[i]=stack.pop()
        #     i+=1

        def reverse(l , r ):
                if l < r :
                    s[l] , s[r] = s[r] , s[l]
                    reverse(l+1 , r-1)
        reverse( 0 , len(s)-1 )