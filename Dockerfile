# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

COPY requirements.txt .

# Copiamos los requisitos e instalamos
RUN pip install fastapi uvicorn

# Copiamos el código
COPY main.py .

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para ejecutar la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]