# （1-100）**2 - 100**2
# 10までの自然数の2乗の合計は
# 1^2 + ...... + 10^2 = 385
#
# (1 + 2 ...... + 10)^2 = 55^2 = 3025
#
# この二式の差は 3025 - 385 = 2640である。
#
# 100までの自然数の2乗の合計と合計の２乗の差を求めてください。

def square(tag = 101): #1^100
 square_num = 0
 for f in range(1,tag):
    square_num += f ** 2
 print(square_num)

 square_numsec = 0
 for ff in range(1,tag):
  square_numsec += ff
  lastnum = square_numsec * 2
 print("合計の二乗の結果",lastnum)
 print("お互いの差は",square_num - lastnum)
square()