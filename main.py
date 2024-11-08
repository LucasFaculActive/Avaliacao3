from classes.vaga import Vaga
from classes.veiculo import Veiculo
from classes.estacionamento import Estacionamento
from classes.relatorio import Relatorio

def main():
    estacionamento = Estacionamento()

    estacionamento.adicionar_vaga(Vaga(1, 'pequeno'))
    estacionamento.adicionar_vaga(Vaga(2, 'médio'))
    estacionamento.adicionar_vaga(Vaga(3, 'grande'))

    while True:
        print("\n1. Registrar Entrada\n2. Registrar Saída\n3. Ver Relatório de Vagas\n4. Ver Histórico\n5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            placa = input("Placa do veículo: ")
            modelo = input("Modelo do veículo: ")
            tamanho = input("Tamanho do veículo (pequeno, médio, grande): ")
            veiculo = Veiculo(placa, modelo, tamanho)
            vaga = estacionamento.registrar_entrada(veiculo)
            if vaga:
                print(f"Veículo estacionado na vaga {vaga.numero}.")
            else:
                print("Nenhuma vaga disponível para o tamanho do veículo.")
        
        elif opcao == '2':
            placa = input("Placa do veículo para saída: ")
            for vaga in estacionamento.vagas:
                if vaga.veiculo and vaga.veiculo.placa == placa:
                    valor = estacionamento.registrar_saida(vaga.veiculo)
                    print(f"Valor a pagar: R$ {valor:.2f}")
                    break
            else:
                print("Veículo não encontrado.")

        elif opcao == '3':
            Relatorio.gerar_relatorio_vagas(estacionamento)

        elif opcao == '4':
            Relatorio.gerar_historico(estacionamento)

        elif opcao == '5':
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
