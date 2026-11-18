# Programa para calcular el IMC

# 1. Entrada de datos
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# 2. Calculo del IMC
imc = peso / (estatura ** 2)

# 3. Mostrar resultados
print("\n--- RESULTADOS ---")
print("Edad:", edad, "años")
print("Peso:", peso, "kg")
print("Estatura:", estatura, "m")
print("Tu IMC es:", round(imc, 2))