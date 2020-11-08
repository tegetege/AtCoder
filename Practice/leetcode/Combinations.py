class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list()
        target = 1
        while target < n:
            

n, k = map(int,input().split())
do = Solution()
print(do.combine(n, k))
