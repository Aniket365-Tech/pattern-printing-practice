class Solution:
    def pattern3(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end=" ")
            print()

n = int(input())
patt3 = Solution()
patt3.pattern3(n)