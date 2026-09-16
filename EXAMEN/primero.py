while True:
    try:
        n = int(input("Ingrese un número entero N (mayor a 0): "))
        if n > 0:
            break
        else:
            print("Error: El número debe ser mayor a 0. Intente nuevamente.\n")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.\n")
fibonacci = []
a, b = 0, 1
for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b
print(f"\nlos primeros {n} términos de la sucesion de fibonacci son:")
print(" -> ".join(map(str, fibonacci)))

