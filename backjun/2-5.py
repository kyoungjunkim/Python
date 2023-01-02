# 알람시계

h, m = map(int, input().split())




if((m-45) < 0):
    h = h - 1
    m = m + 15
else:
    m = m - 45

if(h<0):
    h = 24 + h

print(h, m)