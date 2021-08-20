def main():
    #escribe tu código abajo de esta línea
    edad=int(input('Ingresa tu edad: '))
    #
    if edad>=18:
        ide=input('¿Tienes identificación oficial? (s/n): ')
        if ide=='s':
            print('Trámite de licencia concedido')
        elif ide=='n':
            print('No cumples requisitos')
        else:
            print('Respuesta incorrecta')
    elif edad<18 and edad>0:
        print('No cumples requisitos')
    else:
        print('Respuesta incorrecta')

if __name__ == '__main__':
    main()
