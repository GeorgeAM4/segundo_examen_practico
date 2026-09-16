while True:
    try:
        x = int(input("ingrese un numero entero entre 1 y 10: "))
        if 1 <= x <= 10:
            break
        else:
            print("error: el numero debe estar en el rango de 1 a 10.\n")
    except ValueError:
        print("error: por favor, ingrese un numero entero valido.\n")
print(f"\ntabla de multiplicar {x}")
suma_total = 0
for i in range(1, 13):
    resultado = x * i
    suma_total += resultado
    print(f"{x} * {i:2d} = {resultado}")
print("-" * 30)
print(f"total acumulado de la suma: {suma_total}")