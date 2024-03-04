#sys: 시스템과 관련된 함수제공

import sys
#1 
print(sys.path)
#내가 만든 모듈을 systen path에 등록하거나 삭제할때

#2 버전확인
print(sys.version)

#3 프로그램 종료 : 프로그램 닫기
#sys.exit()

#4 현재 설정 된 인코딩 옵션 리턴
print(sys.getdefaultencoding()) #utf-8

#5 윈도우 버전
print(sys.getwindowsversion()) #sys.getwindowsversion(major=10, minor=0, build=19043, platform=2, service_pack='')

#6 파이썬 설치경로
print(sys.prefix)

# print(chr(76)) L
# print(chr(84)) T
# print(chr(79)) O
# print(chr(86)) V
# print(chr(69)) E
# print(chr(73)) I
# print(chr(51)) 3
# print(chr(48)) 0
# print(chr(87))
