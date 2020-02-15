#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from configparser import ConfigParser
from lxml import etree


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, errors = 'replace', line_buffering = True)
# sys.setdefaultencoding('utf-8')

def save_config(json_config):
    # json_config = json.loads(json_config)
    with open("config.ini", "wt", encoding='UTF-8') as code:
        print("[common]", file=code)
        print("main_mode = " + str(json_config['main_mode']), file=code)
        print("failed_output_folder = " + json_config['failed_output_folder'], file=code)
        print("success_output_folder = " + json_config['success_output_folder'], file=code)
        print("soft_link = " + str(json_config['soft_link']), file=code)
        print("website = " + json_config['website'], file=code)
        print("#all or javdb", file=code)
        print("", file=code)
        print("[proxy]", file=code)
        print("proxy = " + json_config['proxy'], file=code)
        print("timeout = " + str(json_config['timeout']), file=code)
        print("retry = " + str(json_config['retry']), file=code)
        print("", file=code)
        print("[Name_Rule]", file=code)
        print("folder_name = " + json_config['folder_name'], file=code)
        print("naming_media = " + json_config['naming_media'], file=code)
        print("naming_file = " + json_config['naming_file'], file=code)
        print("", file=code)
        print("[update]", file=code)
        print("update_check = " + str(json_config['update_check']), file=code)
        print("", file=code)
        print("[media]", file=code)
        print("media_warehouse = " + json_config['media_warehouse'], file=code)
        print("#emby or plex or kodi ,emby = jellyfin", file=code)
        print("", file=code)
        print("[escape]", file=code)
        print("literals = " + json_config['literals'], file=code)
        print("folders = " + json_config['folders'], file=code)
        print("", file=code)
        print("[debug_mode]", file=code)
        print("switch = " + str(json_config['switch_debug']), file=code)
        print("", file=code)
        print("[emby]", file=code)
        print("emby_url = " + json_config['emby_url'], file=code)
        print("api_key = " + json_config['api_key'], file=code)
    code.close()


def getDataState(json_data):  # 元数据获取失败检测
    if json_data['title'] == '' or json_data['title'] == 'None' or json_data['title'] == 'null':
        return 0
    else:
        return 1


def ReadMediaWarehouse(config):
    return config['media']['media_warehouse']


def UpdateCheckSwitch(check):
    if check == 1:
        return '1'
    else:
        return '0'


def getXpathSingle(htmlcode, xpath):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result1 = str(html.xpath(xpath)).strip(" ['']")
    return result1


def get_html(url, cookies=None):  # 网页请求核心
    config_file = 'config.ini'
    config = ConfigParser()
    config.read(config_file, encoding='UTF-8')
    retry_count = 0
    proxy = {}
    timeout = 0
    try:
        proxy = config['proxy']['proxy']
        timeout = int(config['proxy']['timeout'])
        retry_count = int(config['proxy']['retry'])
    except:
        print('[-]Proxy config error! Please check the config.')
    i = 0
    while i < retry_count:
        try:
            if not str(config['proxy']['proxy']) == '':
                proxies = {"http": "http://" + proxy, "https": "https://" + proxy}
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/60.0.3100.0 Safari/537.36'}
                getweb = requests.get(str(url), headers=headers, timeout=timeout, proxies=proxies, cookies=cookies)
                getweb.encoding = 'utf-8'
                return getweb.text
            else:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/68.0.3440.106 Safari/537.36'}
                getweb = requests.get(str(url), headers=headers, timeout=timeout, cookies=cookies)
                getweb.encoding = 'utf-8'
                return getweb.text
        except:
            i += 1
            print('[-]Connect retry ' + str(i) + '/' + str(retry_count))
    print('[-]Connect Failed! Please check your Proxy or Network!')
    return 'ProxyError'
