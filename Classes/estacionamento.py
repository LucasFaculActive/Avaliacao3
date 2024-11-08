class Estacionamento:
    def __init__(self):
        self.vagas = []
        self.historico = []

    def adicionar_vaga(self, vaga):
        self.vagas.append(vaga)

    def encontrar_vaga_disponivel(self, tamanho):
        for vaga in self.vagas:
            if vaga.disponivel and vaga.tamanho == tamanho:
                return vaga
        return None

    def registrar_entrada(self, veiculo):
        vaga = self.encontrar_vaga_disponivel(veiculo.tamanho)
        if vaga:
            veiculo.registrar_entrada()
            vaga.ocupar(veiculo)
            return vaga
        return None

    def registrar_saida(self, veiculo):
        for vaga in self.vagas:
            if vaga.veiculo == veiculo:
                veiculo.registrar_saida()
                tempo = veiculo.calcular_tempo()
                valor = self.calcular_valor(tempo)
                self.historico.append({
                    "placa": veiculo.placa,
                    "tempo": tempo,
                    "valor": valor
                })
                vaga.liberar()
                return valor
        return None

    def calcular_valor(self, tempo):
        if tempo <= 1:
            return 5.00
        elif tempo <= 3:
            return 10.00
        else:
            return 15.00
