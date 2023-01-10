# 3-1 구구단

N = map(int, input())

for i in range(1, 10):
    mul = N * i
    print('{} * {} = {}'.format(N, i, mul))
