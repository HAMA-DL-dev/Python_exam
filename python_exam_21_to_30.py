#lang='python' 문자열에서 첫번째와 세번째 문자를 출력하라
lang='python'
print(lang[0],lang[2],sep=' ')

#license_plate = "24가 2210"에서 뒤의 네 자리만 출력하라.
license_plate = "24가 2210"
print(license_plate[-4:])

#string = "홀짝홀짝홀짝"에서 '홀' 만 출력하라.
string = "홀짝홀짝홀짝"
print(string[::2])

#string = "PYTHON" 문자열을 거꾸로 뒤집어 출력하라.
string = "PYTHON"
print(string[::-1])

#phone_number = "010-1111-2222"에서 하이푼 ('-')을 제거하고 출력하라.
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))

#위의 결과 값의 숫자를 모두 붙여 출력하라
phone_number = "010-1111-2222"
print(phone_number.replace('-',''))

#url = "http://sharebook.kr" 에 저장된 웹 페이지 주소에서 도메인을 출력하라.
url = "http://sharebook.kr"
print(url[-2:])

#>> lang = 'python'; lang[0] = 'P' ;  print(lang)의 결과를 예상하라.
lang ='python'
lang[0] ='P'
print(lang)

#string = 'abcdfe2a354a32a'소문자 a를 대문자로 변경하여 출력하라.
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))

#코드의 실행 결과를 예측하라.; string = 'abcd';  string.replace('b', 'B');print(string)
string = 'abcd'
string.replace('b', 'B')
print(string)
