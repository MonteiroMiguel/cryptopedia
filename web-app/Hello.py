import streamlit as st
from src.app.domain.general_requests import get_coins_list, get_currencies_list
base_url = "https://api.coingecko.com/api/v3/"
TOKEN = st.secrets["CG_KEY"]

st.set_page_config(
    page_title='Olá!'
)

if 'coins_list' not in st.session_state:
    get_coins_list(base_url, TOKEN)

if 'currencies_list' not in st.session_state:
    get_currencies_list(base_url, TOKEN)

st.markdown("""
# Olá!

Oi! Essa é uma aplicação voltada a criptomoedas desenvolvida como projeto final do curso **Transfero x Senac Academy**. Você pode acessar as funcionalidades através da barra lateral. Abaixo estão algumas informações relevantes de cada funcionalidade.


# Funcionalidades

Nosso projeto conta com as seguintes funcionalidades: **Cotações**, **Calculo de Retornos**, **Preços Históricos** e **Notícias**

## **Cotações**

Essa funcionalidade permite que você tenha acesso ao valor de mais de **14 mil criptomoedas** com cerca de **60 conversões disponíveis**. Tudo isso graças a API da **CoinGecko**, caso tenha ficado interessado, é possível acessar a documentação da API [clicando aqui.](https://docs.coingecko.com/v3.0.1/reference/introduction)

## Cálculo de Retornos

Com essa funcionalidade, é possível calcular o retorno acumulado que a criptomoeda escolhida lhe daria em um determinado período.

## Preços Históricos

Caso tenha interesse em fazer análises um pouco mais elaboradas, nossa aplicação também disponibiliza preços históricos de criptomoedas em um período de até **1 ano**,

## Notícias

Para aqueles que gostam de acompanhar as novidades e acontecimentos relevantes do mundo cripto, criamos uma guia com notícias sobre o tema.
""")
