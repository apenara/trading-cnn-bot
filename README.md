# Trading CNN con CCXT

Sistema de trading algorítmico utilizando Redes Neuronales Convolucionales (CNN) para scalping.

## Requisitos
- Python 3.8+
- Cuenta en un exchange compatible con CCXT

## Instalación
1. Clonar el repositorio
```bash
git clone https://github.com/apenara/trading-cnn-bot.git
cd trading-cnn-bot
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto
- `src/`: Código fuente
  - `data/`: Módulos para obtención y procesamiento de datos
  - `models/`: Modelos CNN y utilidades
  - `utils/`: Funciones auxiliares
- `config/`: Archivos de configuración
- `notebooks/`: Jupyter notebooks para análisis y desarrollo

## Configuración
1. Crear archivo `.env` en la raíz del proyecto
2. Configurar credenciales del exchange:
```
EXCHANGE_ID=binance
API_KEY=tu_api_key
API_SECRET=tu_api_secret
```

## Uso
```bash
python src/main.py
```

## Características
- Modelo CNN para predicción de movimientos de precio
- Integración con múltiples exchanges a través de CCXT
- Estrategia de scalping automatizada
- Análisis técnico y procesamiento de datos en tiempo real

## Contribuir
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos.