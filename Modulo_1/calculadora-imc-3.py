# Programa para calcular el IMC

print("===================================")
print("     CALCULADORA DE IMC")
print("===================================")

# Captura de datos personales
nombre = input("Ingresa tu nombre: ").strip().title()
apellido = input("Ingresa tu apellido: ").strip().title()

# Captura de datos físicos
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

# Cálculo del IMC
imc = peso / (altura ** 2)

# Redondear a dos decimales
imc = round(imc, 2)

# Presentación de resultados
print("\n===================================")
print("       REPORTE DE RESULTADOS")
print("===================================")

print(f"Nombre completo: {nombre} {apellido}")
print(f"Peso registrado: {peso} kg")
print(f"Altura registrada: {altura} metros")
print(f"Tu IMC es: {imc:.2f}")

print("===================================")
print("       FIN DEL PROGRAMA")
print("===================================")