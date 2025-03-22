# Trading CNN con MetaTrader 5

Sistema de trading algorítmico utilizando Redes Neuronales Convolucionales (CNN) para scalping.

## Requisitos
- Windows (MetaTrader 5 solo funciona en Windows)
- Python 3.8+
- MetaTrader 5 instalado
- Cuenta de MetaTrader 5 (demo o real)

## Instalación
1. Instalar MetaTrader 5 desde su [sitio oficial](https://www.metatrader5.com/es/download)

2. Clonar el repositorio:
```bash
git clone https://github.com/apenara/trading-cnn-bot.git
cd trading-cnn-bot
```

3. Instalar dependencias:
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
2. Configurar credenciales de MetaTrader 5:
```
MT5_LOGIN=tu_login
MT5_PASSWORD=tu_password
MT5_SERVER=tu_servidor
```

## Uso
1. Asegúrate de que MetaTrader 5 esté instalado y configurado
2. Ejecuta el sistema:
```bash
python src/main.py
```

## Características
- Modelo CNN para predicción de movimientos de precio
- Integración directa con MetaTrader 5
- Estrategia de scalping automatizada
- Análisis técnico y procesamiento de datos en tiempo real

## Notas Importantes
- Este sistema está diseñado para funcionar exclusivamente en Windows debido a las limitaciones de MetaTrader 5
- Se recomienda probar primero con una cuenta demo
- Asegúrate de tener MetaTrader 5 instalado y configurado antes de ejecutar el sistema

## Contribuir
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos.