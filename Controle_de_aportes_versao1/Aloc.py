# -*- coding: utf-8 -*-
"""
Controle Pessoal de Aportes
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

MINHA_DISTRIBUICAO = {
    'Cripto': 0.10,
    'Reserva Emergência': 0.10,
    'Reserva Oportunidade': 0.20,
    'Ações': 0.40,
    'FIIs': 0.20
}

# Se alguma coisa ficar mais de 10% fora da banda de desbalanceamento
LIMITE_ACEITAVEL = 0.10

# Arquivo onde vou guardar tudo
ARQUIVO_REGISTRO = 'meus_aportes.csv'

def calcular_quanto_devo_colocar(valor_total):
    """Calcula base de acordo com os aportes pré estabelecidos"""
    resultado = {}
    
    # Para cada tipo de investimento na minha lista
    for tipo, porcentagem in MINHA_DISTRIBUICAO.items():
        # Calcula quanto dinheiro vai para esse tipo
        resultado[tipo] = valor_total * porcentagem
    
    return resultado

def mostrar_distribuicao_ideal(valores_calculados):
    """Mostra na tela como eu deveria distribuir meu dinheiro"""
    print("\n" + "="*50)
    print("ASSIM QUE EU DEVERIA DISTRIBUIR MEU DINHEIRO")
    print("="*50)
    
    # Mostra cada tipo e quanto deveria colocar
    for tipo, valor in valores_calculados.items():
        # Pega a porcentagem que defini para esse tipo
        porcentagem = MINHA_DISTRIBUICAO[tipo] * 100
        print(f"{tipo:<25} R$ {valor:>8.2f} ({porcentagem:.0f}%)")
    
    # Soma tudo para ver o total
    total = sum(valores_calculados.values())
    print("-"*50)
    print(f"{'TOTAL':<25} R$ {total:>8.2f}")

def registrar_meu_aporte():
    """Aqui eu registro quanto coloquei de verdade em cada tipo"""
    print("\n" + "="*50)
    print("REGISTRAR O QUE EU FIZ NA PRÁTICA")
    print("="*50)
    print("Vamos colocar quanto eu realmente investi em cada coisa:")
    
    # Pega a data do aporte
    data = input("Data que fiz o aporte (DD/MM/AAAA): ").strip()
    if data == "":
        # Se não colocar nada, usa a data de hoje
        data = datetime.now().strftime("%d/%m/%Y")
    
    # Dicionário para guardar quanto coloquei em cada tipo
    meu_aporte_real = {}
    
    # Pede valor para cada tipo de investimento
    for tipo in MINHA_DISTRIBUICAO:
        while True:
            try:
                valor_digitado = input(f"{tipo}: R$ ")
                valor = float(valor_digitado)
                
                if valor < 0:
                    print("Valor negativo é invalido")
                    continue
                    
                meu_aporte_real[tipo] = valor
                break
            except:
                print("Não é numero valido ")
    
    # Salva no arquivo CSV
    with open(ARQUIVO_REGISTRO, 'a', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        
        # Escreve uma linha para cada tipo
        for tipo, valor in meu_aporte_real.items():
            escritor.writerow([data, tipo, valor])
    
    print(f"\n Aporte Registrado {data}!")
    
    # Mostra quanto investiu no total
    total_investido = sum(meu_aporte_real.values())
    print(f"No total, você investiu R$ {total_investido:.2f} nesse aporte.")

def calcular_como_esta_minha_carteira():
    """Vejo como está a distribuição do meu dinheiro até agora"""
    try:
        # Tenta abrir o arquivo com meus registros
        with open(ARQUIVO_REGISTRO, 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            todos_registros = list(leitor_csv)
    except FileNotFoundError:
        # Se o arquivo não existir, retorna vazio
        return {}, 0
    
    # Aqui vou somar tudo que coloquei em cada tipo
    soma_por_tipo = {}
    total_geral = 0
    
    for registro in todos_registros:
        if len(registro) < 3:
            # Linha com problema, pula
            continue
            
        tipo_investimento = registro[1]
        valor_investido = float(registro[2])
        
        # Soma ao que já tinha desse tipo
        if tipo_investimento in soma_por_tipo:
            soma_por_tipo[tipo_investimento] += valor_investido
        else:
            soma_por_tipo[tipo_investimento] = valor_investido
        
        total_geral += valor_investido
    
    # Calcula a porcentagem atual de cada tipo
    porcentagem_atual = {}
    for tipo, valor in soma_por_tipo.items():
        if total_geral > 0:
            porcentagem_atual[tipo] = valor / total_geral
        else:
            porcentagem_atual[tipo] = 0
    
    return porcentagem_atual, total_geral

def verificar_se_esta_desbalanceado():
    """Verifica se minha carteira está muito diferente do que planejei"""
    como_esta_agora, total_carteira = calcular_como_esta_minha_carteira()
    
    if total_carteira == 0:
        print("\nVocê ainda não registrou nenhum aporte.")
        return
    
    print("\n" + "="*50)
    print("VAMOS VER SE ESTÁ TUDO CERTO...")
    print("="*50)
    print(f"Valor total que tenho investido: R$ {total_carteira:.2f}")
    print("-"*50)
    
    # Listas para os avisos
    problemas_graves = []
    pequenos_desvios = []
    
    # Junto todos os tipos que preciso verificar
    todos_tipos = set(MINHA_DISTRIBUICAO.keys())
    for tipo in como_esta_agora.keys():
        todos_tipos.add(tipo)
    
    # Verifica cada tipo
    for tipo in todos_tipos:
        # Qual a porcentagem ideal
        porcentagem_ideal = MINHA_DISTRIBUICAO.get(tipo, 0)
        
        # Qual a porcentagem atual
        porcentagem_atual = como_esta_agora.get(tipo, 0)
        
        # Calcula a diferença
        diferenca = porcentagem_atual - porcentagem_ideal
        
        # Se a diferença for grande, é problema grave
        if abs(diferenca) >= LIMITE_ACEITAVEL:
            problemas_graves.append((tipo, diferenca*100))
        elif abs(diferenca) > 0.01:
            # Diferença pequena, só para eu saber
            pequenos_desvios.append((tipo, diferenca*100))
    
    # Mostra os problemas graves primeiro
    if problemas_graves:
        print("\n⚠️  ATENÇÃO! Tem coisa Errada")
        print("-"*30)
        for tipo, diferenca in problemas_graves:
            if diferenca > 0:
                print(f"{tipo:<25} ESTÁ {abs(diferenca):.1f}% ACIMA do que deveria")
            else:
                print(f"{tipo:<25} ESTÁ {abs(diferenca):.1f}% ABAIXO do que deveria")
    
    # Mostra os desvios pequenos
    if pequenos_desvios:
        print("\n💡 Presta atenção:")
        print("-"*30)
        for tipo, diferenca in pequenos_desvios:
            if diferenca > 0:
                print(f"{tipo:<25} está {abs(diferenca):.1f}% acima")
            else:
                print(f"{tipo:<25} está {abs(diferenca):.1f}% abaixo")
    
    # Se estiver tudo dentro do aceitável
    if not problemas_graves and not pequenos_desvios:
        print("\n✅ Tudo ok ! Sua carteira está bem balanceada.")
    
    # Mostra uma tabela comparativa
    print("\n" + "-"*60)
    print(f"{'Tipo de investimento':<25} {'Atual':<10} {'Ideal':<10} {'Diferença':<12}")
    print("-"*60)
    
    for tipo in todos_tipos:
        ideal = MINHA_DISTRIBUICAO.get(tipo, 0) * 100
        atual = como_esta_agora.get(tipo, 0) * 100
        diferenca = atual - ideal
        
        # Formata a diferença com sinal
        if diferenca > 0:
            diferenca_formatada = f"+{diferenca:.1f}%"
        else:
            diferenca_formatada = f"{diferenca:.1f}%"
        
        print(f"{tipo:<25} {atual:<10.1f} {ideal:<10.1f} {diferenca_formatada:<12}")

def fazer_grafico_evolucao():
    """Faz um gráfico mostrando como meu dinheiro foi crescendo"""
    try:
        with open(ARQUIVO_REGISTRO, 'r') as arquivo:
            leitor = csv.reader(arquivo)
            dados = list(leitor)
    except FileNotFoundError:
        print("Ops! Não achei o arquivo com os registros.")
        return
    
    if not dados:
        print("Não tem nada registrado ainda.")
        return
    
    # Organiza os dados por data
    dados_por_data = {}
    todos_tipos = set()
    
    for linha in dados:
        if len(linha) < 3:
            continue
        
        data = linha[0]
        tipo = linha[1]
        valor = float(linha[2])
        
        if data not in dados_por_data:
            dados_por_data[data] = {}
        
        # Soma o valor para essa data e tipo
        if tipo in dados_por_data[data]:
            dados_por_data[data][tipo] += valor
        else:
            dados_por_data[data][tipo] = valor
            
        todos_tipos.add(tipo)
    
    # Coloca as datas em ordem
    datas_ordenadas = sorted(dados_por_data.keys(), 
                           key=lambda x: datetime.strptime(x, "%d/%m/%Y"))
    
    # Prepara os dados para o gráfico
    todos_tipos = sorted(list(todos_tipos))
    valores_acumulados = {tipo: [] for tipo in todos_tipos}
    
    # Começa com zero em tudo
    acumulado = {tipo: 0 for tipo in todos_tipos}
    
    # Para cada data, vai acumulando
    for data in datas_ordenadas:
        for tipo in todos_tipos:
            # Adiciona o valor desse aporte (se tiver)
            if tipo in dados_por_data[data]:
                acumulado[tipo] += dados_por_data[data][tipo]
            
            # Guarda o valor acumulado até essa data
            valores_acumulados[tipo].append(acumulado[tipo])
    
    # Cria o gráfico
    figura, eixos = plt.subplots(figsize=(12, 6))
    
    # Começa com barras de tamanho zero
    base = [0] * len(datas_ordenadas)
    
    # Para cada tipo, faz uma barra
    cores = ['blue', 'green', 'orange', 'red', 'purple', 'brown']
    cor_index = 0
    
    for tipo in todos_tipos:
        valores = valores_acumulados[tipo]
        
        # Só mostra no gráfico se tiver algum valor
        if sum(valores) > 0:
            eixos.bar(datas_ordenadas, valores, bottom=base, 
                     label=tipo, color=cores[cor_index % len(cores)])
            
            # Atualiza a base para a próxima barra
            base = [base[i] + valores[i] for i in range(len(valores))]
            cor_index += 1
    
    eixos.set_xlabel('Data do aporte')
    eixos.set_ylabel('Total acumulado (R$)')
    eixos.set_title('Como foi crescendo meu dinheiro ao longo do tempo')
    eixos.legend(title='Tipos de investimento')
    
    # Inclina as datas para caber melhor
    plt.xticks(rotation=45)
    
    # Ajusta o layout para não cortar nada
    plt.tight_layout()
    
    # Mostra o gráfico
    plt.show()
    
    print(f"\nGrágico pronto! Mostrando {len(datas_ordenadas)} aportes.")

def mostrar_menu():
    """Mostra o menu principal e lida com as escolhas"""
    while True:
        print("\n" + "="*50)
        print("MEU CONTROLE DE INVESTIMENTOS")
        print("="*50)
        print("1. Registrar um novo aporte")
        print("2. Ver se minha carteira está balanceada")
        print("3. Ver gráfico da evolução")
        print("4. Sair do programa")
        
        escolha = input("\nO que você quer fazer? (1-4): ").strip()
        
        if escolha == '1':
            registrar_meu_aporte()
        elif escolha == '2':
            verificar_se_esta_desbalanceado()
        elif escolha == '3':
            fazer_grafico_evolucao()
        elif escolha == '4':
            print("\nTchau! Até a próxima! 😊")
            break
        else:
            print("Essa opção não existe! Tenta de novo com 1, 2, 3 ou 4.")

def main():
    """Função principal"""
    print("="*50)
    print("CONTROLE SIMPLES DE INVESTIMENTOS")
    print("="*50)
    print("Controle pessoal de aportes")
    
    # Pede o valor do aporte
    while True:
        try:
            valor_aporte = float(input("\nQuanto você tem para investir este mês? R$ "))
            
            if valor_aporte <= 0:
                print("Tem que ser um valor positivo, né?")
                continue
                
            break
        except:
            print("Isso não é um número! Digita só números, por favor.")
    
    # Calcula como deveria distribuir
    distribuicao_ideal = calcular_quanto_devo_colocar(valor_aporte)
    
    # Mostra como deveria distribuir
    mostrar_distribuicao_ideal(distribuicao_ideal)
    
    # Mostra o menu
    mostrar_menu()

# Isso aqui é para o programa começar quando eu executar
if __name__ == "__main__":
    main()