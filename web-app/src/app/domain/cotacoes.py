import streamlit as st
import requests
from src.app.domain.general_requests import make_request

def get_coin_price(base_url,key,id,currencies):
    currencies_url = ''
    for currency in currencies:
        currencies_url += f"{currency}," 
    url = f'{base_url}simple/price?ids={id}&vs_currencies={currencies_url}&precision=2&x_cg_demo_api_key={key}'
    response = make_request(url)
    st.session_state.coin_prices = response[id]

