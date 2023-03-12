import os

# 1. 創建txt檔
with open('numbers.txt', 'w') as f:
    for i in range(2, 1001):
        f.write(str(i) + '\n')

# 2. 讀取txt檔
with open('numbers.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f.readlines()]

# 3. 計算所有數的因數和
factors_sum = {}
for number in numbers:
    factor_sum = sum([factor for factor in range(1, number) if number % factor == 0])
    factors_sum[number] = factor_sum

# 4. 判斷完全數
perfect_numbers = []
for number, factor_sum in factors_sum.items():
    if factor_sum == number:
        perfect_numbers.append(number)

# 5. 判斷友好數
amicable_numbers = []
for number, factor_sum in factors_sum.items():
    if factor_sum in factors_sum and factors_sum[factor_sum] == number and factor_sum != number:
        amicable_numbers.append(number)

# 6. 將結果由小到大排序
perfect_numbers.sort()
amicable_numbers.sort()

# 7. 輸出結果
print('完全數：', perfect_numbers)
print('友好數：', amicable_numbers)



