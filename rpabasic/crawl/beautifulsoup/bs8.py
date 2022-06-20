# requests + beautifulsoup4
# 객체생성(페이지소스, 파서)
import requests
from bs4 import BeautifulSoup

res = requests.get("https://movie.v.daum.net/v/20220612110302954")
# print(res.text)

# parser : html.parser(기본-설치가 필요없음)
# soup = BeautifulSoup(res.text, "html.parser")
soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify()) # 이쁘게(들여쓰기)

# <head> 태그 안 내용 가져오기
# print(soup.head)

# <body> 태그 안 내용 가져오기
# print(soup.body)

# <title> 태그 안 내용 가져오기
# print(soup.title)
# print(soup.title.name)  # 태그명 가져오기
# print(soup.title.get_text())  # 태그 안 텍스트 가져오기
# print(soup.title.string)  # 태그 안 텍스트 가져오기


# 기사제목 가져오기
# soup.h3
news_title = soup.select_one("h3")
print(news_title)
print(news_title.get_text())

# 기사 작성날짜와 시간 가져오기
num_date = soup.select_one("span.num_date")
print(num_date)
print(num_date.get_text())

# 기사 작성자 가져오기
writer = soup.select_one("span.txt_info")
print(writer)
print(writer.get_text())

# 기사 첫번째 문단 가져오기
para1 = soup.select_one("p")
print(para1)
print(para1.get_text())

print()
contents = soup.select("p")
# print(contents)
for para1 in contents:
    print(para1.get_text())
