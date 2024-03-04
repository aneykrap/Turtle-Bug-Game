# 네이버 뉴스 가져오기 


import requests
from bs4 import BeautifulSoup

#pip install requests
#pip install beautifulsoup4

# kind_num : 신문사 고유번호
# 30 : 전자신문 
def get_news(kind_num):
    
    ret_data=''
    url = 'https://media.naver.com/press/'
    res = requests.get(url+kind_num)
    soup = BeautifulSoup(res.text,'html.parser')

    data=soup.find_all('span',attrs={'class':'press_news_text'})

    for d in data:
        #print(d.strong.text)
        ret_data +=d.strong.text +'\n'
    return ret_data


print(get_news('030'))

#url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo='

#서버로 보내는 방법 request

#받는 방법 response
#print(res.text)
#soup = BeautifulSoup(res.text,'html.parser')
#print(str(soup)) #html 해석할때 검색 함수들을 사용할 수 있음

#soup 해석해서 원하는 정보 뜯어오기
#data=soup.find('div',attrs={'class':'nums'})
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