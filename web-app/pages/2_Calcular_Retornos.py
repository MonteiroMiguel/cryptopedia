import streamlit as st
from datetime import date, timedelta
from src.app.domain.calcular_retornos import show_coin_return
from src.app.domain.general_requests import get_coins_list

base_url = "https://api.coingecko.com/api/v3/"
KEY = st.secrets["CG_KEY"]



if 'coins_list' not in st.session_state:
    get_coins_list(base_url, KEY)

today = date.today()
one_year_ago = today - timedelta(365)
coin = st.sidebar.selectbox('Selecione uma criptomoeda', st.session_state.coins_list, index=st.session_state.coins_list.index('bitcoin') if st.session_state.coins_list else None)
start = st.sidebar.date_input("De: ", min_value=one_year_ago, max_value=today)
end = st.sidebar.date_input("Até: ", min_value=one_year_ago, max_value=today)
search = st.sidebar.button('Obter retorno', on_click=show_coin_return, args=[base_url, KEY, coin, start, end])

st.title("Calcular Retornos")

if 'returns' in st.session_state:
    st.header(f"Retorno de {coin.capitalize()}:")
    st.write(f"{st.session_state.returns:.2%}")
else:
    st.write("Selecione uma criptomoeda e um período para calcular o retorno através da barra lateral!")