141
"""my_list 에서 대문자만 화면에 출력하라.

my_list = ["A", "b", "c", "D"]
실행 예:
A
D
참고 : isupper() 메서드는 대문자 여부를 판별한다.

>> "A".isupper()
True
>> "a".isupper()
False"""
my_list = ["A", "b", "c", "D"]
for list in my_list:
    if list.isupper()==True:
        print(list)

------------------------------------------------------------------------------
142
"""my_list 에서 소문자만 화면에 출력하라.

my_list = ["A", "b", "c", "D"]
실행 예:
b
c"""
my_list = ["A", "b", "c", "D"]
for list in my_list:
    if list.isupper()==False:
        print(list)

------------------------------------------------------------------------------
143
"""문자열의 upper() 메서드는 문자열을 대문자로 변경하고, lower() 메서드는 소문자로 변환한다.

>> 'korea'.upper()
KOREA
>> 'KOREA'.lower()
korea
리스트의 문자를 대문자는 소문자로, 소문자는 대문자로 변환하라.

my_list = ["A", "b", "c", "D"]
실행예:
aBCd"""
my_list = ["A", "b", "c", "D"]
for list in my_list:
    if list.isupper()==True:
        print(list.lower())
    else:
        print(list.upper())

------------------------------------------------------------------------------
144 ******
"""파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split 메서드를 사용)

file_list = ['hello.py', 'ex01.py', 'ch02.py', 'intro.hwp']
실행예:
hello
ex01
ch02
intro"""
file_list = ['hello.py', 'ex01.py', 'ch02.py', 'intro.hwp']
for list in file_list:
    print(list.split(".")[0])


------------------------------------------------------------------------------
145
"""파일 이름이 리스트에 저장되어 있을 때 확장자가 *.h인 파일을 출력하라.

filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']
실행예:
intra.h
define.h"""
filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']
for name in filenames:
    if name.split(".")[1]==".h":
        print(name)

------------------------------------------------------------------------------
146
"""파일 이름이 리스트에 저장되어 있을 때 확장자가 .h나 .c인 파일을 화면에 출력하라.

filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']
실행예:
intra.h
intra.c
define.h"""

filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']
for name in filenames:
    if name.split(".")[1]==".h" or name.split(".")[1]==".c" :
        print(name)

------------------------------------------------------------------------------
147
"""my_list에서 양수만 new_list 이름의 리스트에 저장하라.

my_list = [3, -20, -3, 44]
실행예:
>> new_list
[3, 44]"""
new_list=[]
my_list = [3, -20, -3, 44]
for list in my_list:
    if list>0:
        new_list.append(list)

print(new_list)
------------------------------------------------------------------------------
148
"""my_list 에서 대문자만을 upper_list에 저장하라.

my_list = ["A", "b", "c", "D"]
실행 예:
>> upper_list
["A", "D"]"""
upper_list=[]
my_list = ["A", "b", "c", "D"]
for list in my_list:
    if list.isupper()==True:
        upper_list.append(list)

print(upper_list)

-----------------------------------------------------------------------------
149 *****
"""my_list의 값을 sole_list에 저장하라. 단, 중복된 값은 제거한다.

my_list = [3, 4, 4, 5, 6, 6]
실행 예:
>> sole_list
[3, 4, 5, 6]"""
sole_list=[]
my_list = [3, 4, 4, 5, 6, 6]
for list in my_list:
    if list not in sole_list:
        sole_list.append(list)


------------------------------------------------------------------------------
150
"""내장 함수를 사용하지 않고 반복문을 사용해서 my_list에 저장된 모든 수의 합를 출력하라

my_list = [3, 4, 5]
출력예:
12"""
all=0
my_list = [3, 4, 5]
for list in my_list:
    all=all+list #all+=list

print(all)
