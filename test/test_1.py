# test_1.py
# TEST Number 1 [Exception Handling]
import requests as rq
import time


# number 1.0 <requests error handling>
# no. 1.0.0 : types of requests error
'''
HTTPError : HTTP error occur
ConnectionError : connection error occur
ProxyError : proxy error occur
SSLError : SSL certificate error occur (https)
Timeout : server does not answer for a certain period of time
ConnectTimeout : server does not answer for a certain period of time
ReadTimeout : server does not send data for a certain period of time
URLRequired : error occur when require valid url
TooManyRedirects : error occur when there are too many redirects (refreshifing)
MissingSchema : error occur when omit http or https
InvalidSchema : valid schema refers defaults.py
InvalidURL : error occur when header is wrong
ChunkedEncodingError : error occur when encode in wrong way
ContentDecodingError : error occur when fail to decode reponses
StreamConsumedError : error occur when response contents are already consumed
RetryError : error occur when user defined re-request is failed
UnrewindableBodyError : error occur when reading the body again
'''

# no. 1.0.1 : requesting error handling method
url = "http://blog.naver.com/pjt3591oo"

try:
    res_a = rq.get(url)
    print("no. 1.0.1.0:  ", res_a.url)
except rq.exceptions.HTTPError:
    print("no. 1.0.1.1:  ", 'HTTP Error Occur')
except rq.exceptions.Timeout:
    print("no. 1.0.1.2:  ", 'Timeout Error Occur')

# no. 1.0.2 : error occur
url = "blog.naver.com/pjt3591oo"

#res_b = rq.get(url)

# no. 1.0.3 : handling error
try:
    res_b = rq.get(url)
except rq.exceptions.MissingSchema:
    print("no. 1.0.3.0:  ", 'MissingSchema Error Occur')

# 코드단에서 처리 가능한 부분은 이와 같은 방법으로 따로 에러 처리하지 않는 것이 좋음
# timeout 과 같이 서버에 의한 에러들을 except 처리하는 것이 좋음

# no. 1.0.4 : time error
url = "http://blog.naver.com/pjt3591oo"
delay_time = 1


def connection(u):
    return rq.get(u)


try:
    connection(url)
except rq.exceptions.Timeout:
    time.sleep(delay_time)
    connection(url)
'''
서버의 특수한 상황 때문에 timeout error 가 발생할 수 있다. 
timeout 은 서버가 일정 시간 동안 요청한 클라이언트에 응답하지 않았을 때 발생하는 에러이다.
이럴 때 일정 시간 동안 잠시 기다렸다가 재요청하는 방법으로 해결할 수 있다.

이와 같이 특정 코드를 다시 호출할 경우 retry 패턴을 이용하야 효율적으로 관리할 수 있다.
'''

