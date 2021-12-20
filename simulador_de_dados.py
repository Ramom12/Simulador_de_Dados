# Simular um dado indo de 1 ao número 6
import random


class SimuladorDeDado:
    def __init__(self):
        self.valor_inicial = 1
        self.valor_final = 6
        self.mensagem = 'Você gostaria de jogar o dado??'

    def iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Obrigado pela sua participação')
            else:
                print('Favor Digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_inicial, self.valor_final))


simulador = SimuladorDeDado()
simulador.iniciar()
