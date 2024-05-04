import os

def limpiar_pantalla():
    os.system("cls")

def despedida():
    limpiar_pantalla()
    print("Hasta Pronto 👋")
    
def barra():
    print("----------------------------")
    
limpiar_pantalla()
print("C A L C U L A D O R A  S I M P L E\n")
input('Presiona Enter para continuar\n')

while True:
    limpiar_pantalla()
    print('''ESCRIBE LA OPCION A REALIZAR\n
1) SUMA
2) RESTA
3) MULTIPLICACION
4) DIVISION
5) SALIR
''')
    barra()
    opc = input('')
    limpiar_pantalla()

    if opc == '1' or opc == '2' or opc == '3' or opc == '4':
        print('Digite los numeros\n')
        
        while True:
            try:
                n1 = float(input('Primer Numero ---> '))
                n2 = float(input('Segundo Numero ---> '))
                break  
            except ValueError:
                print("Por favor, ingrese números válidos.")
                input()
                limpiar_pantalla()

        limpiar_pantalla()

        if opc == '1':
            resultado = n1 + n2
        elif opc == '2':
            resultado = n1 - n2
        elif opc == '3':
            resultado = n1 * n2
        elif opc == '4':
            if n2 == 0:
                print('No se puede dividir entre 0\n')
                input("PRESIONE ENTER PARA VOLVER AL INICIO")
                continue
            resultado = n1 / n2
    elif opc == '5':
        despedida()
    elif opc == "270205":
        print("""
                                                                                                                                                                                                                                                                          Hecho por eyeb4gs(Marlon)

                                                                                                                                                                                                                                                                          ( ͡❛ - ͡❛)👍
   """)
        break
    else:
        print("Dgite una opción válida (del 1 al 5)")
        input("PRESIONE ENTER PARA VOLVER AL INICIO")        
        continue
    print(f'El resultado es {resultado}')
    barra() 
    print('''
1) REALIZAR OTRA OPERACION\n
2) SALIR\n''')
        
    salir = input('-> ')
    if salir == '2':
        despedida()
        break
