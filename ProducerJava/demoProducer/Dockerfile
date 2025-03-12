# Etapa 1: Compilación con Maven
FROM maven:3.8.6-openjdk-21-slim AS build

WORKDIR /app

# Copiamos el archivo pom.xml y el directorio src para aprovechar el cache de Docker
COPY pom.xml .
COPY src ./src

# Compilamos y empaquetamos la aplicación (se puede omitir tests con -DskipTests)
RUN mvn clean package -DskipTests

# Etapa 2: Imagen final con OpenJDK
FROM openjdk:21-jdk-slim

WORKDIR /app

# Copiamos el .jar generado en la etapa de build
COPY --from=build /app/target/*.jar app.jar

# Exponemos el puerto configurado en la aplicación (ej. 8082)
EXPOSE 8081

ENTRYPOINT ["java", "-jar", "app.jar"]
