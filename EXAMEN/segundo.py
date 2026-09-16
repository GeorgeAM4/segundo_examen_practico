tarifas = {
    '1': ("auto", 10),
    '2': ("moto", 5),
    '3': ("camion", 20),
}
while True:
    try:
        print("vehiculos")
        print("1 auto (10 Bs/hora)")
        print("2 moto (5 Bs/hora)")
        print("3 camion (20 Bs/hora)")
        opcion = input("seleccione el tipo de vehiculo (1, 2 o 3): ").strip()
        if opcion not in tarifas:
            raise ValueError("opcion de vehiculo no valida.")
        horas = float(input("ingrese las horas de parqueo: "))
        if horas <= 0:
            raise ValueError("las horas deben ser mayores a 0.")
        break
    except ValueError as e:
        print(f"error: {e} intente de nuevo.\n")
    except Exception as e:
        print(f"oocurrio un error inesperado: {e}\n")
tipo_vehiculo, tarifa_hora = tarifas[opcion]
subtotal = horas * tarifa_hora
recargo = 0.0
if horas > 4:
    recargo = subtotal * 0.15
monto_total = subtotal + recargo
print("\n" + "="*35)
print("detalles de cobro2")
print("="*35)
print(f"tipo de vehículo: {tipo_vehiculo}")
print(f"horas estacionado: {horas:.2f} hrs")
print(f"tarifa por hora : {tarifa_hora} Bss")
print(f"subtotal        : {subtotal:.2f} Bs")
if recargo > 0:
    print(f"recargo (15%)   : {recargo:.2f} Bs")
else:
    print("recargo (15%)   : 0.00 Bs")
print("-" * 35)
print(f"monto final : {monto_total:.2f} Bs")
print("="*35)
