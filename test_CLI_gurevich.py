from urlextract import URLExtract
import requests
from pprint import pprint

# def read_input():
#     N = int(input())
#     data = [input() for _ in range(N)]
#     return N, data

result = {}
data = list(iter(input, ''))
N = len(data)

extractor = URLExtract()


for i in range(N):
    url = extractor.find_urls(data[i])
    if not url:
        print(f'Строка {i+1} не является ссылкой.')
    else:
        all_methods = {
            'GET': requests.get(url[0]).status_code,
            'POST': requests.post(url[0]).status_code,
            'HEAD': requests.head(url[0]).status_code,
            'OPTIONS': requests.options(url[0]).status_code,
            'PUT': requests.put(url[0]).status_code,
            'PATCH': requests.patch(url[0]).status_code,
            'DELETE': requests.delete(url[0]).status_code,
        }
        for method in all_methods:
            if all_methods[method] != 405:
                if not result:
                    result[url[0]] = {method: all_methods[method]}
                elif url[0] in result:
                    result[url[0]][method] = all_methods[method]
                else:
                    result[url[0]] = {method: all_methods[method]}


pprint(result)




