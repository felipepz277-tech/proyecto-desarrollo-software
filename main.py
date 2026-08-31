print("===================================")
print("PROYECTO DE DESARROLLO DE  SOFTWARE")
print("===================================")

print("Bienvenido al proyecto")
print("Estudiantes: James Reyes y Felipe Paez ")
print("Curso: 10A")

from operaciones import sumar, restar, multiplicar, dividir

print("==============================")
print("     CALCULADORA EN PYTHON")
print("==============================")

num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))

print("\nResultados:")

print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2))
print("Multiplicación:", multiplicar(num1, num2))
print("División:", dividir(num1, num2))