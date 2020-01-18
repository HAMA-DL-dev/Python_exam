# 구구단 만들기 예제
a=range(1,10)
for b in a:
  print(2 ,'X', b,'=',2*b)

i=1
while i<=9:
  print(2 ,'X',i,'=',i*2)
  i=i+1

# 카운트 다운 예제 만들기
def countdown(n):
  if n==0:
    print("폭발은 예술이다!")
  else:
    print(n)
    countdown(n-1)

countdown(4)    

# 아르바이트 비용 문제
 
def i_love_money(money):
  print(money,"만원 받았다고 했지?")

  if money<10:
    print("이건 노동 착취야!")

  else:
    print("하하 기운이 나는걸?^^")

i_love_money(10)      
