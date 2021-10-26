# 문자열 조작
# 02 문자열 뒤집기

# 문제: 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며 리스트 내부를 직접 조작하라.
# 풀이 1. 투 포인터를 이용한 스왑 (2개의 포인터로 범위를 좁혀가며 스왑)

class ans1():
    def reverseString(self, s: list) -> list:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

ans1 = ans1()
print(ans1.reverseString(["h","e","l","l","o"]))


# 풀이 2. Pythonic
class ans2():
    def reverseString(self, s: list) -> list:
        s.reverse()

        return s

ans2 = ans2()
print(ans2.reverseString(["h","e","l","l","o"]))

# 03 로그 파일 재정렬
""" 로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2 .문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.
예시) logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']
print out -> ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
"""
class reorder_log_1():
    
    def reorder_log(self, logs: list) -> list:
        letters = []
        digits = []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 2개의 키를 람다 표현식으로 정렬
        # sort 함수 -> key 매개변수 활용하여 key값을 기준으로 정렬되고 오름차순으 디폴트.
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']
reorder_log = reorder_log_1()
print(reorder_log.reorder_log(logs))












