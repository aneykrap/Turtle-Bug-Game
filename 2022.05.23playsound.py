# 2022.05.23 playsound 테스트

from playsound import playsound
import time
import os

'''
print('시작음 before',time.time())
playsound('start.wav',True)
print('시작음 after',time.time())

print('coin before',time.time())
playsound('coin.wav',True)
print('coin after',time.time())


print('bgm2 before',time.time())
playsound('bgm2.wav',True)
print('bgm2 after',time.time())
'''
print(os.path.exists('start.wav'))
print(os.path.exists('bgm2.wav'))
'''
bgm = False

while True:
    if not bgm:
        bgm_star_tm = time.time()
        playsound('bgm2.wav',False)
        bgm = True
    else:
        gap_time = time.time() - bgm_star_tm 
        if gap_time > 8.5 :
            bgm = False
    print(bgm,time.time())
'''