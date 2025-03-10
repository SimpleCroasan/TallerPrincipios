# Usa una imagen base de OpenJDK (puedes ajustar la versión según tus necesidades)
FROM openjdk:21-jdk-slim


# Directorio de trabajo en el contenedor
WORKDIR /app

# Copia el JAR generado (asegúrate de que el build coloque el JAR en target)
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar

# Expone el puerto de la aplicación (configurado en application.properties, ej. 8081 o 8082)
EXPOSE 8081

# Comando de inicio de la aplicación
ENTRYPOINT ["java", "-jar", "app.jar"]
