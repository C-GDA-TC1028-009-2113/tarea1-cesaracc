def main():
    #escribe tu código abajo de esta línea
    import math
    edad = int(input("Dame tu edad: "))
    añoa = int(input("Dame el año actual: "))
    añof = math.ceil((100 - edad) + añoa)
    print("Cumplirás 100 años en el año: " + str(añof))


if __name__ == '__main__':
    main()
