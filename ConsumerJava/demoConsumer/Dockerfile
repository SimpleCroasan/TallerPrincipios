# Etapa 1: Compilación con Maven y OpenJDK 21
FROM maven:3-eclipse-temurin-21 AS build

WORKDIR /app

# Copia los archivos necesarios para compilar el proyecto
COPY pom.xml .
COPY src ./src

# Compila el proyecto (se pueden omitir tests con -DskipTests)
RUN mvn clean package -DskipTests

# Etapa 2: Imagen final con OpenJDK 21
FROM eclipse-temurin:21-jdk AS runtime

WORKDIR /app

# Copia el .jar generado en la etapa de build
COPY --from=build /app/target/*.jar app.jar

# Expone el puerto configurado en la aplicación
EXPOSE 8082

ENTRYPOINT ["java", "-jar", "app.jar"]
