from numbers import Real


def isDigit(n):
    for n1 in n:
        if ord(n1)>=ord('0') and ord(n1)<=ord('9'):
            return False
    return True # 마지막 까지 가서도 return False가 안됐으면 숫자로만 구성
        
n = input("값 ?") # 23  0-48, 1-49 2-50 3-51
print(ord(n[0])) # 코드값 확인 ord(문자) - 문자에 해당하는 유니코드값을 반환
print(ord(n[0])) # chr(코드) - 문자를 반환

if isDigit(n)==True: # if isDigit(n):
    n = int(n)*10
    print(n)
else:
    print(f"{n}은 정수가 아닙니다.")

