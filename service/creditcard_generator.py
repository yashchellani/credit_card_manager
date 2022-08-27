import requests

def generate_creditcard():
    resp = requests.get("https://v00j17tbch.execute-api.ap-southeast-1.amazonaws.com/default/credit_card_generator")
    data = resp.json()
    return data