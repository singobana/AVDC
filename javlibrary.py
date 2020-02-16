import re
from lxml import etree
import json
from ADC_function import *


def getTitle(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath("//h3[@class='post-title text']/a/text()")).strip(" ['']")
    return result


def getActor(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    actor = []
    count_all = len(html.xpath("//td[@class='text']/span[@class='cast']"))
    for count in range(1, count_all + 1):
        actor = actor + (html.xpath("//td[@class='text']/span[" + str(count) + "]/span/a/text()"))
    return actor


def getActorPhoto(actor):  # //*[@id="star_qdt"]/li/a/img
    d = {}
    for i in actor:
        if ',' not in i or ')' in i:
            p = {i: ''}
            d.update(p)
    return d


def getStudio(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result = str(html.xpath("//div[@id='video_maker']/table/tr/td[@class='text']/span[@class='maker']/a/text()")).strip(" ['']")
    return result


def getPublisher(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result = str(html.xpath("//div[@id='video_label']/table/tr/td[@class='text']/span[@class='label']/a/text()")).strip(" ['']")
    return result


def getRuntime(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result = str(html.xpath("//div[@id='video_length']/table/tr/td[2]/span[@class='text']/text()")).strip(" ['']")
    return result


def getNum(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result = str(html.xpath("//div[@id='video_id']/table/tr/td[@class='text']/text()")).strip(" ['']")
    return result


def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getRelease(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result = str(html.xpath("//div[@id='video_date']/table/tr/td[@class='text']/text()")).strip(" ['']")
    return result


def getTag(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    tag = []
    count_all = len(html.xpath("//div[@id='video_genres']/table/tr/td[@class='text']/span[@class='genre']"))
    for count in range(1, count_all + 1):
        tag = tag + (html.xpath("//div[@id='video_genres']/table/tr/td[@class='text']/span[" + str(count) + "]/a/text()"))
    return tag


def getCover(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = 'http:' + str(html.xpath("//img[@id='video_jacket_img']/@src")).strip(" ['']")
    return result


def getDirector(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath("//div[@id='video_director']/table/tr/td[@class='text']/text()")).strip(" ['']")
    return result1


def getOutline(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath("//div[@class='mg-b20 lh4']/text()")).strip(" ['']")
    return result


def getWebsite(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = 'http:' + str(html.xpath('/html/head/meta[@property=\'og:url\']/@content')).strip(" ['']")
    return result


def main(number, javlibrary_url):
    try:
        htmlcode = get_html('http://' + javlibrary_url + '/ja/vl_searchbyid.php?keyword=' + number).replace(u'\xa0', u' ')
        title = getTitle(htmlcode)
        movie_found = 1
        if title == '':  # 页面为搜索结果页，而不是视频信息页，遍历搜索结果
            movie_found = 0
            html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
            count_all = len(html.xpath("//div[@class='videothumblist']/div[@class='videos']/div[@class='video']"))
            for count in range(1, count_all + 1):
                number_get = str(html.xpath("//div[@class='videothumblist']/div[@class='videos']/div[" + str(count) + "]/a/div[1]/text()")).strip(" ['']")
                if number_get == number.upper():
                    url_get = str(html.xpath("//div[@class='videothumblist']/div[@class='videos']/div[" + str(count) + "]/a/@href")).strip(" ['.']")
                    htmlcode = get_html('http://' + javlibrary_url + '/ja' + url_get).replace(u'\xa0', u' ')
                    movie_found = 1
                    break
        if movie_found == 1:
            try:  # 从dmm获取简介
                dww_htmlcode = get_html("https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=" + number.replace("-", '00'))
            except:
                dww_htmlcode = ''
            actor = getActor(htmlcode)
            number = getNum(htmlcode)
            release = getRelease(htmlcode)
            dic = {
                'actor': str(actor).strip(" [',']").replace('\'', ''),
                'title': getTitle(htmlcode).replace('中文字幕', '').replace("\\n", '').replace('_', '-').replace(number,
                                                                                                      '').strip().replace(
                    ' ', '-').replace('--', '-'),
                'studio': getStudio(htmlcode),
                'publisher': getPublisher(htmlcode),
                'outline': getOutline(dww_htmlcode).replace('\n', '').replace('\\n', '').replace('\'', '').replace(',', '').replace(' ', ''),
                'runtime': getRuntime(htmlcode),
                'director': str(getDirector(htmlcode)).replace('----', ''),
                'release': release,
                'number': number,
                'cover': getCover(htmlcode),
                'imagecut': 1,
                'tag': getTag(htmlcode),
                'series': '',
                'year': getYear(release),
                'actor_photo': getActorPhoto(actor),
                'website': getWebsite(htmlcode),
                'source': 'javlibrary.py',
            }
        else:
            dic = {
                'title': '',
                'website': '',
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

# print(main('LUXU-1217'))
# input("[+][+]Press enter key exit, you can check the error messge before you exit.\n[+][+]按回车键结束，你可以在结束之前查看和错误信息。")
# print(main('ssni-674','www.n43a.com'))
# print(main('040409-562'))
# print(main('n1403'))
