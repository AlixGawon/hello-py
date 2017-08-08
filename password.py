# password 검증기

#input()함수로 사용자로부터 패스워드 입력

def password(regulation):
    if regulation.isalnum() and regulation.__len__() >= 8:
        return True
    else:
        return False

# 패스워드 규칙 : 8자 이상이고, 영어와 숫자가 혼합된 형태이여야 함
def main():
    print(password(input()))

main()
