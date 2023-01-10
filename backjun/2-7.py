
# 주사위 세개



#  a, b, c = map(int, input().split())

# if(a == b == c):
#     same = a
# elif(a == b):
#     same = a
# elif(a == c):
#     same = a
# elif(b == c):
#     same = b

# if(a > b > c):
#     big = a
# elif(a > c > b):
#     big = b
# elif(b > a > c):
#     big = b
# elif(b > c > a):
#     big = b
# elif(c > a > b):
#     big = c
# elif(c > b > a):
#     big = c


# if(a == b == c):
#     m = 10000 + same * 1000

# elif(a == b or a == c or b == c):
#     m = 1000 + same * 100

# elif(a != b and a != c and b != c):
#     m = big * 100


# print(m)

a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c))