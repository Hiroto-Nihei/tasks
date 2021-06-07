# 10までの3と5の倍数の和は、
# 3の倍数: 3 6 9
# 5の倍数: 5 10
# = 33
#
#
# 10000000の場合の和は？
#target = 1000

def multiple(thistarget = 10000000):
 summary_three = 0
 summary_five = 0
 summary_total = 0
 for f in range(0,thistarget+1,3): #1000万までの3の倍数を合計する
     summary_three += f
 print(summary_three)

 for ff in range(0,thistarget+1,5): #　   ”　  5の倍数を合計する
  summary_five += ff
 print(summary_five)
 print("3と5の倍数の和は",summary_three + summary_five)

 for fff in range(0,thistarget+1,15):
     summary_total += fff
 summary_t = summary_three + summary_five -summary_total
 print(summary_t)
multiple()

# def anothersolusion():
#  s_t
#  s_f