# 문자열 조작
# 01 유요한 팰린드롬 (뒤집어도 같은 말)

# 풀이 1: 리스트로 변환
# 조건: 대소문자 여부를 구분하지 않음

class Palin:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():    # 영문자, 한글, 숫자이면 True
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():   # 맨 앞의 값과 맨 뒤의 값을 비교
                return False
        
        return True

palin = Palin()
print(palin.isPalindrome("A man, A plan, a canal: Panama"))
print(palin.isPalindrome("abbba"))
print(palin.isPalindrome("acbba"))
print(palin.isPalindrome("김밥김"))


# 풀이 2: 데크 자료형을 이용한 최적화
# deque를 사용하면 속도를 좀 더 높일 수 있음

import collections
class Palin2:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            # Deque의 popleft 활용
            if strs.popleft() != strs.pop():
                return False
            
        return True

palin2 = Palin2()
print('\n\n')
print(palin2.isPalindrome("A man, A plan, a canal: Panama"))
print(palin2.isPalindrome("abbba"))
print(palin2.isPalindrome("acbba"))
print(palin2.isPalindrome("김밥김"))
print(palin2.isPalindrome("김밥집"))


# 풀이 3: 슬라이싱
# 2번 풀이보다 속도 2배 빠름
import re
def isPalindrome(s: str) -> bool:
    s = s.lower()
    # 정규식
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # 뒤집기

print('\n')
print(isPalindrome("김밥김"))
print(isPalindrome("abcbb"))