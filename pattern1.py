#Pattern 1:

class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()


n = int(input())
patt1 = Solution()
patt1.pattern1(n)