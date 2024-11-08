class Vaga:
    def __init__(self, numero, tamanho):
        self.numero = numero
        self.tamanho = tamanho
        self.disponivel = True
        self.veiculo = None

    def ocupar(self, veiculo):
        self.disponivel = False
        self.veiculo = veiculo

    def liberar(self):
        self.disponivel = True
        self.veiculo = None
