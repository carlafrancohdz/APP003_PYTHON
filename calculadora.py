#Relaizar una calculadora matemática

print("Bienvendio a la calculadora")

num1=float(input("ingresa el primer número"))
num2=float(input("ingresa el segundo valor"))

suma=num1+num2
resta=num1-num2
multiplicación=num1*num2
division=num1/num2

print("El resultado de la suma es: ",suma)
print("El resultado de la resta es: ",resta)
print("El resultado de la multiplicación es: ",multiplicación)
print("El resultado de la división es: ",division)

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion=input("Ingresa el número de la opción: ")

#Evaluar la opción seleccionada 
if opcion == "1":
    resultado = num1 + num2 
    print("El resultado de la suma es:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif opcion == "3": 
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif opcion == "4": 
    if num2 != 0: #Evitar división entre 0
        resultado = num1 / num2
        print ("El resultado de la división es:", resultado)
    else:
        print ("Error: No se puede dividir entre 0")
else:
    print("Opción no válida")