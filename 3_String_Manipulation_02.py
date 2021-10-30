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


# 04 가장 흔한 단어
""" 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력. 대소문자 구분 하지 않으며 구두점도 무시"""
# (1) List Comprehension, Counter
# defaultdict(): default 객체는 존재하지 않는 키를 조회할 때, 에러 메시지를 출력하는 대신 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성

import collections
import re

class Count():
    
    def most_common_words(self, paragraph: str, banned: list) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 값을 most_common(1)로 추출. 문제의 입력값에서는 [('ball', 2)]가 되며 이 값의 [0][0]을 추출해서 key인 'ball'을 출력하낟.
        
        return counts.most_common(1)[0]  

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
Count = Count()
print(Count.most_common_words(paragraph, banned))


# defaultdict 활용 (디폴트: 0)
class Count2():
    
    def most_common_words2(self, paragraph: str, banned: list) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1

        return max(counts, key=counts.get)  # 딕셔너리.get(접근할 키)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
Count2 = Count2()
print(Count2.most_common_words2(paragraph, banned))


# 05 그룹 애너그램
"""문자열 배열을 받아 내러그램 단위로 그룹핑하라.
애너그램: 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것. '문전박대', '대박전문' """

# 풀이 1. 정렬하여 딕셔너리에 추가
# sroted()로 정렬한 리스트 형태의 결과를 join()으로 합쳐서 딕셔너리 구성

def Ana(strs: list) -> list:
    anagrams = collections.defaultdict(list)   # 디폴트 값이 리스트. 값을 지정하지 않으면 빈 리스트

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)    # aet, ant, abt 라는 3개의 key 생성. 거기에 해당하는 word를 추가

    return anagrams.values()

strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(Ana(strs))


# 여러가지 정렬방법




