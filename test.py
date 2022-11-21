import application


class TestExtract:
    def test_extract_link(self):
        N = 3
        data = ['kasjbfksajfb', 'https://google.com', 'google.com']
        url_list = application.extract_urls(N, data)
        assert len(url_list) == 1, 'В списке должна быть только одна ссылка'

    def test_no_one_link(self):
        N = 2
        data = ['kasjbfksajfb', 'ljsdfhskjhfakjgke']
        result = application.extract_urls(N, data)
        assert result == [], 'Список должен быть пуст'

    def test_similar_link(self):
        N = 2
        data = ['https://google.com', 'https://google.com']
        result = application.extract_urls(N, data)
        assert len(result) == 1, 'Список не должен содержать повторных ссылок'

    def test_http_https(self):
        N = 2
        data = ['http://google.com', 'https://google.com']
        url_list = application.extract_urls(N, data)
        assert len(url_list) == 1, 'Список не должен содержать повторных ссылок'


class TestAllowMethods():
    def test_no_allow_methods(self):
        url = 'https://vk.com'
        assert application.check_allow_methods(url) is None, 'В заголовке нет разрешенных методов'

    def test_yes_allow_methods(self):
        url = 'https://google.com'
        assert application.check_allow_methods(url) == ['GET', 'HEAD'], ('В заголовке должны быть разрешенные методы'
                                                                         'GET и HEAD')


class TestWriteInDict:
    def test_type_result(self):
        url_list = ['https://vk.com', 'https://google.com']
        result = application.write_id_dict(url_list)
        assert type(result) == dict, 'Результат не в виде словаря'

    def test_no_one_link(self):
        url_list = ['https://vk.com', 'https://google.com']
        result = application.write_id_dict(url_list)
        assert len(result) == 2, 'Словарь должен содержать 2 ссылки'




