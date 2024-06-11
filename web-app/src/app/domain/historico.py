from src.app.domain.general_requests import make_request


def get_coin_historical_price(base_url,key,coin_id):
    url = f"{base_url}coins/{coin_id}/market_chart?vs_currency=brl&precision=5&days=365&interval=daily&x_cg_demo_api_key={key}"
    return make_request(url)