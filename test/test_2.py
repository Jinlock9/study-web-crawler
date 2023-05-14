# test_2.py
# TEST Number 2 [Module : Urllib]


# number 2.0 <urllib module>
# no. 2.0.0 : importing urllib module
from urllib.request import urlopen, Request
import urllib

# no. 2.0.1 : using urllib module
url = "https://pjt3591oo.github.io/"

req = Request(url)  # to create Requesting Object
page = urlopen(req)  # to request by using Requesting Module

print("no. 2.0.1.0:  ", page)

# no. 2.0.2 : checking various information
print("no. 2.0.2.0:  ", page)
print("no. 2.0.2.1:  ", page.code)
print("no. 2.0.2.2:  ", page.headers)
print("no. 2.0.2.3:  ", page.url)
print("no. 2.0.2.4:  ", page.info().get_content_charset())

# no. 2.0.3 : getting HTML code
url = "https://pjt3591oo.github.io/"

req = Request(url)
page = urlopen(req)
print("no. 2.0.3.0:  ", page)
print("no. 2.0.3.1:  ", page.read())  # getting HTML code in binary form

# no. 2.0.4 : requesting data
url = "http://blog.naver.com/pjt3591oo"

# post 요청 시 보낼 데이터 생성
data = {'key1': 'value1', 'key2': 'value2'}  # data 를 만들 때는 encode 함수를 바이너리 형태로 인코딩해서 보내야 한다.
data = urllib.parse.urlencode(data)  # key1=value1&key2=value2  # 딕셔너리를 쿼리스트링 형태로 바꿔준다.
data = data.encode('utf-8')  # b'key1=value1&key2=value2' # 쿼리스트링처럼 표현된 문자열을 UTF-8 로 인코딩하여 바이너리 형태로 바꿔준다.

print("no. 2.0.4.0:  ", data)

# post request
req_post = Request(url, data=data, headers={})  # 2번째 인자 데이터, 세 번째 인자 헤더
page = urlopen(req_post)

print("no. 2.0.4.1:  ", page)
print("no. 2.0.4.2:  ", page.url)

# get request
req_get = Request(url+"?key1=value1&key2=value2", None, headers={}) # 2번째 인자 데이터, 세 번째 인자 헤더
page = urlopen(req_get)

print("no. 2.0.4.3:  ", page)
print("no. 2.0.4.4:  ", page.url)
'''
urllib 는 Request() 함수를 이용하여 요청 객체를 만들 때 두 번째 인자에는 데이터, 세 번째 인자에는 헤더가 들어간다.
만약 두 번째 인자 값이 존재한다면 POST 요청, 존재하지 않는다면 GET 요청을 보낸다.
즉, 두 번째 인자 값의 존재 여부에 따라 GET 요청인지 POST 요청인지 결정된다.
(GET 요청일 때 두 번째 인자에 None 을 넣거나 넣지 않으면 된다.)
'''

# no. 2.0.5 : requesting non-existing page
url = "https://pjt3591oo.github.io/1"

req_post = Request(url)
page = urlopen(req_post)

print("no. 2.0.5.0:  ", page)
print("no. 2.0.5.1:  ", page.url)  # urllib.error.HTTPError: HTTP Error 404: Not Found


# number 2.1 <requests VS urllib>
# no. 2.1.0 : requests VS urllib
'''
1. requests 와 urllib 는 요청 시 요청 개체를 만드는 방법에 차이가 있다.
2. 데이터를 보낼 때 requests 는 딕셔너리 형태로 urllib 는 인코딩하여 바이너리 형태로 전송한다.
3. requests 는 요청 메소드(GET, POST)를 명시하지만 urllib 는 데이터의 여부에 따라 GET 요청과 POST 요청을 구분한다.
4. 없는 페이지 요청 시 requests 는 error 를 띄우지 않지만 urllib 는 에러를 띄웁니다.
'''

