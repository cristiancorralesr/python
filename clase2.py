import math

numero_texto = input("Ingrese el radio del círculo: ")

radio = float(numero_texto)

print(radio,type(radio))

area = math.pi * (radio * radio)

area = math.pi * (radio ** 2)

print("El área del círculo es:", area)

#Tipos de datos

print(type([]))  #Lista
print(type({}))  #diccionario
print(type(()))  #tupla
