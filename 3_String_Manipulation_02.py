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
