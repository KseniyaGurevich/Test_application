from urlextract import URLExtract
import requests
from pprint import pprint


def extract_urls(N, data):
    """Проверяет, является ли строка ссылкой"""
    extractor = URLExtract()
    url_list = []
    shot_url_list = []
    for i in range(N):
        url = extractor.find_urls(data[i])
        if not url:
            print(f'Строка {i + 1} не является ссылкой.')
        elif len(url[0]) > 8 and (url[0][:8] == 'https://' or url[0][:7] == 'http://'):
            shot_url = url[0].split('//')[1]
            if shot_url not in shot_url_list:
                url_list.append(url[0])
                shot_url_list.append(shot_url)
        else:
            print(f'Строка {i + 1} не является ссылкой.')
    return url_list


def check_allow_methods(url):
    """Проверяет, указаны ли в  заголовке разрешённые методы"""
    try:
        options = requests.options(url)
        allow_methods = options.headers['Allow'].split(', ')
        return allow_methods
    except KeyError:
        return None


def write_id_dict(url_list):
    """Определяет методы для каждой ссылки и записывает результат в словарь"""
    result = {}
    for url in url_list:
        all_methods = {
            'GET': requests.get(url).status_code,
            'POST': requests.post(url).status_code,
            'HEAD': requests.head(url).status_code,
            'OPTIONS': requests.options(url).status_code,
            'PUT': requests.put(url).status_code,
            'PATCH': requests.patch(url).status_code,
            'DELETE': requests.delete(url).status_code,
        }
        allow_methods = check_allow_methods(url)
        if allow_methods is None:
            for method in all_methods:
                if all_methods[method] != 405:
                    if not result:
                        result[url] = {method: all_methods[method]}
                    elif url in result:
                        result[url][method] = all_methods[method]
                    else:
                        result[url] = {method: all_methods[method]}
        else:
            for method in allow_methods:
                if not result:
                    result[url] = {method: all_methods[method]}
                elif url in result:
                    result[url][method] = all_methods[method]
                else:
                    result[url] = {method: all_methods[method]}
    return result


def read_input():
    """Ввод данных"""
    N = int(input())
    data = [input() for _ in range(N)]
    return N, data


if __name__ == "__main__":
    N, data = read_input()
    url_list = extract_urls(N, data)
    result = write_id_dict(url_list)
    pprint(result)

