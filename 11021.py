t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a+b}")

# fstring: f'문자열 {변수} 문자열'
# 예제 name = 'Song' sex = 'male' f'Hi, I am {name}. I am {sex}.' >>> 'Hi, I am song. I am male.'