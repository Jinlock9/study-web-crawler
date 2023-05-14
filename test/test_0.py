# test_0.py
# TEST Number 0 [Module : Requests]
import requests as rq
import json


# number 0.0 <requests module>
# no. 0.0.0 : importing requests module
# no. 0.0.1 : import requests as rq
# import requests as rq


# number 0.1 <connecting to web pages>
# no. 0.1.0 : GET request
url = "http://pjt3591oo.github.io"

res_get = rq.get(url)
print("no. 0.1.0.0:  ", res_get)

# no. 0.1.1 : POST request
'''
res_post = rq.post(url)
print("no. 0.1.1.0:  ", res_post)
'''


# number 0.2 <response code>
# no. 0.2.0 : status_code
print("no. 0.2.0.0:  ", res_get.status_code)
'''
status code 200 : the server successfully handles the client's request.
Web pages return 200 codes when the page's request completes normally.
'''

# no. 0.2.1 : checking the code of non-existing pages
url = "http://pjt3591oo.github.io/a"

res_get = rq.get(url)

print("no. 0.2.1.0:  ", res_get)
print("no. 0.2.1.1:  ", res_get.status_code)  # status code 404: PAGE NOT FOUND, connecting to non-existing url

# no. 0.2.2 : conditioning using response codes


def url_check(def_url):
    def_res = rq.get(def_url)

    print("no. 0.2.2.0:  ", def_res)

    sc = def_res.status_code

    if sc == 200:
        print("no. 0.2.2.1:  ", "%s Request Success" % def_url)
    elif sc == 404:
        print("no. 0.2.2.2:  ", "%s PAGE NOT FOUND" % def_url)
    else:
        print("no. 0.2.2.3:  ", "%s Unknown Error : %s" % (def_url, sc))


url_check("http://pjt3591oo.github.io")
url_check("http://pjt3591oo.github.io/a")


# number 0.3 <headers>
# no. 0.3.0 : retrieving headers
url = "http://blog.naver.com/pjt3591oo"

res_get = rq.get(url)

print("no. 0.3.0.0:  ", res_get)
print("no. 0.3.0.1:  ", res_get.headers)

# no. 0.3.1 : retrieving specific data (ex. Set-Cookie)
headers = res_get.headers
print("no. 0.3.1.0:  ", headers['Set-Cookie'])

# no. 0.3.2 : accessing to all factors of headers
i = 0
for header in headers:
    print("no. 0.3.2.%d:  " % i, headers[header])
    i += 1


# number 0.4 <cookies>
# no. 0.4.0 : retrieving cookies 1
url = "http://blog.naver.com/pjt3591oo"

res_get = rq.get(url)
print("no. 0.4.0.0:  ", res_get)

cookies = res_get.cookies
print("no. 0.4.0.1:  ", cookies)

# no. 0.4.1 : retrieving cookies 2
print("no. 0.4.1.0:  ", list(cookies))
print("no. 0.4.1.1:  ", tuple(cookies))
print("no. 0.4.1.2:  ", dict(cookies))


# number 0.5 <HTML codes>
# no. 0.5.0 : retrieving HTML codes 1
url = "https://pjt3591oo.github.io/"

res_get = rq.get(url)
print("no. 0.5.0.0:  ", res_get.text)

# no. 0.5.1 : retrieving HTML codes 2
print("no. 0.5.1.0:  ", res_get.content)

# no. 0.5.2 :checking encoding method
print("no. 0.5.2.0:  ", res_get.encoding)


# number 0.6 <query string>
# no. 0.6.0 : creating query strings 1
url = "https://pjt3591oo.github.io/"

res_get = rq.get(url, params={"key1": "value1", "key2": "value2"})
print("no. 0.6.0.0:  ", res_get.url)

# no. 0.6.1 : creating query strings 2
url_a = "https://pjt3591oo.github.io//?key2=value2&key1=value1"

res_a = rq.get(url_a)
print("no. 0.6.1.0:  ", res_a.url)


# number 0.7 <POST request>
# no. 0.7.0 : post request
url = "http://www.example.com"

res_post = rq.post(url, data={"key1": "value1", "key2": "value2"})
print("no. 0.7.0.0:  ", res_post.url)

# no. 0.7.1 : post request using json module
# import json

res_post = rq.post(url, data=json.dumps({"key1": "value1", "key2": "value2"}))
# transform form of data to character sting from dictionary
print("no. 0.7.1.0:  ", res_post.url)

# no. 0.7.2 : difference between json module and str
dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = {"key1": "value1", "key2": "value2"}

print("no. 0.7.2.0:  ", json.dumps(dict1))
print("no. 0.7.2.1:  ", str(dict1))

print("no. 0.7.2.2:  ", json.dumps(dict2))
print("no. 0.7.2.3:  ", str(dict2))


# number 0.8 <setting up headers>
# no. 0.8.0 : setting up headers
url = "https://pjt3591oo.github.io/"

res_b = rq.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"})

print("no. 0.8.0.0:  ", res_b.url)

