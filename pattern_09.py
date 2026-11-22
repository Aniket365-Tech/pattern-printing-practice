class Solution:
    def pattern9(self,n):
        for i in range(n):
            print(" "*(n-i-1),end="")
            for j in range(2*i+1):
                print("*",end="")
            print()
        for i in range(n,0,-1):
            print(" "*(n-i),end="")
            for i in range(2*i-1):
                print("*",end="")
            print()
n = int(input())
patt9 = Solution()
patt9.pattern9(n)