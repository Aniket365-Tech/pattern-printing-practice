class Solution:
    def pattern6(self, n):
        for i in range(n):
            for j in range(1,n-i+1):
                print(j,end=" ")
            print()

n = int(input())
patt6 = Solution()
patt6.pattern6(n)