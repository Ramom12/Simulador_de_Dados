import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_inicial = 1
        self.valor_final = 6
        # Layout
        self.layout = [
            [sg.Text('Você gostaria de jogar o dado?')],
            [sg.Button('sim'),sg.Button('Não')]
        ]
    
    def Iniciar(self):
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Obrigado por participar!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')
    
    def GerarValorDoDado(self):
        print(random.randint(self.valor_inicial,self.valor_final))

simulador = SimuladorDeDado()
simulador.Iniciar()