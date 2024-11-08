from datetime import datetime

class Veiculo:
    def __init__(self, placa, modelo, tamanho):
        self.placa = placa
        self.modelo = modelo
        self.tamanho = tamanho 
        self.hora_entrada = None
        self.hora_saida = None

    def registrar_entrada(self):
        self.hora_entrada = datetime.now()

    def registrar_saida(self):
        self.hora_saida = datetime.now()

    def calcular_tempo(self):
        if self.hora_entrada and self.hora_saida:
            return (self.hora_saida - self.hora_entrada).total_seconds() / 3600
        return 0
