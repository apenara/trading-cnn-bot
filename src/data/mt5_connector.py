import os
import MetaTrader5 as mt5
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class MT5Connector:
    def __init__(self):
        load_dotenv()
        self.login = int(os.getenv('MT5_LOGIN'))
        self.password = os.getenv('MT5_PASSWORD')
        self.server = os.getenv('MT5_SERVER')
        self.connected = False
        
    def connect(self):
        """Establece conexión con MetaTrader 5"""
        if not mt5.initialize():
            print("Error inicializando MT5")
            return False
            
        authorized = mt5.login(self.login, password=self.password, server=self.server)
        if not authorized:
            print("Error en la autorización")
            mt5.shutdown()
            return False
            
        self.connected = True
        print("Conexión exitosa con MetaTrader 5")
        return True
        
    def get_data(self, symbol, timeframe, n_bars=1000):
        """Obtiene datos históricos del símbolo especificado"""
        if not self.connected:
            print("No hay conexión con MT5")
            return None
            
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n_bars)
        if rates is None:
            print(f"Error obteniendo datos para {symbol}")
            return None
            
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        return df
        
    def prepare_data_for_cnn(self, df, window_size=60):
        """Prepara los datos para la CNN"""
        features = ['open', 'high', 'low', 'close', 'tick_volume']
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
        
    def close(self):
        """Cierra la conexión con MetaTrader 5"""
        if self.connected:
            mt5.shutdown()
            self.connected = False