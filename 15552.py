# import: 컴퓨터에서 다른 프로그램으로부터 데이터를 갖고 오는 것.
# 모듈을 갖고 오는 방법
# 1. import 모듈: 모듈 전체를 가져오는 것, 
# 2. from 모듈 import 이름: 원하는 모듈을 집어서 가져오는 것

import sys

T = int(sys.stdin.readline())

for i in range (T):
  A, B = map(int, sys.stdin.readline().split())
  print(A+B)