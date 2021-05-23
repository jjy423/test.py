# 수열:  수열 또는 열은 수 또는 다른 대상의 순서 있는 나열이다.
# 수열은 자연수의 집합에 정의된 함수라고 할 수 있다.

n, x = map(int, input().split())
num = list(map(int, input().split()))

for i in range(n):
    if num[i] < x:
        print(num[i], end = " ")

# 문제의 조건에 맞게 n, x로 map 함수를 이용해서 10, 5 숫자를 각각 정수(int)로 입력받고
# num 변수를 만들어 둘째 줄에 입력되는 숫자들을 list에 int로 집어넣는다.
# num = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]
# for문을 이용해서 range(n), n = 10이므로 i는 0부터 9까지 입력 된다.
# if문을 이용해서 num[0~9] list에 있는 숫자들이 x인 5보다 작을 때 print 함수를 이용해서 출력하게 된다.

#이때 num[i]를 통해 list 중 5보다 작은 숫자즐 end=" "로 한 칸씩 띄어서 출력하면 된다.