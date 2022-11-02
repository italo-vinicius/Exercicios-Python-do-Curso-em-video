import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('ERRO AO ABRIR SITE')
else:
    print('SITE ABERTO COM SUCESSO')
    print(site.read())