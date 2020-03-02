121
"""아래 for 문에서 print 문은 몇 번 호출 되는가?

for 변수 in ["가", "나", "다", "라"]:
    print(변수)"""

def answer():
    print("리스트 안에 총 4가지가 있으므로 4번 호출된다.")

-------------------------------------------------------------------------
122
"""아래 코드의 실행 결과를 예측하라.

for 변수 in ["사과", "귤", "수박"]:
    print(변수)"""

def answer():
    print("사과", "귤", "수박",sep='\n')
------------------------------------------------------------------------
123
"""아래 코드의 실행 결과를 예측하라.

for 변수 in ["사과", "귤", "수박"]:
    print(변수)
    print("--")"""

def answer():
    print("사과", "귤", "수박",sep='\n--\n')
-------------------------------------------------------------------------
124
"""아래 코드의 실행 결과를 예측하라.

for 변수 in ["사과", "귤", "수박"]:
    print(변수)
print("--")"""
def answer():
    print("사과", "귤", "수박",sep='\n')
    print("--")
# 사과, 귤, 수박은 한 줄 띄어서 출력 된 뒤에 '--'가 마지막으로 출력된다.
-------------------------------------------------------------------------
125
"""menu 리스트에는 판매중인 메뉴가 저장돼 있다. 아래와 같이 화면에 출력하라.

menu = ["김밥", "라면", "튀김"]
실행 예

오늘의 메뉴:김밥
오늘의 메뉴:라면
오늘의 메뉴:튀김"""
menu = ["김밥", "라면", "튀김"]
for food in menu:
    print("오늘의 메뉴:%s"%food)

-------------------------------------------------------------------------
126
"""portfolio에는 보유중인 주식 목록이 저장돼 있다. 아래와 같이 화면에 출력하라.

portfolio = ["SK하이닉스", "삼성전자", "LG전자"]
실행 예

SK하이닉스 보유중
삼성전자 보유중
LG전자 보유중"""
portfolio = ["SK하이닉스", "삼성전자", "LG전자"]
for com in portfolio:
    print("%s 보유중"%portfolio)

-------------------------------------------------------------------------
127
"""다음과 같이 애완 동물 리스트가 있을 때 애완 동물의 이름과 애완 동물의 글자수를 출력하라.

pets = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']
실행 예

dog 3
cat 3
parrot 6
squirrel 8
goldfish 8"""
pets = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']
for pet in pets:
    print("%s"%pet,"%d"%len(pet))

-------------------------------------------------------------------------
128
"""다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 화면에 출력하라.
단 부가세는 10원으로 가정한다.

prices = [100, 200, 300]
실행 예

110
210
310"""
prices = [100, 200, 300]
for price in prices:
    print(price+10)

-------------------------------------------------------------------------
129 **********
"""prices 리스트에는 가격정보가 문자열로 저장돼 있다.s
prices 리스트에 저장된 모든 데이터를 파이썬 숫자 형으로 변환 후 화면에 출력하라.

prices = ["129,300", "1,000", "2,300"]
실행 예

129300
1000
2300"""
prices = ["129,300", "1,000", "2,300"]
for price in prices:
    temp = price.replace(',', '')
    print(int(temp))

-------------------------------------------------------------------------
130
"""menu 리스트에는 음식이름이 뒤집혀 저장돼 있다. 이를 읽기 좋게 뒤집어서 아래와 같이 출력하라.

menu = ["면라", "밥김", "김튀"]
실행 예

라면
김밥
튀김"""
menu = ["면라", "밥김", "김튀"]
for food in menu:
    print(food[::-1])
