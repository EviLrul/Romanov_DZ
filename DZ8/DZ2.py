# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера
# из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>,
# <requested_resource>, <response_code>, <response_size>),
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1"
# 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2',
# '304', '0')

import re

itog_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f1:
    f2 = open('out.txt', 'w', encoding='utf-8')
    line_f1 = f1.readline()
    line_f1 = line_f1.replace('\n', '').replace('\r', ' ')
    while line_f1:
        reg = re.compile(r'^[\w:.]+')
        temp_list = reg.findall(line_f1)
        itog_list.append(temp_list[0])
        reg = re.compile(r'\d{2}[/:\w]+ \+\d{4}')
        temp_list = reg.findall(line_f1)
        itog_list.append(temp_list[0])
        reg = re.compile(r'GET|HEAD|POST')
        temp_list = reg.findall(line_f1)
        itog_list.append(temp_list[0])
        reg = re.compile(r'/\w+/\w+_\d')
        temp_list = reg.findall(line_f1)
        itog_list.append(temp_list[0])
        reg = re.compile(r'" [1-5]\d{2}')
        temp_list = reg.findall(line_f1)
        itog_list.append(temp_list[0][2:])
        reg = re.compile(r'\d+ "')
        temp_list = reg.findall(line_f1)
        itog_list.append(temp_list[0][0: len(temp_list) - 3])
        print(itog_list)
        f2.write(str(itog_list) + '\n')
        itog_list.clear()
        line_f1 = f1.readline()
f2.close()
