# type hint

def func(a: int) -> bool:
    if a in [1, 2, 3, 4, 5]:
        print(True)
    else:
        print(False)

# func(2)


# filter(결과 타입이 bool일 때), map(결과 타입이 bool 이외일 때)
a = [1, 2, 3, 4, 5]
# print(list(filter(lambda x: x < 3, a)))
# print(list(map(lambda x: x + 1, a)))


# Generator
# yield문을 사용하면 제너레이터 리턴할 수 있다.
# yield는 return과 달리, 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 의미로, 중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행된다.

def get_natural_number():
    n = 0
    while 1:
        n += 1
        yield n

# 제너레이터에서 다음 값을 생성하려면 next()로 추출하면 된다
g = get_natural_number()
# for _ in range(0, 100):
#     print(next(g))


# 제너레이터는 다음처럼 여러 타입의 값을 하나의 함수에서 생성하는 것이 가능
def generator():
    yield 1
    yield 'string' 
    yield True

ge = generator()
print(next(ge))
print(next(ge))
print(next(ge))

