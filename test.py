# 1. 백준 알고리즘 9488번
# n = int(input())
# if n >= 90:
#     print('A')
# elif n >= 80:
#     print('B')
# elif n >= 70:
#     print('C')
# elif n >= 60:
#     print('D')
# else:
#     print('F')

# 2. 백준 알고리즘 2753번
# n = int(input())

# if (n % 4 == 0 and n % 100 != 0) or n%400 == 0:
#     print(1)
# else :
#     print(0)

# 3. 백준 알고리즘 2884번
# l = input().split()

# h = int(l[0])
# m = int(l[1])

# r = m - 45
# if r >= 0:
#     m = r
# else : 
#     h = h-1
#     if h < 0:
#         h = 24 + h
#     m = 60 + r
# print(h, m)