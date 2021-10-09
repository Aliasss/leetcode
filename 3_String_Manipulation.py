# 문자열 조작
# 01 유요한 팰린드롬 (뒤집어도 같은 말)

# 풀이 1: 리스트로 변환
# 조건: 대소문자 여부를 구분하지 않음

class Palin:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():    # 영문자, 숫자 여부 판별
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                print(False)
        
        print(True)

palin = Palin()
palin.isPalindrome("A man, A plan, a canal: Panama")