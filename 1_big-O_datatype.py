""" 
<빅오>
빅오는 입력값이 커질 때 알고리즘의 실행시간(시간 복잡도)과 함께 공간 요구사항(공간 복잡도)이 어떻게 증가하는지를 분류하는 데 사용,
알고리즘의 효율성을 분석하는 데에도 매우 유용

빅오(O, big-O) : 입력값이 무한대로 향할 때 함수의 상한을 설명하느 수학적 표기 방법

먼저, 빅오는 점근적 실행 시간(Asymptotic Running Time)을 표기할 때 가장 널리 쓰이는 수학적 표기법
점근적 실행 시간 = 입력값 n이 커질 때, 즉 입력값이 무한대를 향할 때 lim(n->무한) 함수의 실행 시간의 추이를 의미. 다시 말하면 시간 복잡도.
시간 복잡도 = 어떤 알고리즘을 수행하는 데 걸리는 시간을 설명하는 계산 복잡도. 이 계산 복잡도를 표기하는 대표적인 방법이 빅오

빅오로 시간 복잡도를 표현할 때는 최고차항만을 표기하며, 상수항은 무시한다.

빅오는 상한을 의미한다. 상한이란, 함수 f(n)이 있을 때, 가장 늦게 실행될 때를 의미한다. 
빅오 표기법은 n이 매우 클 때의 전체적인 큰 그림에 집중한다.
즉, 빅오 표기법이란, 주어진(최선/최악/평균) 경우의 수행 시간의 상한을 나타낸다.
"""

#<자료형>
#is와 ==
#is는 id()값을 비교하는 함수

a = [1, 2, 3]
print(a == a)  # True 출력

print(a == list(a))  # True 출력

print(a is a)  # True 출력

print(a is list(a)) # False 출력 (값은 동일하지만, list()로 한 번 더 묶어주면, 별도의 객체로 복사되면서 다른 ID를 갖게 됨)

# deepcopy로 복사한 결과 역시 값은 동일하지만, ID는 다르기 때문에 ==로 비교하면 True, is로 비교하면 False.