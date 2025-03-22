import os
import ccxt
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class ExchangeConnector:
    def __init__(self):
        load_dotenv()
        self.exchange_id = os.getenv('EXCHANGE_ID', 'binance')
        self.api_key = os.getenv('API_KEY')
        self.api_secret = os.getenv('API_SECRET')
        self.exchange = None
        self.connected = False
        
    def connect(self):
        """Establece conexión con el exchange"""
        try:
            exchange_class = getattr(ccxt, self.exchange_id)
            self.exchange = exchange_class({
                'apiKey': self.api_key,
                'secret': self.api_secret,
                'enableRateLimit': True
            })
            self.connected = True
            print(f'Conexión exitosa con {self.exchange_id}')
            return True
        except Exception as e:
            print(f'Error conectando con el exchange: {e}')
            return False
            
    def get_data(self, symbol, timeframe='1m', limit=1000):
        """Obtiene datos históricos del símbolo especificado"""
        if not self.connected:
            print('No hay conexión con el exchange')
            return None
            
        try:
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            return df
        except Exception as e:
            print(f'Error obteniendo datos: {e}')
            return None
            
    def prepare_data_for_cnn(self, df, window_size=60):
        """Prepara los datos para la CNN"""
        features = ['open', 'high', 'low', 'close', 'volume']
        data = df[features].values
        
        # Normalización
        data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
        
        # Crear ventanas de datos
        X = []
        y = []
        
        for i in range(len(data) - window_size):
            window = data[i:(i + window_size)]
            target = 1 if data[i + window_size, 3] > data[i + window_size - 1, 3] else 0
            X.append(window)
            y.append(target)
            
        return np.array(X), np.array(y)