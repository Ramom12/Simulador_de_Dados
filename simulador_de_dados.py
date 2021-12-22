import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_inicial = 1
        self.valor_final = 6
        # Criação do layout
        self.layout = [
            [sg.Text('Você gostaria de jogar o dado?')],
            [sg.Button('YES'),sg.Button('NOT')]
        ]
    #Inicio da simulação
    def Iniciar(self):
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'YES' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'NOT' or self.eventos == 'n':
                print('Obrigado por participar!')
            else:
                print('Erro, favor clicar em YES OR NOT')
        except:
            print('Ocorreu um erro ao receber sua resposta')
    
    def GerarValorDoDado(self):
        print(random.randint(self.valor_inicial,self.valor_final))

simulador = SimuladorDeDado()
simulador.Iniciar()