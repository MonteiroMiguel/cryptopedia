import streamlit as st
from newsapi import NewsApiClient

API_KEY = st.secrets['NEWS_API_KEY']

newsapi = NewsApiClient(api_key=API_KEY)
keywords_list = ['bitcoin', 'blockchain', 'memecoin', 'ethereum','solana']

st.title('Notícias sobre Crypto')
for elements in keywords_list:
    elements_news = newsapi.get_everything(q=elements, language='pt', sort_by='publishedAt')
    if elements_news['totalResults'] > 0:
        articles = elements_news['articles']
        for article in articles:
            if article['title'] != '[Removed]':
                st.write('**Título:**', article['title'])
                st.write('**Fonte:**', article['source']['name'])
                st.write('**Publicado em:**', article['publishedAt'])
                st.write('**Descrição:**', article['description'])
                st.write('**Link:**', article['url'])
                st.write('---')
    else:
        st.write('Nenhuma notícia encontrada.')