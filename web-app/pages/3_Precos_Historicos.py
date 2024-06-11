import streamlit as st
import requests
from datetime import datetime
import pandas as pd

base_url = "https://api.coingecko.com/api/v3/"
key = st.secrets["CG_KEY"]
def make_request(url):
    response = requests.get(url)
    return response.json()

def get_coins_list():
    url = f"{base_url}coins/list?x_cg_demo_api_key={key}"
    response = make_request(url)
    coins_list = []
    for coin in response:
        coins_list.append(coin["id"])
    return coins_list

def get_coin_price_history(coin_id, currency, days):
    url = f"{base_url}coins/{coin_id}/market_chart?vs_currency={currency}&precision=5&days={days}&interval=daily&x_cg_demo_api_key={key}"
    response = requests.get(url)
    response = response.json()
    return response

def show_price_history(coin_id, currency, days):
    price_history = get_coin_price_history(coin_id, currency, days)
    if 'prices' in price_history:
        st.header(f"Preço histórico de {coin_id.capitalize()} em {currency.upper()} nos últimos {days} dias:")
        datas = []
        precos = []
        for data_point in price_history['prices']:
            data_formatada = datetime.fromtimestamp(data_point[0] / 1000).strftime('%m/%d/%Y')
            datas.append(data_formatada)
            precos.append(data_point[1])
            # st.text(f"Data: {data_formatada}, Preço: {data_point[1]} {currency.upper()}")
        df = pd.DataFrame(list(zip(datas, precos)), columns=['Data', 'Valor'])
        df['Data'] = pd.to_datetime(df['Data'])  # Convertendo para datetime
        st.session_state.df = df.sort_values(by='Data')  # Ordenando pelo valor da data
        
        

    

coins_list = get_coins_list()
currencies_list = ['brl', 'usd', 'eur']
days_list = [7, 30, 90, 365]
coin = st.sidebar.selectbox('Selecione uma criptomoeda', coins_list, index=coins_list.index('bitcoin') if coins_list else None)
currency = st.sidebar.selectbox('Selecione os câmbios desejados', currencies_list, index=0 if currencies_list else None)
days = st.sidebar.selectbox('Selecione o período de dias', days_list, index=0 if days_list else None)
chart = st.sidebar.checkbox("Exibir grafico")
search = st.sidebar.button("Obter histórico de preço", on_click=show_price_history, args=[coin, currency, days])

st.title('Preços Históricos')

if 'df' in st.session_state:
    st.dataframe(st.session_state.df, width=500)
    if chart:
        st.line_chart(st.session_state.df.set_index('Data'), color=["#FF0000"]) 
else:
    st.write("Selecione uma criptomoeda e um período para obter o preço histórico através da barra lateral!")