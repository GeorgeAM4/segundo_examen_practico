while True:
    try:
        n = int(input("inngrese un numero entero (mayor a 0): "))
        if n > 0:
            break
        else:
            print("error el numero debe ser mayor a 0 intente nuevamente.\n")
    except ValueError:
        print("error debe ingresar un número entero valido.\n")
fibonacci = []
a, b = 0, 1
for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b
print(f"\nlos primeros {n} términos de la sucesion de fibonacci son:")
print(" -> ".join(map(str, fibonacci)))

