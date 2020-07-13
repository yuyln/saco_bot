from twitter import *
from time import sleep
from random import choice
import os

class Bot(Api):
    def __init(self, consumer_key, consumer_secret, access_token_key, access_token_secret, sleep_on_rate_limit=False):
        super().__init__(consumer_key, consumer_secret, access_token_key, access_token_secret, sleep_on_rate_limit)
        print("vai se foder")


access_token = os.environ['ACCESS_TOKEN_SACO']
access_secret = os.environ['ACCESS_SECRET_SACO']
twitter_key = os.environ['TWITTER_KEY_SACO']
twitter_secret = os.environ['TWITTER_SECRET_SACO']
adjetivos = ['pinto', 'ruim', 'gordo', 'doente']
adjetivos_backup = adjetivos.copy()
#api = Bot(consumer_key=twitter_key,
                      #consumer_secret=twitter_secret,
                      #access_token_key=access_token,
                      #access_token_secret=access_secret)
while True:
    if len(adjetivos) != 0:
        adj = choice(adjetivos)
        adjetivos.remove(adj)
    else:
        adjetivos = adjetivos_backup.copy()
        adj = choice(adjetivos)
        adjetivos.remove(adj)
    try:
        if len(adjetivos) != 0:
            print(f"Meu saco {adj}\nFalta(m) {len(adjetivos)} adjetivo(s)")
            #api.PostUpdate(f"Meu saco {adj}\nFaltam {len(adjetivos)} adjetivos")
        else:
            print(f"Meu saco {adj}\nA lista de adjetivos sera resetada")
            #api.PostUpdate(f"Meu saco {adj}\nA lista de adjetivos sera resetada")
    except Exception as e:
        print(e)
    sleep(5)
    
