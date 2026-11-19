class Solution:
    def pattern2(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*",end=" ")

            print()

n = int(input())
patt2 = Solution()
patt2.pattern2(n)


