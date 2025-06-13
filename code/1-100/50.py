# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
from typing import Any
from time import time
class Solution:
    def myPow(self, x: float, n: int) -> float: 
        # brute force
        if n == 0: # 0乗は1
            return 1
        
        if n < 0: # 指数が負の時は逆数
            x = 1 / x
            n = -n 

        ans = 1
        for i in range(n):
            ans *= x
        return ans
    
    def myPow2(self, x: float, n: int) -> float: 
        # recursive
        def calc_pow(x: float, n: int) -> float:
            if n == 0:
                return 1
            
            # 偶数の場合 x^n = (x^2)^(n/2)
            # 奇数の場合 x^n = x * (x^2)^(n/2)
            if n % 2 == 0:
                return calc_pow(x*x, n//2)
            else: # 奇数の場合
                return x * calc_pow(x*x, n//2)
        
        if n < 0: # 指数が負の時は逆数
            x = 1 / x
            n = -n 
        
        return calc_pow(x, n)

    def myPow3(self, x: float, n: int) -> float: 
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n 
        
        ans = 1
        current_product = x

        while n > 0:
            if n % 2 == 1: # nが奇数なら現在の累乗を結果にかける
                ans *= current_product

            current_product *= current_product
            n //= 2

        return ans


def test_pow():
    x = 2.0
    n = 10
    
    # 各メソッドの実行時間を計測
    start = time()
    result1 = Solution().myPow(x, n)
    end = time()
    print(f"myPow: {result1}, 時間: {(end - start)*1000:.3f}ms")
    
    start = time()
    result2 = Solution().myPow2(x, n)
    end = time()
    print(f"myPow2: {result2}, 時間: {(end - start)*1000:.3f}ms")
    
    start = time()
    result3 = Solution().myPow3(x, n)
    end = time()
    print(f"myPow3: {result3}, 時間: {(end - start)*1000:.3f}ms")

test_pow()

