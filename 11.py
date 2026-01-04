# 假設我們列出前5個二進位小數
numbers = [
    "0.00000",
    "0.01011",
    "0.11100",
    "0.10101",
    "0.01110"
]

print("原始列表:")
for n in numbers:
    print(n)

# 對角線法則生成新數字
new_number = ""
for i, num in enumerate(numbers):
    # 取小數點後第 i 位
    digit = num[i+2]  # i+2 因為索引0是'0', 索引1是'.'
    # 反轉 0->1, 1->0
    new_digit = "1" if digit == "0" else "0"
    new_number += new_digit

new_number = "0." + new_number
print("\n生成的新數字（對角線法則）:")
print(new_number)

# 檢查新數字是否在原列表中
if new_number in numbers:
    print("\n錯誤：新數字在列表中")
else:
    print("\n成功：新數字不在列表中")
