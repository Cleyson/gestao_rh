from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='8f68687695434aa585fde49ffd92944f')

all_articles = newsapi.get_everything(
        q='bitcoin',
        sources='globo,info-money',
        domains='globo.com. informoney.com.br',
        from_param='2023-04-01',
        to='2023-04-21',
        language='pt',
        sort_by='publishedAt',
)
print(all_articles)