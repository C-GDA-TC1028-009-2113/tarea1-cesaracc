def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Dame tu edad: "))
    añoa = int(input("Dame el año actual: "))
    añof = (100 - edad) + añoa
    print("Cumplirás 100 años en el año: " + str(añof))


if __name__ == '__main__':
    main()
