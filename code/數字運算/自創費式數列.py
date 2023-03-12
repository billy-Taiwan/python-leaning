# 定義一個函數，用來計算費式數列的第n項
def fibonacci_sequence(n):
  # 如果n是0或1，則返回n
  if n == 0 or n == 1:
    return n
  # 否則，返回前兩項的和
  else:
    return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

# 測試一下函數的效果
# 輸出費式數列的前10項
for i in range(100):
  print(fibonacci_sequence(i))