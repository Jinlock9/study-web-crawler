# test_3.py
# TEST Number 3 [Module : Parsing Module]
import bs4
from bs4 import BeautifulSoup


# number 3.0 <definition>
# no. 3.0.0 : parsing
'''
Parsing: Parsing 은 구문 분석이라고 한다.
문장이 이루고 있는 구성 성분을 분해하고 분해된 성분의 위계 관계를 분석하여 구조를 결정하는 것이다.
즉 데이터를 분해 분석하여 원하는 형태로 조립하고 다시 빼내는 프로그램을 말한다.
웹상에서 주어진 정보를 내가 원하는 형태로 가공하여 서버에서 불러들이는 것이다.
이러한 parsing 기법은 XML parsing 과 JSON parsing 이 있다.

출처: https://kingpodo.tistory.com/8 [킹포도의 코딩]
'''

# no. 3.0.1 : parser
'''
Parser: Parser 란 Compiler 의 일부로서 원시 프로그램의 명령문이나 온라인 명령문, HTML 문서 등에서 Markup Tag 등을 
입력으로 받아들여서 구분을 해석 할 수 있는 단위로 여러 부분으로 해석하는 역할을 한다. 
즉 Compiler 나 Interpreter 에서 원시 프로그램을 읽어 들여, 그 문장이 구조를 알아내는 Parsing 을 행하여 주는 프로그램이다.

출처: https://kingpodo.tistory.com/8 [킹포도의 코딩]
'''


# number 3.1 <bs4 module>
# no. 3.1.0 : importing bs4 module
# import bs4

# no. 3.1.1 : using bs4 module
# html = """"""
# soup = bs4.BeautifulSoup(html)  # BeautifulSoup() : 문자열을 파이썬에서 사용 가능한 객체로 만들어줌.
# BeautifulSoup() 함수에 두 번째 인자로 파서를 넣지 않아서 line 34번 실행 시 경고문이 나옴. 에러는 아님.
# 해당 시스템에서 가장 적합한 Parser 를 선택했다는 경고문. 대체로 'lxml'

# no. 3.1.2 : selecting parser
html = """"""
soup1 = bs4.BeautifulSoup(html, 'lxml')  # BeautifulSoup(String, 'Parser')
# bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml.
# Do you need to install a parser library?
# 라고 오류가 났었는데, cmd 로 pip install lxml 하여 lxml 을 설치를 해도 계속 오류가 났다.
# C:\Users\choij\Appdata\local\programs\python\python38\lib\site-packages 여기서 'lxml'과 'lxml-4.5.0.dist-info'를
# 복사하여 이 프로젝트 폴더 내에 붙여넣으니 오류가 해결되었다.

# no. 3.1.3 : easy usage of bs4
# from bs4 import BeautifulSoup
html = """"""
soup2 = BeautifulSoup(html, 'lxml')

# no. 3.1.4 : Parsers
'''
Parser 란, 원시 코드인 순수 문자열 객체를 해석할 수 있도록 분석하는 것을 의미.
Python 에서 사용되는 Parser 는 아래와 같다.
- lxml :  XML 해석이 가능한 Parser. 그리고 Python 2.x와 3.x 모두 지원 가능. 다른 Parser 에 비해 매우 빠른 속도로 처리 가능.
- html5lib : Web Brower 방식으로 HTML을 해석. 하지만 처리 속도가 매우 느림. 2.x 버전 전용.
- html.parser : 최신 버전에서 사용 불가.
'''