from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        """
        ソートを使ってアナグラムをグループ化する
        """

        # ソート済み文字列をキーとしてグループ化
        anagram_groups = defaultdict(list)
        for str in strs:
            # 文字列をソートしてキーにする
            # アナグラム同士は同じソート結果になる
            sorted_str = ''.join(sorted(str)) # ['a', 'b', 'c'] -> 'abc'にする
            anagram_groups[sorted_str].append(str)

        # 辞書の値（リスト）を結果として返す
        return list(anagram_groups.values()) # keyはソートした文字列、valueはアナグラムのリスト
    

def Test():
    sol = Solution()
    # Example 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(strs1))  # Expected: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    # Example 2
    strs2 = [""]
    print(sol.groupAnagrams(strs2))  # Expected: [[""]]

    # Example 3
    strs3 = ["a"]
    print(sol.groupAnagrams(strs3))  # Expected: [["a"]]


if __name__ == "__main__":
    Test()
