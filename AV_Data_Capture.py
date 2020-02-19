#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from core import *


def movie_lists(escape_folder):
    if escape_folder != '':
        escape_folder = re.split('[,，]', escape_folder)
    total = []
    file_type = ['.mp4', '.avi', '.rmvb', '.wmv', '.mov', '.mkv', '.flv', '.ts', '.MP4', '.AVI', '.RMVB', '.WMV',
                 '.MOV', '.MKV', '.FLV', '.TS', ]
    file_root = os.getcwd()
    for root, dirs, files in os.walk(file_root):
        if escape_folder != '':
            flag_escape = 0
            for folder in escape_folder:
                if folder in root:
                    flag_escape = 1
                    break
            if flag_escape == 1:
                continue
        for f in files:
            if os.path.splitext(f)[1] in file_type:
                path = root + '/' + f
                path = path.replace(file_root, '.')
                path = path.replace("\\\\", "/").replace("\\", "/")
                total.append(path)
    return total

num_cache = {}
def getNumber(filepath):
    if filepath in num_cache.keys():
        return num_cache[filepath]
    filename = filepath.replace('-C.', '.').replace('-c.', '.')
    filename = os.path.splitext(filename.split('/')[-1])[0]
    part = ''
    if re.search('-CD\d+', filename):
        part = re.findall('-CD\d+', filename)[0]
    if re.search('-cd\d+', filename):
        part = re.findall('-cd\d+', filename)[0]
    
    filename = filename.replace(part, '')
    filename = filename.lower()
    filename = filename.replace('22-sht.me','')
    filename = filename.replace('-10mu','')
    filename = filename.replace('-1pon','')
    filename = filename.replace('-paco','')
    filename = filename.replace('-hd','')
    filename = filename.replace('_hd','')
    filename = filename.replace('-720p','')
    filename = filename.replace('_720p','')
    filename = filename.replace('-1080p','')
    filename = filename.replace('_1080p','')
    filename = str(re.sub("-\d{4}-\d{1,2}-\d{1,2}", "", filename))  # 去除文件名中时间
    filename = str(re.sub("\d{4}-\d{1,2}-\d{1,2}-", "", filename))  # 去除文件名中时间
    if '-' in filename or '_' in filename:  # 普通提取番号 主要处理包含减号-和_的番号
        if 'FC2' or 'fc2' in filename:
            filename = filename.replace('-PPV', '').replace('PPV-', '').replace('-ppv', '').replace('ppv-', '')
        if re.search('[a-zA-Z]+-\d+', filename):  # 提取类似mkbd-120番号
            file_number = re.search('[a-zA-Z]+-\d+', filename).group()
        elif re.search('[a-zA-Z]+-[a-zA-Z]\d+', filename):  # 提取类似mkbd-s120番号
            file_number = re.search('[a-zA-Z]+-[a-zA-Z]\d+', filename).group()
        elif re.search('\d+-\d+', filename):  # 提取类似 111111-000 番号
            file_number = re.search('\d+-\d+', filename).group()
        elif re.search('\d+_\d+', filename):  # 提取类似 111111_000 番号
            file_number = re.search('\d+_\d+', filename).group()
        elif re.search('\d+-[a-zA-Z]+', filename):  # 提取类似 111111-MMMM 番号
            file_number = re.search('\d+-[a-zA-Z]+', filename).group()
        elif 'heyzo' in filename and re.search('\d{4}', filename):  # 提取heyzo番号:
            file_number = 'heyzo-'+ re.search('\d{4}', filename).group()
        else:
            file_number = filename
        num_cache[filepath] = file_number
        return file_number
    else:  # 提取不含减号-的番号，FANZA CID 保留ssni00644，将MIDE139改成MIDE-139
        try:
            file_number = os.path.splitext(filename.split('/')[-1])[0]
            find_num = re.findall(r'\d+', file_number)[0]
            find_char = re.findall(r'\D+', file_number)[0]
            if len(find_num) <= 4 and len(find_char) > 1:
                file_number = find_char + '-' + find_num
            num_cache[filepath] = file_number
            return file_number
        except:
            file_number = os.path.splitext(filepath.split('/')[-1])[0]
            num_cache[filepath] = file_number
            return file_number