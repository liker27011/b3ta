import random

NUM_CLIENTES = 5
MIN_INGRESO = 1000000
MAX_INGRESO = 8000000
ENCABEZADO = "REPORTE FINANCIERO - FINANSMART INC."

clientes = []

for i in range(NUM_CLIENTES):
    print(f"\nIngrese los datos del Cliente {i + 1}")
    nombre = input("Nombre completo: ")
    id_numero = input("Número de identificación: ")
    edad = int(input("Edad: "))
    gastos = float(input("Gastos mensuales (COP): "))
    telefono = input("Número de celular: ")
    direccion = input("Dirección: ")
    estado = True  

    ingreso = random.randint(MIN_INGRESO, MAX_INGRESO)
    balance = ingreso - gastos

    cliente_info = {
        "Nombre": nombre,
        "ID": id_numero,
        "Edad": edad,
        "Gastos": gastos,
        "Ingreso": ingreso,
        "Balance": balance,
        "Teléfono": telefono,
        "Dirección": direccion,
        "Estado": estado
    }

    clientes.append(cliente_info)

print("\n" + ENCABEZADO)
print("-" * len(ENCABEZADO))

for idx, cliente in enumerate(clientes, start=1):
    print(f"\nCliente {idx}")
    print(f"Nombre: {cliente['Nombre']}")
    print(f"ID: {cliente['ID']}")
    print(f"Edad: {cliente['Edad']}")
    print(f"Teléfono: {cliente['Teléfono']}")
    print(f"Dirección: {cliente['Dirección']}")
    print(f"Estado Activo: {cliente['Estado']}")
    print(f"Ingreso mensual: ${cliente['Ingreso']:,.0f} COP")
    print(f"Gastos mensuales: ${cliente['Gastos']:,.0f} COP")
    print(f"Balance estimado: ${cliente['Balance']:,.0f} COP")
