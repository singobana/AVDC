import re
from pyquery import PyQuery as pq  # need install
from lxml import etree  # need install
from bs4 import BeautifulSoup  # need install
import json
from ADC_function import *


def getActorPhoto(htmlcode):  # //*[@id="star_qdt"]/li/a/img
    soup = BeautifulSoup(htmlcode, 'lxml')
    a = soup.find_all(attrs={'class': 'star-name'})
    d = {}
    for i in a:
        l = i.a['href']
        t = i.get_text()
        html = etree.fromstring(get_html(l), etree.HTMLParser())
        p = str(html.xpath('//*[@id="waterfall"]/div[1]/div/div[1]/img/@src')).strip(" ['']")
        p2 = {t: p}
        d.update(p2)
    return d


def getTitle(htmlcode):  # 获取标题
    doc = pq(htmlcode)
    title=str(doc('div.container h3').text()).replace(' ','-')
    try:
        title2 = re.sub('n\d+-', '', title)
        return title2
    except:
        return title


def getStudio(htmlcode):  # 获取厂商
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"製作商")]/following-sibling::a/text()')).strip(" ['']")
    return result


def getPublisher(htmlcode):  # 获取发行商
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"發行商")]/following-sibling::a/text()')).strip(" ['']")
    return result


def getYear(getRelease):  # 获取年份
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getCover(htmlcode):  # 获取封面链接
    doc = pq(htmlcode)
    image = doc('a.bigImage')
    return image.attr('href')


def getRelease(htmlcode):  # 获取出版日期
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"發行日期")]/../text()')).strip(" ['']")
    return result


def getRuntime(htmlcode):  # 获取分钟
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"長度")]/../text()')).strip(" ['']")
    return result


def getActor(htmlcode):  # 获取女优
    b = []
    soup = BeautifulSoup(htmlcode, 'lxml')
    a = soup.find_all(attrs={'class': 'star-name'})
    for i in a:
        b.append(i.get_text())
    return b


def getNum(htmlcode):  # 获取番号
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"識別碼")]/following-sibling::span/text()')).strip(" ['']")
    return result


def getDirector(htmlcode):  # 获取导演
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"導演")]/following-sibling::a/text()')).strip(" ['']")
    return result


def getOutline(htmlcode):  # 获取简介
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath("//div[@class='mg-b20 lh4']/text()")).strip(" ['']")
    return result


def getSeries(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"系列")]/following-sibling::a/text()')).strip(" ['']")
    return result


def getCover_small(number):  # 从avsox获取封面图
    htmlcode = get_html('https://avsox.host/cn/search/' + number)
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//*[@id="waterfall"]/div/a/@href')).strip(" ['']")
    if result1 == '' or result1 == 'null' or result1 == 'None':
        htmlcode = get_html('https://avsox.host/cn/search/' + number.replace('-', '_'))
        html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
        result1 = str(html.xpath('//*[@id="waterfall"]/div/a/@href')).strip(" ['']")
        if result1 == '' or result1 == 'null' or result1 == 'None':
            htmlcode = get_html('https://avsox.host/cn/search/' + number.replace('_', ''))
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = html.xpath('//*[@id="waterfall"]/div/a/div[1]/img/@src')
    if len(result) > 1:
        result = result[0]
    else:
        result = str(result).strip(" ['']")
    return result


def getTag(htmlcode):  # 获取标签
    tag = []
    soup = BeautifulSoup(htmlcode, 'lxml')
    a = soup.find_all(attrs={'class': 'genre'})
    for i in a:
        if 'onmouseout' in str(i):
            continue
        tag.append(i.get_text())
    return tag


def find_number(number):
    # =======================================================================有码搜索
    counts = 0
    if not (re.match('^\d{4,}', number) or re.match('n\d{4}', number) or 'HEYZO' in number.upper()):
        htmlcode = get_html('https://www.javbus.com/search/' + number + '&type=1')
        html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
        counts = len(html.xpath("//div[@id='waterfall']/div[@id='waterfall']/div"))
        if counts != 0:
            for count in range(1, counts + 1):  # 遍历搜索结果，找到需要的番号
                number_get = html.xpath("//div[@id='waterfall']/div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/div[@class='photo-info']/span/date[1]/text()")[0]
                # number_get = number_get.replace('_', '-')
                if number_get == number.upper() or number_get == number.upper().replace('-', '') or number_get == number.upper().replace('_', ''):
                    result_url = html.xpath(
                        "//div[@id='waterfall']/div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/@href")[0]
                    return result_url
                elif number_get == number.lower() or number_get == number.lower().replace('-', '') or number_get == number.lower().replace('_', ''):
                    result_url = html.xpath(
                        "//div[@id='waterfall']/div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/@href")[0]
                    return result_url
    # =======================================================================无码搜索
    htmlcode = get_html('https://www.javbus.com/uncensored/search/' + number + '&type=1')
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    counts = len(html.xpath("//div[@id='waterfall']/div[@id='waterfall']/div"))
    if counts == 0:
        return 'not found'
    for count in range(1, counts + 1):  # 遍历搜索结果，找到需要的番号
        number_get = html.xpath("//div[@id='waterfall']/div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/div[@class='photo-info']/span/date[1]/text()")[0]
        # number_get = number_get.replace('_', '-')
        if number_get == number.upper() or number_get == number.upper().replace('-', '') or number_get == number.upper().replace('_', ''):
            result_url = html.xpath(
                "//div[@id='waterfall']/div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/@href")[0]
            return result_url
        elif number_get == number.lower() or number_get == number.lower().replace('-', '') or number_get == number.lower().replace('_', ''):
            result_url = html.xpath(
                "//div[@id='waterfall']/div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/@href")[0]
            return result_url
        elif number_get == number.replace('-', '_') or number_get == number.replace('_', '-'):
            result_url = html.xpath(
                "//div[@id='waterfall']/div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/@href")[0]
            return result_url
    return 'not found'


def main(number):
    result_url = find_number(number)
    if result_url == 'not found':
        dic = {
            'title': '',
            'actor': '',
            'website': '',
        }
        js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4,
                        separators=(',', ':'), )  # .encode('UTF-8')
        return js
    htmlcode = get_html(result_url)
    try:
        dww_htmlcode = get_html("https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=" + number.replace("-", '00'))
    except:
        dww_htmlcode = ''
    try:
        number = getNum(htmlcode)
        dic = {
            'title': str(getTitle(htmlcode)).replace(number, '').strip().replace(' ', '-'),
            'studio': getStudio(htmlcode),
            'publisher': getPublisher(htmlcode),
            'year': getYear(getRelease(htmlcode)),
            'outline': getOutline(dww_htmlcode).replace('\n', '').replace('\\n', '').replace('\'', '').replace(',', '').replace(' ', ''),
            'runtime': getRuntime(htmlcode).replace('分鐘', '').strip(),
            'director': getDirector(htmlcode),
            'actor': getActor(htmlcode),
            'release': getRelease(htmlcode),
            'number': number,
            'cover': getCover(htmlcode),
            'imagecut': 1,
            'tag': getTag(htmlcode),
            'series': getSeries(htmlcode),
            'actor_photo': getActorPhoto(htmlcode),
            'website': result_url,
            'source': 'javbus.py',
        }
    except Exception as error_info:
        print('Error in javbus.main :' + str(error_info))
        if htmlcode == 'ProxyError':
            dic = {
                'title': '',
                'website': 'timeout',
            }
        else:
            dic = {
                'title': '',
                'website': '',
            }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


def main_uncensored(number):
    result_url = find_number(number)
    if result_url == 'not found':
        dic = {
            'title': '',
            'actor': '',
            'website': '',
        }
        js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4,
                        separators=(',', ':'), )  # .encode('UTF-8')
        return js
    htmlcode = get_html(result_url)
    try:
        number = getNum(htmlcode)
        dic = {
            'title': getTitle(htmlcode).replace(number, '').strip().replace(' ', '-'),
            'studio': getStudio(htmlcode),
            'publisher': '',
            'year': getYear(getRelease(htmlcode)),
            'outline': '',
            'runtime': getRuntime(htmlcode).replace('分鐘', '').strip(),
            'director': getDirector(htmlcode),
            'actor': getActor(htmlcode),
            'release': getRelease(htmlcode),
            'number': getNum(htmlcode),
            'cover': getCover(htmlcode),
            'tag': getTag(htmlcode),
            'series': getSeries(htmlcode),
            'imagecut': 3,
            'cover_small': getCover_small(number),
            'actor_photo': getActorPhoto(htmlcode),
            'website': result_url,
            'source': 'javbus.py',
        }
        if dic['cover_small'] == '':
            dic['imagecut'] = 0
    except Exception as error_info:
        print('Error in javbus.main_uncensored :' + str(error_info))
        if htmlcode == 'ProxyError':
            dic = {
                'title': '',
                'website': 'timeout',
            }
        else:
            dic = {
                'title': '',
                'website': '',
            }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js

# print(find_number('KA-001'))
# print(main('OFJE-175'))
# print(main_uncensored('122919-949'))
# print(main_uncensored('012715-793'))
