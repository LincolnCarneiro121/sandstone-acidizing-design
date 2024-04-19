import numpy as np
import matplotlib.pyplot as plt

from calculate import Calculate


class Manager(Calculate):
    def __init__(self):
        self.inpt = input('iniciar simulador? [Y/N]: ')
        self.run()

    def terminal_init(self):
        while(True):
            if self.inpt == 'Y':
                return self.terminal_options()
            if self.inpt == 'N':
                self.leave()
                break
            return self.__init__()

    def terminal_options(self):
        while(True):
            option = input('O que você deseja fazer? \n [1] - Volume de Colchão de Lavagem Ácida \n [2] - Vazão Máxima de Injeção Ácida e Pressão de Injeção \n [3] - Sair \n -> ')
            match(option):
                case "1":
                    self.calculate_required_acid_volume()
                case "2":
                    self.calculate_injection_pump_flow_and_pressure()
                case "3":
                    return self.leave()
                case _:
                    self.terminal_options()

    def leave(self):
        leave_msg = 'Terminal finalizado.'
        print(leave_msg)
        return

    def run(self):
        self.terminal_init()

Manager()