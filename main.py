# main.py

# Importar las funciones de los otros archivos
from sumar import suma
from restar import resta
from multiplicacion import mult
from dividir import div
from suma_avanzada import suma_n

def get_num(msg):
    """
    Solicita al usuario un número y valida la entrada.
    """
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("¡Error! Debes ingresar un valor numérico válido.")

def menu():
    """
    Muestra el menú de opciones de la calculadora.
    """
    print("\n--- CALCULADORA VERSÁTIL ---")
    print("1. Suma de dos números")
    print("2. Resta de dos números")
    print("3. Multiplicación de dos números")
    print("4. División de dos números")
    print("5. Suma de múltiples números")
    print("6. Salir de la aplicación")
    print("--------------------------")

def app():
    """
    Función principal para ejecutar la calculadora.
    """
    while True:
        menu()
        opt = input("Selecciona una opción (1-6): ")

        if opt == '1':
            n1 = get_num("Introduce el primer número: ")
            n2 = get_num("Introduce el segundo número: ")
            print(f"El resultado de la suma es: {suma(n1, n2)}")
        
        elif opt == '2':
            n1 = get_num("Introduce el primer número: ")
            n2 = get_num("Introduce el segundo número: ")
            print(f"El resultado de la resta es: {resta(n1, n2)}")
        
        elif opt == '3':
            n1 = get_num("Introduce el primer número: ")
            n2 = get_num("Introduce el segundo número: ")
            print(f"El resultado de la multiplicación es: {mult(n1, n2)}")
        
        elif opt == '4':
            n1 = get_num("Introduce el dividendo: ")
            n2 = get_num("Introduce el divisor: ")
            res = div(n1, n2)
            print(f"El resultado de la división es: {res}")
        
        elif opt == '5':
            nums_str = input("Ingresa los números a sumar, separados por comas (ej: 10, 5.5, 20): ")
            try:
                l_nums = [float(n.strip()) for n in nums_str.split(',') if n.strip()]
                if not l_nums:
                    print("No se detectaron números válidos para sumar.")
                else:
                    print(f"La suma total de {l_nums} es: {suma_n(*l_nums)}")
            except ValueError:
                print("¡Error! Asegúrate de que todos los valores sean numéricos y estén separados por comas.")
        
        elif opt == '6':
            print("¡Cerrando la calculadora! Que tengas un buen día.")
            break
        
        else:
            print("Opción no reconocida. Por favor, elige un número del 1 al 6 del menú.")

# Esto asegura que app() se ejecute solo cuando el script se corre directamente
if __name__ == "__main__":
    app()