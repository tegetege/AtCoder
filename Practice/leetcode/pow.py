class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        K = 1
        if n > 0:
            while n > 1:
                if n % 2 != 0:
                    K = K * x
                    x = x ** 2
                    n = (n - 1) // 2
                else:
                    x = x ** 2
                    n = n // 2

            return K * x # 指数を割り続け n が 1 に至ったら終了
        else:
            n *= -1
            x = 1 / x
            while n > 1:
                if n % 2 != 0:
                    K *= x
                    x = x ** 2
                    n = (n - 1) // 2
                else:
                    x = x ** 2
                    n = n // 2
            return K * x
