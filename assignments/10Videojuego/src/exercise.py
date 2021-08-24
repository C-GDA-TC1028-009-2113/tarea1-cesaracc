def main():
    #escribe tu código abajo de esta línea
    jnuevos = int(input("Dame la cantidad de juegos nuevos: "))
    jusados = int(input("Dame la cantidad de juegos usados: "))
    total = (jnuevos * 1000) + (jusados * 350)
    print("El total de la compra es: " + str(total))



if __name__ == '__main__':
    main()
