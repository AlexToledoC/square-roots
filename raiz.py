def run():
    objetivo = int(input("Escribe un número: "))
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f"{objetivo} no tiene raíz cuadrada exacta.")


if __name__ == '__main__':
    run()