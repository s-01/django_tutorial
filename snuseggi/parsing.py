import urllib.request
from bs4 import BeautifulSoup

# input : 식당이름
# 아래의 snuYes, snuNo의 문자열값을 따라야함.

def menulist(input):

    snuYes = ['학생회관식당학생회관(63동)', '3식당전망대(75-1동)', '기숙사식당관악사(919동)', '자하연식당농협(109동)',
              '302동식당302동', '솔밭간이식당110동', '동원관식당113동', '감골식당101동']

    snuNo = ['4식당서당골 (76동)', '두레미담75-1동', '301동식당301동', '예술계식당(74동)75동', '샤반501동',
         '공대간이식당30-2동', '상아회관연건켐퍼스 19동', '소담마루동원생활관 113동 3층', '220동식당3단계대학원연구동(220동)',
         '라운지오동원생활관(113동) 1층']

    if input in snuYes:
        menuURL = 'http://www.snuco.com/html/restaurant/restaurant_menu1.asp'
        restaurantNum = snuYes.index(input)
    elif input in snuNo:
        menuURL = 'http://www.snuco.com/html/restaurant/restaurant_menu2.asp'
        restaurantNum = snuNo.index(input)
    else:
        return 'ERROR'

    # 디버깅용으로 날짜변경시
    #menuURL = menuURL + '?date=2016-06-14'

    html = urllib.request.urlopen(menuURL)
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find('table', attrs={'width':'586px'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    cols = rows[restaurantNum+1].find_all('td')
    data = [ele.text.strip() for ele in cols if ele]

    #식당이름제거
    del data[0]

    # '/'가 포함된 시간대는 편의상 제일 앞 메뉴만 표시
    data = [iter.split('/')[0][1:] for iter in data]
    # 1아침 3점심 5저녁
    data = [data[1], data[3], data[5]]

    return data