# Usar la imagen oficial de Python
FROM python:3.12

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5051

# Ejecutar la aplicación
CMD ["python", "productor.py"]