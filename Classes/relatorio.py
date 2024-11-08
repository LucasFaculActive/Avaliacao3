class Relatorio:
    def gerar_relatorio_vagas(estacionamento):
        for vaga in estacionamento.vagas:
            if not vaga.disponivel:
                print(f"Vaga {vaga.numero} - Tamanho: {vaga.tamanho} - Placa: {vaga.veiculo.placa}")

    def gerar_historico(estacionamento):
        for registro in estacionamento.historico:
            print(f"Placa: {registro['placa']}, Tempo: {registro['tempo']:.2f} horas, Valor Pago: R$ {registro['valor']:.2f}")
