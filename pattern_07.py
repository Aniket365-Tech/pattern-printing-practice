class Solution:
    def pattern7(self, n):
        
        for i in range(n):
            print(" "*(n-i-1),end="")
            
            for j in range(2*i+1):
                print("*",end="")
            print()
            
n = int(input())
patt7 = Solution()
patt7.pattern7(n)