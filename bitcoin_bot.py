import requests
from datetime import datetime

def preco_bitcoin():
    url = "https://api.coinbase.com/v2/prices/BTC-BRL/spot"
    resposta = requests.get(url)
    dados = resposta.json()
    preco = float(dados["data"]["amount"])
    hora = datetime.now().strftime("%H:%M:%S")
    print(f"[{hora}] Bitcoin: R$ {preco:,.2f}")
    return preco

import time

LIMITE = 300000  # R$300.000

while True:
    preco = preco_bitcoin()
    if preco < LIMITE:
        print(f"[ALERTA] Bitcoin abaixo de R${LIMITE:,}!")
    time.sleep(60)  # verifica a cada 1 minuto