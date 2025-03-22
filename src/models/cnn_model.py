import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam
import numpy as np

class TradingCNN:
    def __init__(self, input_shape):
        self.model = self._build_model(input_shape)
        
    def _build_model(self, input_shape):
        """Construye el modelo CNN"""
        model = Sequential([
            # Primera capa convolucional
            Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=input_shape),
            MaxPooling1D(pool_size=2),
            Dropout(0.2),
            
            # Segunda capa convolucional
            Conv1D(filters=128, kernel_size=3, activation='relu'),
            MaxPooling1D(pool_size=2),
            Dropout(0.2),
            
            # Tercera capa convolucional
            Conv1D(filters=256, kernel_size=3, activation='relu'),
            MaxPooling1D(pool_size=2),
            Dropout(0.2),
            
            # Aplanar los datos
            Flatten(),
            
            # Capas densas
            Dense(128, activation='relu'),
            Dropout(0.3),
            Dense(64, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        return model
        
    def train(self, X_train, y_train, X_val, y_val, epochs=50, batch_size=32):
        """Entrena el modelo"""
        history = self.model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            epochs=epochs,
            batch_size=batch_size,
            verbose=1
        )
        return history
        
    def predict(self, X):
        """Realiza predicciones"""
        return self.model.predict(X)
        
    def evaluate(self, X_test, y_test):
        """Evalúa el modelo"""
        return self.model.evaluate(X_test, y_test)
        
    def save(self, filepath):
        """Guarda el modelo"""
        self.model.save(filepath)
        
    @classmethod
    def load(cls, filepath):
        """Carga un modelo guardado"""
        model = tf.keras.models.load_model(filepath)
        instance = cls((None, None))
        instance.model = model
        return instance