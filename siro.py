import re
from lxml import etree
import json
from bs4 import BeautifulSoup
from ADC_function import *


def getTitle(a):
    try:
        html = etree.fromstring(a, etree.HTMLParser())
        result = str(html.xpath('//*[@id="center_column"]/div[1]/h1/text()')).strip(" ['']")
        return result.replace('/', ',')
    except:
        return ''


def getActor(a):  # //*[@id="center_column"]/div[2]/div[1]/div/table/tbody/tr[1]/td/text()
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"出演：")]/../td/a/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    result2 = str(html.xpath('//th[contains(text(),"出演：")]/../td/text()')).strip(" ['']").strip('\\n    ').strip('\\n')
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '').replace('/', ',')


def getActorPhoto(actor):  # //*[@id="star_qdt"]/li/a/img
    d = {}
    for i in actor:
        if ',' not in i or ')' in i:
            p = {i: ''}
            d.update(p)
    return d


def getStudio(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"メーカー：")]/../td/a/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    result2 = str(html.xpath('//th[contains(text(),"メーカー：")]/../td/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getPublisher(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"レーベル：")]/../td/a/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    result2 = str(html.xpath('//th[contains(text(),"レーベル：")]/../td/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getRuntime(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"収録時間：")]/../td/a/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    result2 = str(html.xpath('//th[contains(text(),"収録時間：")]/../td/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    return str(result1 + result2).strip('+').rstrip('mi')


def getSeries(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"シリーズ：")]/../td/a/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    result2 = str(html.xpath('//th[contains(text(),"シリーズ：")]/../td/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getNum(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"品番：")]/../td/a/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    result2 = str(html.xpath('//th[contains(text(),"品番：")]/../td/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    return str(result1 + result2).strip('+')


def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getRelease(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"配信開始日：")]/../td/a/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    result2 = str(html.xpath('//th[contains(text(),"配信開始日：")]/../td/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    return str(result1 + result2).strip('+')


def getTag(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"ジャンル：")]/../td/a/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    result2 = str(html.xpath('//th[contains(text(),"ジャンル：")]/../td/text()')).strip(" ['']").strip('\\n    ').strip(
        '\\n')
    return str(result1 + result2).strip('+').replace("', '\\n", ",").replace("', '", "").replace('"', '')


def getCover(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//*[@id="center_column"]/div[1]/div[1]/div/div/h2/img/@src')).strip(" ['']")
    #                    /html/body/div[2]/article[2]/div[1]/div[1]/div/div/h2/img/@src
    return result


def getOutline(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//*[@id="introduction"]/dd/p[1]/text()')).strip(" ['']")
    return result


def main(number2):
    number = number2.upper()
    htmlcode = str(
        get_html('https://www.mgstage.com/product/product_detail/' + str(number) + '/', cookies={'adc': '1'}))
    soup = BeautifulSoup(htmlcode, 'lxml')
    a = str(soup.find(attrs={'class': 'detail_data'})).replace('\n                                        ',
                                                               '').replace('                                ',
                                                                           '').replace('\n                            ',
                                                                                       '').replace(
        '\n                        ', '')
    try:
        actor = getActor(a).replace(' ', '')
        dic = {
            'title': getTitle(htmlcode).replace("\\n", '').replace('        ', ''),
            'studio': getStudio(a),
            'publisher': getPublisher(a),
            'outline': getOutline(htmlcode).replace('\n', ''),
            'runtime': getRuntime(a),
            'director': '',
            'actor': actor,
            'release': getRelease(a),
            'number': getNum(a),
            'cover': getCover(htmlcode),
            'imagecut': 0,
            'tag': getTag(a).strip(','),
            'series': getSeries(a).strip(','),
            'year': getYear(getRelease(a)),  # str(re.search('\d{4}',getRelease(a)).group()),
            'actor_photo': getActorPhoto(actor.split(',')),
            'website': 'https://www.mgstage.com/product/product_detail/' + str(number) + '/',
            'source': 'siro.py',
        }
    except:
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

# print(main('300MIUM-382'))
