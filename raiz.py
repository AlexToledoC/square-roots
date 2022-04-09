def run():
    numero = int(input("Escribe un número: "))
    answer = numero**.5
    if answer == int(answer):
        answer = int(answer)
        print(f"La raíz cuadrada de {numero} es {answer}")
    else:
        print(f"{numero} no tiene raíz cuadrada exacta.")

if __name__ == '__main__':
    run()