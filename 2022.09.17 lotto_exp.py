#로또 번호 가져오기 부분만 연습
# https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=2
import requests
from bs4 import BeautifulSoup

#pip install requests
#pip install beautifulsoup4

#당첨번호,보너스 번호 리턴 
def get_lottonum(num_str):
    
    ret_data=''
    url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='
    res = requests.get(url+num_str)
    soup = BeautifulSoup(res.text,'html.parser')

    data=soup.find('div',attrs={'class':'nums'})

    s=data.text
    lst = s.splitlines()

    # print('당첨번호:',lst[4],lst[5],lst[6],lst[7],lst[8],lst[9])
    # print('보너스번호:',lst[14])
    ret_data='당첨번호:'+' '.join(lst[4:10]) +'\n보너스 번호:'+lst[14]

    return ret_data

print(get_lottonum(1))

url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='

#서버로 보내는 방법 request
res = requests.get(url+'1')

#받는 방법 response
#print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
#print(str(soup)) #html 해석할때 검색 함수들을 사용할 수 있음

#soup 해석해서 원하는 정보 뜯어오기
data=soup.find('div',attrs={'class':'nums'})
#print(type(data.text)) class<<str>
#문자열 처리 => 줄 기준
#당첨번호:, 보너스 번호 추출
#UI에 연결

# s=data.text
# lst = s.splitlines()
# for d in lst:
#     print(d)

# print('당첨번호:',lst[4],lst[5],lst[6],lst[7],lst[8],lst[9])
# print('보너스번호:',lst[14])