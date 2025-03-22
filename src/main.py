from data.mt5_connector import MT5Connector
from models.cnn_model import TradingCNN
import MetaTrader5 as mt5
from sklearn.model_selection import train_test_split
import numpy as np
import os
from datetime import datetime

def main():
    # Configurar el símbolo y timeframe para scalping
    SYMBOL = "EURUSD"
    TIMEFRAME = mt5.TIMEFRAME_M1  # Timeframe de 1 minuto para scalping
    WINDOW_SIZE = 60  # Ventana de 60 minutos
    
    # Inicializar conexión con MT5
    connector = MT5Connector()
    if not connector.connect():
        return
        
    try:
        # Obtener datos históricos
        print(f"Obteniendo datos históricos para {SYMBOL}...")
        df = connector.get_data(SYMBOL, TIMEFRAME, n_bars=10000)
        
        if df is None:
            print("Error obteniendo datos")
            return
            
        # Preparar datos para la CNN
        print("Preparando datos para el entrenamiento...")
        X, y = connector.prepare_data_for_cnn(df, window_size=WINDOW_SIZE)
        
        # Dividir datos en entrenamiento, validación y prueba
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
        
        # Crear y entrenar el modelo
        print("Iniciando entrenamiento del modelo...")
        input_shape = (WINDOW_SIZE, X.shape[2])
        model = TradingCNN(input_shape)
        
        history = model.train(X_train, y_train, X_val, y_val, epochs=50)
        
        # Evaluar el modelo
        print("\nEvaluando el modelo...")
        loss, accuracy = model.evaluate(X_test, y_test)
        print(f"Precisión en datos de prueba: {accuracy*100:.2f}%")
        
        # Guardar el modelo
        model_path = os.path.join('models', f'cnn_model_{datetime.now().strftime("%Y%m%d_%H%M")}.h5')
        os.makedirs('models', exist_ok=True)
        model.save(model_path)
        print(f"\nModelo guardado en: {model_path}")
        
    finally:
        # Cerrar conexión
        connector.close()

if __name__ == "__main__":
    main()