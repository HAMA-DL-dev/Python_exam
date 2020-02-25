061
"""다음 코드의 결괏값에 대해 예측하여라

interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
print(interest_0)"""

def answer():
    print("'Naver', 'LG전자', 'SK Hynix'")


062
"""다음 코드의 결괏값에 대해 예측하여라

interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:2]
interest_1[0] = 'Naver'
print(interest_0)"""

def answer():
    print("'Naver', 'LG전자'")

063
"""my_variable 이름의 비어있는 튜플을 만들라."""
my_varialbe=()



064
"""다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.

>> t = (1, 2, 3)
>> t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment"""
def answer():
    print("자료형 유형 중 하나인 튜플은 입력값 수정이 불가능하다.")



065
"""숫자 1 이 저장된 튜플을 생성하라."""

one=(1)

066
"""아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?

t = 1, 2, 3, 4"""

def answer():
    print("정수 int이다.")



067
"""변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.

t = ('a', 'b', 'c')"""

def answer():
    print("t=('A','b','c')를 새롭게 지정한다.")
    print("
     t = ('a', 'b', 'c')에서
     t=(t[0].upper,t[1],t[2])
    ")


068
"""다음 튜플을 리스트로 변환하라.

interest = ('삼성전자', 'LG전자', 'SK Hynix')"""

def answer():
    interest = ('삼성전자', 'LG전자', 'SK Hynix')
    data=list(interest)
    print(data)


069
"""다음 리스트를 튜플로 변경하라.

interest = ['삼성전자', 'LG전자', 'SK Hynix']"""

def answer():
    interest = ['삼성전자', 'LG전자', 'SK Hynix']
    data=tuple(interest)
    print(data)

070
"""아래 코드의 실행 결과를 예측하라

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a + b + c)"""
def answer():
    print("이 경우 언패킹(unpacking)이라고 해서 튜플안의 자료가 변수의 개수와 동일하면서 순서대로 변수에 입력되는 구조.")
    print("따라서
    a=my_tuple[0]
    b=my_tuple[1]
    c=my_tuple[2]이므로
    답은 6이된다.")
