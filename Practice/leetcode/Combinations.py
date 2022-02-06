class Solution:
    def combine(self, n: int, k: int):
        ans = list()
        target = list()
        for i in range(1, k + 1):
            com = list(range(i, n - k + i))
            target.append(com)
        print(target)
        return ans
           

# n, k = map(int, input().split())
n = int(input())
k = int(input())
do = Solution()
print(do.combine(n, k))
