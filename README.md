# Trading CNN con MetaTrader 5

Sistema de trading algorítmico que utiliza Redes Neuronales Convolucionales (CNN) para scalping en MetaTrader 5. El sistema está diseñado para analizar patrones en los datos de precio y volumen para predecir movimientos futuros del mercado.

## Requisitos del Sistema

### Software Necesario
- Windows (MetaTrader 5 solo funciona en Windows)
- Python 3.8 o superior
- MetaTrader 5 instalado
- Git (opcional, para clonar el repositorio)

### Cuenta de Trading
- Cuenta de MetaTrader 5 (demo o real)
- Credenciales de acceso (login, contraseña, servidor)

## Instalación

### 1. Instalar MetaTrader 5
1. Descargar MetaTrader 5 desde el [sitio oficial](https://www.metatrader5.com/es/download)
2. Ejecutar el instalador y seguir las instrucciones
3. Iniciar MetaTrader 5 y configurar tu cuenta

### 2. Instalar Python
1. Descargar Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, marcar la opción "Add Python to PATH"
3. Verificar la instalación abriendo una terminal y ejecutando:
```bash
python --version
```

### 3. Obtener el Código
Hay dos formas de obtener el código:

#### Opción A: Clonar con Git
```bash
git clone https://github.com/apenara/trading-cnn-bot.git
cd trading-cnn-bot
```

#### Opción B: Descargar ZIP
1. Ir a https://github.com/apenara/trading-cnn-bot
2. Clic en "Code" -> "Download ZIP"
3. Extraer el ZIP y abrir la carpeta

### 4. Instalar Dependencias
Abrir una terminal en la carpeta del proyecto y ejecutar:
```bash
pip install -r requirements.txt
```

### 5. Configuración
1. Crear un archivo `.env` en la raíz del proyecto
2. Agregar las siguientes líneas con tus credenciales:
```
MT5_LOGIN=tu_login
MT5_PASSWORD=tu_password
MT5_SERVER=tu_servidor
```

## Estructura del Proyecto

```
trading-cnn-bot/
│
├── src/
│   ├── data/
│   │   └── mt5_connector.py    # Conexión con MetaTrader 5
│   ├── models/
│   │   └── cnn_model.py        # Implementación del modelo CNN
│   └── main.py                 # Script principal
│
├── models/                     # Modelos entrenados (creado automáticamente)
├── notebooks/                  # Jupyter notebooks para análisis
├── requirements.txt           # Dependencias del proyecto
├── .env                       # Configuración (crear manualmente)
└── README.md                 # Este archivo
```

## Uso del Sistema

### 1. Preparación
- Asegurarse de que MetaTrader 5 esté abierto y con la sesión iniciada
- Verificar que las credenciales en `.env` sean correctas

### 2. Ejecutar el Sistema
```bash
python src/main.py
```

### 3. Funcionamiento
El sistema realizará las siguientes operaciones:
1. Conexión con MetaTrader 5
2. Descarga de datos históricos (EURUSD por defecto)
3. Preparación de datos para el modelo CNN
4. Entrenamiento del modelo
5. Evaluación y guardado del modelo entrenado

## Configuración del Trading

### Parámetros Principales
Los siguientes parámetros se pueden modificar en `src/main.py`:

```python
SYMBOL = "EURUSD"              # Par de divisas
TIMEFRAME = mt5.TIMEFRAME_M1   # Timeframe (1 minuto)
WINDOW_SIZE = 60               # Ventana de análisis (60 minutos)
```

### Estructura del Modelo CNN
El modelo utiliza la siguiente arquitectura:
- 3 capas convolucionales (64, 128, 256 filtros)
- Capas de MaxPooling y Dropout para regularización
- 2 capas densas finales
- Salida binaria (predicción arriba/abajo)

## Recomendaciones

### Para Trading Real
1. Probar primero con una cuenta demo
2. Empezar con cantidades pequeñas
3. Monitorear el rendimiento del modelo
4. Ajustar los parámetros según resultados

### Optimización
- Ajustar `WINDOW_SIZE` según el timeframe
- Modificar la arquitectura CNN en `models/cnn_model.py`
- Experimentar con diferentes pares de divisas
- Agregar indicadores técnicos adicionales

## Solución de Problemas

### Errores Comunes
1. "Error inicializando MT5"
   - Verificar que MetaTrader 5 esté instalado y abierto
   - Comprobar que estés en Windows

2. "Error en la autorización"
   - Verificar credenciales en `.env`
   - Comprobar conexión a internet

3. "Error obteniendo datos"
   - Verificar que el símbolo existe en tu cuenta
   - Comprobar permisos de trading

## Contribuir
Las contribuciones son bienvenidas:
1. Fork del repositorio
2. Crear una rama para tu feature
3. Commit de tus cambios
4. Push a la rama
5. Crear Pull Request

## Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto
Para preguntas o sugerencias, abrir un issue en el repositorio.