001
# 화면에 Hello World 문자열을 출력하라.
print("Hello World")
print('Hello World')

002
# 화면에 Mary's cosmetics을 출력하라. (중간에 '가 있음에 주의.)
print('Mary\'s cosmetics')
print("Mary's cosmetics")

003
"""화면에 아래 문장을 출력하라. (중간에 "가 있음에 주의.)
신씨가 소리질렀다. "도둑이야"."""

print('신씨가 소리질렀다. \"도둑이야\"')
print('신씨가 소리질렀다. \"도둑이야\"')

004
# 화면에 C:\Windows를 출력하라.
print("C:\\Windows")
print('C:\\Windows')

005
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명하라.
print("안녕하세요.\n만나서\t\t반갑습니다.")

def answer():
    print("\\n은 줄바꿈, \\t는 10칸 공백 띄우기 역할을 수행 ")

006
# print 함수에 두 개의 단어를 입력한 예제이다. 아래 코드의 출력 결과를 예상하라.

print ("오늘은", "일요일")

007
"""print() 함수를 사용하여 다음과 같이 출력하라.
naver;kakao;sk;samsung"""
print("naver","kakao","samsung",sep=';')

008
""" print() 함수를 사용하여 다음과 같이 출력하라.
naver/kakao/sk/samsung"""
print("naver","kakao","samsung",sep='/')

009
"""다음 코드를 수정하여 줄바꿈이 없이 출력되도록 하라. (힌트: end='') print 함수는 두 번 사용한다.
세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용된다.
print("first");print("second")
"""
print("first",end=' ');print("second")


010
"""string 문자열의 길이를 구하여라.
string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
"""
string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
a=len(string)
print(a)
