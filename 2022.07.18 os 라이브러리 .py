#os 라이브러리: 
# 파이썬에서 운영체제를 제어하기 위해서 사용
# 현재 폴더 위치는?
# 파일 존재?
# 폴더 존재
# 폴더 생성/삭제
# 이름 변경

import os 
d_name = 'test'

#1 현재 폴더 얻기
# cwd= os.getcwd()
# print('현재 폴더:',cwd)

# #2 폴더 존재 확인 
# #C:\Users\TOI300\test
# #r'C:\Users\TOI300\test'
# #C:/Users/TOI300/test
# s= os.path.isdir(r'C:\Users\TOI300\test')
# print('폴더존재 여부:',s)

# # #3 파일 존재 여부
# # s = os.path.isfile('Monica.txt')
# # print('파일존재 여부:',s)

# # #4 폴더 이동
# # #os.chdir(r'C:\Users\TOI300\test')
# # print(os.getcwd())

# # #5 폴더 생성
# # if os.path.isdir('test2'):
# #     print('폴더가 이미 있으므로 만들 수 없습니다')
# # else:
# #     os.mkdir('test2')
# #     print('test2 폴더 생성완료')
# # # 확인
# # print('test2 생성여부:',os.path.isdir('test2'))

# #6. 폴더 이름 변경: rename
# #test2=> test3
# #먼지 2가 있는지 확인 =>true
# #     3가 있는지 확이 =>false


# # os.chdir(r'C:\Users\TOI300')
# # if os.path.isdir('test2'):
# #     if not os.path.isdir('test3'):
# #         os.rename('test2','test3')
# #         print('test2를 3로 변경완료')
# #     else:
# #         print('test3가 이미 존재하므로 2를 3으로 변경불과')
# # else:
# #     print('test2폴더 존재X')

# #연습

# # os.chdir(r'C:\Users\TOI300\test3')
# # if os.path.isdir('test3'):
# #     if not os.path.isdir('test4'):
# #         os.rename('test3','test4')
# #         print('test3을 4로 변경완료')
# #     else:
# #         print('test4가 이미 존재하므로 3를 4로 변경불과')
# # else:
# #     print('test3폴더 존재X')
# # print(os.getcwd())

# #연습
# #1
# print(os.getcwd())
# os.chdir(r'C:\\')
# print(os.getcwd())

# if os.path.isdir('working'):
#     print('폴더가 이미 있으므로 만들 수 없습니다')
# else:
#     os.mkdir('working')
#     print('생성여부:',os.path.isdir('working'))

# #2 test폴더 만들기

# os.chdir(r'C:\working')
# print(os.getcwd())

# if os.path.isdir('test'):
#     print('폴더가 이미 있으므로 만들 수 없습니다')
# else:
#     os.mkdir('test')
#     print('test 폴더 생성여부:',os.path.isdir('test'))

# #3 파일 이름변경
# if os.path.isdir('test'):
#     if not os.path.isdir('test2'):
#         os.rename('test','test2')
#         print('test를 test2로 변경완료')
#     else:
#         print('test2가 이미 존재하므로 변경불과')
# else:
#     print('test폴더 존재X')

#4 파일 삭제

os.rmdir(r'C:\working\test2')
print('존재여부:',os.path.isdir(r'C:\working\test2'))

# os.rmdir(r'C:\working')
# print('존재여부:',os.path.isdir(r'C:\working'))

# os.rmdir(r'C:\working')
# print('존재여부:',os.path.isdir(r'C:\working'))