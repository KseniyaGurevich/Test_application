import application

N = 4
data = ['kasjbfksajfb', 'https://google.com', 'https://vk.com', 'jsfkhfkajhfkajs']

res = application.cli_application(N, data)
print(type(res))