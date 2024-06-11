
import streamlit as st
import pandas as pd
from datetime import datetime
from src.app.domain.historico import get_coin_historical_price

def get_price_dfs(price_history, start, end):
    datas = []
    precos = []
    for data_point in price_history['prices']:
        data_formatada = datetime.fromtimestamp(data_point[0] / 1000).strftime('%m/%d/%Y')
        datas.append(data_formatada)
        precos.append(data_point[1])
    df = pd.DataFrame(list(zip(datas, precos)), columns=['Data', 'Valor'])
    df['Data'] = pd.to_datetime(df['Data'])  # Convertendo para datetime
    df = df.sort_values(by='Data')  # Ordenando pelo valor da data
    start_price_df = df.query(f"Data=='{start}'")["Valor"]
    end_price_df = df.query(f"Data=='{end}'")["Valor"]
    return start_price_df, end_price_df

def calculate_percent_change(start_price_df, end_price_df):
        start_price = start_price_df.iloc[0]
        end_price = end_price_df.iloc[0]
        st.session_state.returns = (end_price - start_price)/ start_price


def show_coin_return(base_url, key, coin_id, start, end):
    price_history = get_coin_historical_price(base_url, key, coin_id)
    if 'prices' in price_history:
        start_price_df, end_price_df = get_price_dfs(price_history, start, end)
        calculate_percent_change(start_price_df, end_price_df)
        