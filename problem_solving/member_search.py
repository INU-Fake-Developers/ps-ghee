import requests
from bs4 import BeautifulSoup

# 찾고 싶은 아이디를 리스트로 입력
bojIDs = ['sjy9484', 'jhjeon_99', 'potados99']

for bojID in bojIDs:
    # http 요청 시간이 오래 걸려 3~4초 정도의 딜레이가 발생할 수 있음.
    res = requests.get('https://solved.ac/profile/' + bojID)
    soup = BeautifulSoup(res.content, 'html.parser')
    ratingTag = soup.find('span', 'ProfileRatingCard__AcRatingDisplay-sc-989yd6-0 jaNtBE')
    rating = ratingTag.contents[0].contents[0]
    print(bojID + ' : ' + str(rating))
