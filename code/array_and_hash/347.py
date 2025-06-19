from collections import defaultdict

class Solution:
    def topKFrequent_My_Ans(self, nums, k):
        dicts = defaultdict(int)
        ans = []
        for num in nums:
            dicts[num] += 1 # numをkeyにして何回あるかを辞書に格納

        sorted_dict = sorted(dicts.items(), key=lambda x:x[1], reverse=True) # value(回数)の値が大きい順に並び替え
        
        for i in range(k):
            ans.append(sorted_dict[i][0])
        # print(ans)
        return ans
    
    def topKFrequent_Brute_Force(self, nums, k):
        """
        k=1のとき
        set(nums)で出現する数字をまとめている
        そして、1つずつピックアップ(target)して、その数字(target)と入力したリストの要素を
        比較して、同じだったらcountしていく。
        例えば : 100をピックアップしたら、その100と一致するnumsの要素を1つずつ確かめ、
        同じだったらcountしていく。
        """
        result = []

        # 既に選ばれた要素を記録
        selected = set()

        for _ in range(k):
            print(f"k : {_}")
            max_count = 0
            max_num = None

            # 各数字の出現回数を数える
            for target in set(nums):
                print(f"target : {target}")
                if target in selected:
                    print(f"{target}は既に選ばれている要素です(既出です)")
                    continue
                    
                count = 0
                print(f"{target}は初めて選ばれた要素です")
                for num in nums:
                    print(f"num: {num}")
                    if num == target:
                        count += 1

                if count > max_count:
                    print(f"target:{target}のときにcount{count}更新した")
                    max_count = count
                    max_num = target
                
            result.append(max_num)
            selected.add(max_num)
            print(f"result : {result} , selected : {selected}")
        print("result", result)
        return result


sol = Solution()
nums1 = [1]
nums2 = [100, 100, 100, 200, 300, 200]
k1 = 1
k2 = 2
# sol.topKFrequent_Brute_Force(nums1, k1)
sol.topKFrequent_Brute_Force(nums2, k2)

