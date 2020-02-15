import re
from lxml import etree  # need install
import json
import ADC_function


def getTitle(htmlcode):  # 获取厂商
    # print(htmlcode)
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[2]/div/div[1]/h3/text()')).strip(" ['']")
    result2 = str(re.sub('\D{2}2-\d+', '', result)).replace(' ', '', 1)
    # print(result2)
    return result2


def getActor(htmlcode):
    try:
        html = etree.fromstring(htmlcode, etree.HTMLParser())
        result = str(html.xpath('/html/body/div[2]/div/div[1]/h5[5]/a/text()')).strip(" ['']")
        return result
    except:
        return ''


def getActorPhoto(actor):  # //*[@id="star_qdt"]/li/a/img
    actor = actor.split('/')
    d = {}
    for i in actor:
        p = {i: ''}
        d.update(p)
    return d


def getStudio(htmlcode):  # 获取厂商
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[2]/div/div[1]/h5[3]/a[1]/text()')).strip(" ['']")
    return result


def getNum(htmlcode):  # 获取番号
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[5]/div[1]/div[2]/p[1]/span[2]/text()')).strip(" ['']")
    # print(result)
    return result


def getRelease(htmlcode2):  #
    # a=ADC_function.get_html('http://adult.contents.fc2.com/article_search.php?id='+str(number).lstrip("FC2-").lstrip("fc2-").lstrip("fc2_").lstrip("fc2-")+'&utm_source=aff_php&utm_medium=source_code&utm_campaign=from_aff_php')
    html = etree.fromstring(htmlcode2, etree.HTMLParser())
    result = str(html.xpath('//*[@id="container"]/div[1]/div/article/section[1]/div/div[2]/dl/dd[4]/text()')).strip(
        " ['']")
    return result


def getCover(htmlcode, number, htmlcode2):  # 获取厂商 #
    # a = ADC_function.get_html('http://adult.contents.fc2.com/article_search.php?id=' + str(number).lstrip("FC2-").lstrip("fc2-").lstrip("fc2_").lstrip("fc2-") + '&utm_source=aff_php&utm_medium=source_code&utm_campaign=from_aff_php')
    html = etree.fromstring(htmlcode2, etree.HTMLParser())
    result = str(html.xpath('//*[@id="container"]/div[1]/div/article/section[1]/div/div[1]/a/img/@src')).strip(" ['']")
    if result == '':
        html = etree.fromstring(htmlcode, etree.HTMLParser())
        result2 = str(html.xpath('//*[@id="slider"]/ul[1]/li[1]/img/@src')).strip(" ['']")
        return 'https://fc2club.com' + result2
    return 'http:' + result


def getOutline(htmlcode2):  # 获取番号 #
    html = etree.fromstring(htmlcode2, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/article/section[4]/p/text()')).strip(
        " ['']").replace("\\n", '', 10000).replace("'", '', 10000).replace(', ,', '').strip('  ').replace('。,', ',')
    return result


def getTag(htmlcode):  # 获取番号
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[2]/div/div[1]/h5[4]/a/text()'))
    return result.strip(" ['']").replace("'", '').replace(' ', '')


def getYear(release):
    try:
        result = re.search('\d{4}', release).group()
        return result
    except:
        return ''


def main(number):
    htmlcode2 = ADC_function.get_html(
        'http://adult.contents.fc2.com/article_search.php?id=' + number + '&utm_source=aff_php&utm_medium=source_code&utm_campaign=from_aff_php')
    htmlcode = ADC_function.get_html('https://fc2club.com//html/FC2-' + number + '.html')
    actor = getActor(htmlcode)
    if len(actor) == 0:
        actor = 'FC2系列'
    try:
        dic = {
            'title': getTitle(htmlcode).replace(' ', '-'),
            'studio': getStudio(htmlcode),
            'publisher': '',
            'year': '',  # str(re.search('\d{4}',getRelease(number)).group()),
            'outline': getOutline(htmlcode2).replace('\n', ''),
            'runtime': getYear(getRelease(htmlcode)),
            'director': '',
            'actor': actor.replace('/', ','),
            'release': getRelease(number),
            'number': 'FC2-' + number,
            'cover': getCover(htmlcode, number, htmlcode2),
            'imagecut': 0,
            'series': '',
            'tag': getTag(htmlcode),
            'actor_photo': getActorPhoto(actor),
            'website': 'https://fc2club.com//html/FC2-' + number + '.html',
            'source': 'fc2fans_club.py',
        }
    except:
        if htmlcode2 == 'ProxyError':
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

# print(main('1251689'))
