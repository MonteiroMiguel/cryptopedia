import streamlit as st
from src.app.domain.general_requests import get_coins_list, get_currencies_list
from src.app.domain.cotacoes import get_coin_price

base_url = "https://api.coingecko.com/api/v3/"
TOKEN = st.secrets["CG_KEY"]

if 'coins_list' not in st.session_state:
    get_coins_list(base_url, TOKEN)

if 'currencies_list' not in st.session_state:
    get_currencies_list(base_url, TOKEN)

st.sidebar.empty()
coin = st.sidebar.selectbox('Selecione uma cripto', st.session_state.coins_list, index=st.session_state.coins_list.index('bitcoin'))
currencies = st.sidebar.multiselect('Converter para:', options=st.session_state.currencies_list, default='brl')
search = st.sidebar.button("Obter valor", on_click=get_coin_price, args=(base_url, TOKEN,coin, currencies))

st.title("Cotações Cripto")


if 'coin_prices' in st.session_state:
    st.header(f'Preço de {coin}')
    for currency, price in st.session_state.coin_prices.items():
        st.text(f"{currency.upper()} {price}")
else:
    st.write('Selecione uma criptomoeda e as conversões que deseja realizar através das opções na barra lateral!')
