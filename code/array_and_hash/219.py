from typing import List
from time import time

class Solution():
    def containsNearbyDuplicate_brute_force(self, nums: List[int], k: int) -> bool:
        # brute force
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False
    
    def containsNearbyDuplicate_hash_map(self, nums: List[int], k: int) -> bool:
        # hash map
        # 各値の最新のインデックスを記録する key: 値, value: インデックスにする
        index_map = {}

        for i, num in enumerate(nums):
            # 同じ値がすでに存在する場合
            if num in index_map: # numがkeyに存在するかを確認
                # インデックスの差がk以下であるかを確認
                if i - index_map[num] <= k:
                    return True
            # 現在のインデックスを更新
            index_map[num] = i
        return False

class Testcase:
    def __init__(self):
        self.solution = Solution()

    def load_large_test_case(self, filename):
        # 大規模なテストケースをファイルから読み込む
        try:
            with open(filename, 'r') as file:
                content = file.read().strip()
                # カンマで区切られた数値をリストに変換
                nums = list(map(int, content.split(',')))
                # kの値を設定
                return nums
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except ValueError:
            print("Error in converting file content to integers. Please check the file format.")

    
    def run_tests(self, large_test_case=None):
        test_cases = [
            ([1, 2, 3, 1], 3, True),
            ([1, 0, 1, 1], 1, True),
            ([1, 2, 3, 1, 2, 3], 2, False),
            ([1, 2], 0, False),
            ([1, 2, 3, 4, 5], 5, False)
        ]

        # 大規模なテストケースの読み込み
        if large_test_case:
            nums = self.load_large_test_case(large_test_case)
            if nums:
                test_cases.append((nums, 35000, False))
            
        # Brute Force Tests
        start_time = time() 
        for i, (nums, k, expected) in enumerate(test_cases):
            result_bf = self.solution.containsNearbyDuplicate_brute_force(nums, k)
            print(f"Test case {i+1} (Brute Force): {result_bf} | Expected: {expected} |")
        
        end_time = time()
        print(f"Brute Force tests completed in {end_time - start_time:.6f} seconds.\n")

        # Hash Map Tests
        start_time = time()
        for i, (nums, k, expected) in enumerate(test_cases):
            result_hm = self.solution.containsNearbyDuplicate_hash_map(nums, k)
            print(f"Test case {i+1} (Hash Map): {result_hm} | Expected: {expected} |")
        end_time = time()
        print(f"Hash Map tests completed in {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    testcase = Testcase()
    testcase.run_tests("../../datasets/219_test.txt")    