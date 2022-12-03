import PySimpleGUI as sg
from triangulo_retangulo import calcular

layout = [
    [sg.Text("Digite o tamanho do primeiro lado:")],
    [sg.Input(key="lado1")],
    [sg.Text("Digite o tamanho do segundo lado:")],
    [sg.Input(key="lado2")],
    [sg.Text("Digite o tamanho do terceiro lado:")],
    [sg.Input(key="lado3")],
    [sg.Button("Calcular"), sg.Button("Cancelar")],
    [sg.Text("", key="texto_resultado")],
] 

janela = sg.Window("Calculadora", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Calcular":
        lado1 = float(valores["lado1"])
        lado2 = float(valores["lado2"])
        lado3 = float(valores["lado3"])
        resultado = calcular(lado1, lado2, lado3)
        janela["texto_resultado"].update(f"A area do retangulo é {resultado}")

janela.close()


