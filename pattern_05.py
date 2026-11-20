class Solution:
    def pattern5(self, n):
        for i in range(1,n+1):
            for j in range(n-i+1):
                print("*", end=" ")
            print()

n = int(input())
patt5 = Solution()
patt5.pattern5(n)