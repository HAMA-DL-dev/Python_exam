051
"""price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)

price = ['20180728', 100, 130, 140, 150, 160, 170]
출력 예시:
[100, 130, 140, 150, 160, 170]"""
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

052
"""슬라이싱을 사용해서 홀수만 출력하라.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
실행 예:
[1, 3, 5, 7, 9]"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

053
"""슬라이싱을 사용해서 짝수만 출력하라.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
실행 예:
[2, 4, 6, 8, 10]"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

054
"""슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.

nums = [1, 2, 3, 4, 5]
실행 예:
[5, 4, 3, 2, 1]"""
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

055
"""
interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver']
interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

출력 예시:
삼성전자 Naver"""
interest = ['삼성전자', 'LG전자', 'Naver']
del interest[1]
print(interest)
# 또는
print(interest[0], interest[2])


056
"""
interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

출력 예시:
삼성전자 LG전자 Naver SK하이닉스 미래에셋대우"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest)

057
"""
interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

출력 예시:
삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"""

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest,sep='/')
058
"""interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.

출력 예시:
삼성전자
LG전자
Naver
SK하이닉스
미래에셋대우"""

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))

059"""
회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.

string = "삼성전자/LG전자/Naver"
이를 interest 이름의 리스트로 분리 저장하라.

실행 예시
>> print(interest)
['삼성전자', 'LG전자', 'Naver']"""
string = "삼성전자/LG전자/Naver"
# 이때 print(string.index("/"))와 'LG전자'문자열 크기를 이용하여 slash의 인덱스 번호를 찾는다.
interest = [string[0:4], string[5:9], string[10:15]]
print(interest)

060"""
회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.

string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
이를 interest 이름의 리스트로 분리 저장하라.

실행 예시
>> print(interest)
['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']"""
interest = [string[0:4], string[5:9], string[10:15], string[16:22], string[23:29]]

#slahs의 인덱스 번호를 하나하나 찾는게 번거롭다. 무얼 어쩌면 좋을까 하다가 split함수 기능을 이용해보았다.
interest = string.split('/') 
print(interest)
