import os
import sys
import requests
token = "YOUR_ACCESS_TOKEN" # 네이버 로그인 접근 토큰
header = "Bearer " + token # Bearer 다음에 공백 추가
url = "https://openapi.naver.com/blog/writePost.json"

title = "네이버 블로그 api Test Python"
contents = "<font color='red'>python multi-part</font>로 첨부한 글입니다. <br> python 이미지 2개 첨부 <br> <img src='#0' /> <img src='#1' />";
data = {'title': title, 'contents': contents}
files = [
    ('image', ('captcha.jpg', open('captcha.jpg', 'rb'), 'image/jpeg', {'Expires': '0'})),
    ('image', ('ptest.jpg', open('ptest.jpg', 'rb'), 'image/jpeg', {'Expires': '0'}))
    ]

headers = {'Authorization': header }
response = requests.post(url, headers=headers, files=files, data=data)

rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print("Error Code:" + rescode)
