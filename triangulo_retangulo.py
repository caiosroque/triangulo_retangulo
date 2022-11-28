import threading
import os
import keyboard

def encerrar():
    while True:
     if keyboard.is_pressed('esc'):
        os._exit(0)

def calcular():
    while True:
        lado1 = int(input("Digite o tamanho do primeiro lado: "))
        lado2 = int(input("Digite o tamanho do segundo lado: "))
        lado3 = int(input("Digite o tamanho do terceiro lado: "))

        if lado1 > lado2 and lado1 > lado3:
            area = (lado2 * lado3) / 2
            print(f"A area do triangulo retangulo é de {area}cm²")
            print(f"A hipotenusa tem {lado1}cm")

        elif lado2 > lado1 and lado2 >lado3:
            area = (lado1 * lado3) / 2
            print(f"A area do triangulo retangulo é de {area}cm²")
            print(f"A hipotenusa tem {lado2}cm")

        elif lado3 > lado1 and lado3 > lado2:
            area = (lado1 * lado2) / 2
            print(f"A area do triangulo retangulo é de {area}cm²")
            print(f"A hipotenusa tem {lado3}cm")

threading.Thread(target=encerrar).start()
threading.Thread(target=calcular).start()
    

        

        



