# Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида:
# (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным
# файла логов из предыдущего задания.

dict_spam = {}

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for content in f:
        remote_addr = content.split(' ')[0]
        if remote_addr in dict_spam:
            dict_spam[remote_addr] += 1
        else:
            dict_spam[remote_addr] = 1
        request_type_temp = content.split('"')[1]
        request_type = request_type_temp.split(' ')[0]
        requested_resource = request_type_temp.split(' ')[1]
        final_tuple = (remote_addr, request_type, requested_resource)
        print(final_tuple)
print(dict_spam)
max_val = max(dict_spam.values())
print(max_val)
print('СПАМЕР ЗЛОСТНЫЙ -', {ip_addr: number_of_requests for ip_addr, number_of_requests in dict_spam.items()
                            if number_of_requests == max_val})
