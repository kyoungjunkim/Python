"""
날짜 : 2023/01/02
이름 : 김경준
내용 : 파이썬 기본입출력 실습하기
"""

#파이썬입력
num = input('숫자입력 : ')

#파이썬출력
print('num : ', num)
print('num type : ', type(num))

#문자열 숫자 변환
r1 = int(num) + 1
print('r1 : ',r1)

# 출력 옵션
print('010','1234','5678',sep='-')
print('Hello', end='~ ') #다음 출력만과 한줄로 출력
print('Python', end=' ') 
print('Programming')

#서식문자
print('%d년 %d월 %d일 %s요일' % (2023,1,2,'월'))

#포맷문자
print('{}년 {}월 {}일 {}요일'.format(2023,1,2,'월'))


