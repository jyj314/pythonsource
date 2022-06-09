import urllib.request as req

# 저장하고 싶은 이미지

img_url = "https://previews.123rf.com/images/reinekke/reinekke1603/reinekke160300016/55091878-%EC%9D%B4-oldschool-%EB%AC%B8%EC%8B%A0%EC%9D%98-%EC%A7%91%ED%95%A9%EC%9E%85%EB%8B%88%EB%8B%A4-%EA%BD%83-%ED%98%B8%EC%8A%A4-%EC%8A%88-%ED%96%89%EC%9A%B4%EC%9D%98-%EC%83%81%EC%A7%95.jpg"

# 다운로드 받을 경로
path = "./rpabasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path + "lucky.jpg")
except Exception as e:
    print(e)
else:
    print(header1)
