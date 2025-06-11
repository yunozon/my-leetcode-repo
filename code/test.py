filename  = "../datasets/219_test.txt"
# リストにしてどのくらいのサイズか確認
with open(filename, 'r') as file:
    content = file.read().strip()
    nums = list(map(int, content.split(',')))
    print(f"Number of elements in the file: {len(nums)}")
    print(f"First 10 elements: {nums[:10]}")  # 最初の10個の要素を表示
    print(f"Last 10 elements: {nums[-10:]}")  # 最後の10個の要素を表示