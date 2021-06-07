 # 10までの自然数の2乗の合計は
# 1^2 + ...... + 10^2 = 385
#
# (1 + 2 ...... + 10)^2 = 55^2 = 3025
#
# この二式の差は 3025 - 385 = 2640である。
#
# 100までの自然数の2乗の合計と合計の２乗の差を求めてください。
stock_nijoul = 0
stock_nijourr = 0
targetnumber = 101
for prime_l in range(1,targetnumber): #自然数の二乗
    prime_l *= prime_l
    stock_nijoul += prime_l
print(stock_nijoul)

for prime_r in range(1,101):#自然数の合計の二乗
    stock_nijourr += prime_r
stock_nijourr * 2
print(stock_nijourr)

#print(stock_nijoul - stock_nijourr)
#_____________________________________________5.24の回答

# # （1-100）**2 - 100**2
# beki = 2
# count = 1
# lTotal = 0
# rTotal = 0
# for an in range(count, 101):
#     rTotal_2 = an * an
#     # print(rTotalTotal) #右辺の解
#     count_2 = an
#     # lTotal_2 = anfi + an
#     # print(lTotal_2)
#
# total = 0
# i = 1
# ii = 2
# sigma_t = 0
# for an in range(1, 101):
#     total += an ** ii
#     sigma_t += an
# total_t = sigma_t ** ii
# allTotal = total_t - total
# print(allTotal)
#_____________________________________________________________初回の回答

# 10までの3と5の倍数の和は、
# 3の倍数: 3 6 9
# 5の倍数: 5 10
# = 33
#
#
# 10000000の場合の和は？
# targetnumber = 10000000
# stock = 0
# stock_two = 0
# for f in range(0,targetnumber,3): #1000万までの3の倍数を合計する
#     stock += f
# print(stock)
#
# for ff in range(0,targetnumber,5): #　   ”　  5の倍数を合計する
#  stock_two += ff
# print(stock_two)
# print("3と5の倍数の和は",stock + stock_two)
#______________________________________________________________
