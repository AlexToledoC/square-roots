def run():
    numero = float(input("Escribe un número: "))
    answer = numero**.5
    answer = round(answer, 2)
    print(f"La raíz cuadrada de {numero} es {answer}")

if __name__ == '__main__':
    run()