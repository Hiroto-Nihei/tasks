# 二乗差の合計
# 1^2+.......+10^2=385
# (1+2......+10)^2=3025
# この二式の差は3025-385=2640
# 100までの合計と合計の二乗


def differences_and_square_sum(num):
    return pow(sum(range(1, num + 1)), 2) - sum(map(lambda n: n ** 2, range(1, num + 1)))


a = 100
print(differences_and_square_sum(a))