class Solution:
    def pattern8(self, n):
        for i in range(n,0,-1):
            print(" "*(n-i),end="")
            for j in range(2*i-1):
                print("*",end="")
            print()

n = int(input())
patt8 = Solution()
patt8.pattern8(n)
    