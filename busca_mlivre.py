import requests
from bs4 import BeautifulSoup


# Exemplo
# Obter produto do Mercado Livre a partir de uma busca realizada pelo usuário

url_base = 'https://lista.mercadolivre.com.br/'

produto = input('Digite o nome do produto: ')

response = requests.get(url_base + produto)

site = BeautifulSoup(response.text, 'html.parser')

prod_datas = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for prod_data in prod_datas:

    titulo = prod_data.find('h2', attrs={'class': 'ui-search-item__title'})

    link = prod_data.find('a', attrs={'class': 'ui-search-link'})

    real = prod_data.find('span', attrs={'class': 'price-tag-fraction'})

    cents = prod_data.find('span', attrs={'class': 'price-tag-cents'})

    #print(prod_data.prettify())

    print('Titulo do produto', titulo.text)  # Imprime somente o título do produto pesquisado

    print('Link do produto', link['href'])
    if(cents):
        print('Preço do produto: R$', real.text + ',' + cents.text)
    else:
        print('Preço do produto: R$', real.text)

    print('\n')
