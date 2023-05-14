# parser_.py
from bs4 import BeautifulSoup
import time

# < lxml >
# lxml parser 는 c 언어로 구현되어 있기 때문에 가장 빠르다.
# XML 도 처리 가능하지만, c 언어로 구현되어 있기 때문에 c 언어에 의존적이다.

# 1
html = """<p>test</p>"""

soup = BeautifulSoup(html, 'lxml')
print('lxml #1 : ', soup)

# 2
html = """<html><p>test</p></html>"""
soup = BeautifulSoup(html, 'lxml')
print('lxml #2-1 : ', soup)

html = """<body><p>test</p></body>"""
soup = BeautifulSoup(html, 'lxml')
print('lxml #2-2 : ', soup)

'''
# < html5lib >
# html5lib parser 는 web browser 형태로 HTML 을 분석하고 관리한다.
# python 으로 구현되어 있기 때문에 lxml 처럼 c 언어에 의존적이지 않지만, c 언어로 구현된 lxml 보다 느리다.

# 1
html = """<p>test</p>"""

soup = BeautifulSoup(html, 'html5lib')
print('html5lib #1 : ', soup)

# 2
html = """<html><body><p>test</p></body></html>"""
soup = BeautifulSoup(html, 'html5lib')
print('html5lib #2-1 : ', soup)

html = """<html><head></head><p>test</p></html>"""
soup = BeautifulSoup(html, 'html5lib')
print('html5lib #2-2 : ', soup)

html = """<head></head><p>test</p>"""
soup = BeautifulSoup(html, 'html5lib')
print('html5lib #2-3 : ', soup)
'''

# < lxml VS html5lib >
# speed gap

# 1
# import time
html = """<html><head></head><p>test</p></html>"""

start_time = time.time()
BeautifulSoup(html, 'lxml')
lxml_end_time = time.time() - start_time

start_time = time.time()
BeautifulSoup(html, 'html5lib')
html5lib_end_time = time.time() - start_time

print('lxml VS html5lib #1-1 : ', 'lxml 시간 측정 : %f' % lxml_end_time)
print('lxml VS html5lib #1-2 : ', 'html5lib 시간 측정 : %f' % html5lib_end_time)
print('lxml VS html5lib #1-3 : ', html5lib_end_time/lxml_end_time)

# 2
html = """<html><head></head><p>test</p></html>"""

time_sum = 0
loop_count = 5
j = 1

for i in range(0, loop_count):

    start_time = time.time()
    BeautifulSoup(html, 'lxml')
    lxml_end_time = time.time() - start_time

    start_time = time.time()
    BeautifulSoup(html, 'html5lib')
    html5lib_end_time = time.time() - start_time

    rate = html5lib_end_time / lxml_end_time

    print('lxml VS html5lib #2-%d : ' % j, "%d 번째 시도" % i)
    print('lxml VS html5lib #2-%d : ' % (j+1), 'lxml 시간측정 : %f' % lxml_end_time)
    print('lxml VS html5lib #2-%d : ' % (j+2), 'html5lib 시간측정 : %f' % html5lib_end_time)
    print('lxml VS html5lib #2-%d : ' % (j+3), '**', rate, '**\n')
    time_sum += rate
    j += 4

average = time_sum / loop_count
print('lxml VS html5lib #1-%d : ' % j, 'average time : %f' % average)

# Parser 를 잘못 넣으면 에러가 발생합니다.
# 없는 Parser 를 넣거나, 오타 등의 이유로 잘못 타이핑했다면, 해당 파서를 찾을 수 없다고 에러 메시지를 띄워줍니다.