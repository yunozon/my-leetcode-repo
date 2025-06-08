# あるリストが渡されたときに、そのリストの要素が重複しているかどうかをチェック
# 重複していればTrue, 重複していなければFalse

from time import time
from typing import List
class Solution:
    # 初期条件
    # Brute Force
    def containsDuplicate_brute_force(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return False
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False

    # Sort
    def containsDuplicate_sort(self, nums: list[int]) -> bool:
        """
        ある要素とその次の要素を比較して、同じであれば重複があると判断する
        時間計算量はO(n log n)
        """
        if len(nums) < 2:
            return False
        # ソートされたリストを作成
        nums_sorted = sorted(nums)
        # ソートされたリストの隣接要素を比較
        for i in range(len(nums_sorted) - 1):
            if nums_sorted[i] == nums_sorted[i + 1]:
                return True
        return False
    # Hash Set
    def containsDuplicate_hash_set(self, nums: List[int]) -> bool:
        """
        ハッシュセットを使用して、要素の重複をチェック
        時間計算量はO(n)
        """
        if len(nums) < 2:
            return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def MySolution(self, nums: List[int]) -> bool:
        """
        自分の解法
        ハッシュセット
        setを使用して、元のリストと長さを比較することで重複をチェック
        時間計算量はO(n)
        """
        output = len(set(nums)) != len(nums)
        return output
    # Hash Map
    def containsDuplicate_hash_map(self, nums: List[int]) -> bool:
        """
        ハッシュマップを使用して、要素の重複をチェック
        時間計算量はO(n)
        """
        count_map = {}
        for num in nums:
            if num in count_map:
                return True
            count_map[num] = 1
        return False

test_case = [
    ([1, 2, 3, 4, 5], False),  # False
    ([1, 2, 3, 4, 5, 1], True),  # True
    ([1], False),  # False
    ([], False),  # False
    ([1, 2, 3, 2], True),  # True
    ([1, 1, 1, 1], True),  # True
    ([-1, -2, -3, -4], False),  # False
    ([-1, -2, -3, -4, -1], True),  # True
    ([0, 0, 0, 0], True),  # True
    ([1000000, 1000001, 1000002, 1000003, 1000004], False),  # False
    ([1000000, 1000001, 1000002, 1000003, 1000000], True),  # True
]

def test_all_method(test_case):
    """
    全てのメソッドをテストする
    """
    solution = Solution()
    methods = [
        ("brute force", solution.containsDuplicate_brute_force),
        ("sort", solution.containsDuplicate_sort),
        ("hash set", solution.containsDuplicate_hash_set),
        ("my solution", solution.MySolution),
        ("hash map", solution.containsDuplicate_hash_map)
    ]
    for method_name, method in methods:
        print(f"Testing {method_name} method:")
        for i, (nums, answer) in enumerate(test_case):
            start_time = time()
            result = method(nums)
            if result != answer:
                check = "Incorrect"
            else:
                check = "Correct"
            end_time = time()
            print(f"Test case {i + 1}: {nums} -> {result}, {check} (Time: {end_time - start_time:.6f} seconds)")
        print("\n")

if __name__ == "__main__":
    test_all_method(test_case)
