# 242. Valid Anagram
from collections import Counter, defaultdict

class Solution():



    def isAnagram_BruteForce(self, s, t):
        """
        計算量 : O(n^2)
        """
        # アナグラムになる条件を満たすかどうか
        if len(s) != len(t):
            return False


        s_list = list(s)
        t_list = list(t)

        for s_char in s_list:
            if s_char in t_list: # sの文字がtに入っていたら
                t_list.remove(s_char) # tの文字リストから一個消す
            else: 
                return False
                
        return len(t_list) == 0
    
    def isAnagram_Counter(self, s, t):
        if Counter(s) == Counter(t): # それぞれの文字と出現回数が同じなら
            return True
        else:
            return False
    
    def isAnagram_Sort(self, s, t):
        return sorted(s) == sorted(t)

    def isAnagram_HashTable(self, s, t):
        # アナグラムになる条件を満たすかどうか
        if len(s) != len(t):
            return False
        s_table = {}
        t_table = {}

        for s_char, t_char in zip(s, t):
            s_table[s_char] = s_table.get(s_char, 0) + 1
            t_table[t_char] = t_table.get(t_char, 0) + 1

        return s_table == t_table 
    
    def isAnagram_Array(self, s, t):
        """
        配列法（小文字のアルファベットのみの場合）
        計算量: O(n)
        空間計算量: O(1) - 固定サイズの配列
        """

        if len(s) != len(t):
            return False
        
        # 26個のアルファベット用の配列
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        # すべて0なら,両方の文字列が同じ回数存在
        return all(c == 0 for c in count)
    
    def isAnagram_DefaultDict(self, s, t):
        """
        defaultdict使用法
        計算量: O(n)
        空間計算量: O(1) - 最大26文字のアルファベットのみ
        """
        if len(s) != len(t):
            return False
        
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for char in s:
            s_count[char] += 1
        
        for char in t:
            t_count[char] += 1
        
        return s_count == t_count

    def Test(self, s1, t1, s2, t2):
        print("-------------True---------------")
        print(self.isAnagram_BruteForce(s1, t1))
        print(self.isAnagram_Counter(s1, t1))
        print(self.isAnagram_Sort(s1, t1))
        print(self.isAnagram_HashTable(s1, t1))
        print(self.isAnagram_Array(s1, t1))
        print(self.isAnagram_DefaultDict(s1, t1))
        
        print("-------------False---------------")
        print(self.isAnagram_BruteForce(s2, t2))
        print(self.isAnagram_Counter(s2, t2))
        print(self.isAnagram_Sort(s2, t2))
        print(self.isAnagram_HashTable(s2, t2))
        print(self.isAnagram_Array(s2, t2))
        print(self.isAnagram_DefaultDict(s2, t2))


# Test True
s1 = "anagram"
t1 = "nagaram"

# Test False
s2 = "cat"
t2 = "rat"

sol = Solution()
sol.Test(s1, t1, s2, t2)
