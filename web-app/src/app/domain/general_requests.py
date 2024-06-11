import streamlit as st
import requests

def make_request(url):
    response = requests.get(url)
    return response.json()

def get_coins_list(base_url, key):
    url = f"{base_url}coins/list?x_cg_demo_api_key={key}"
    response = make_request(url)
    st.session_state.coins_list = []
    for coin in response:
        st.session_state.coins_list.append(coin["id"])

def get_currencies_list(base_url, key):
    url = f"{base_url}simple/supported_vs_currencies?x_cg_demo_api_key={key}"
    st.session_state.currencies_list = make_request(url)