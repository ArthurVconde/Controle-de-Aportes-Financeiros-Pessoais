# 📊 Controle de Aportes Financeiros Pessoais

Programa em **Python** desenvolvido **para uso pessoal**, com o objetivo de auxiliar no controle e organização de investimentos, focando em **alocação estratégica**, **registro histórico de aportes** e **análise de desbalanceamento da carteira**.

O projeto também faz parte do meu **portfólio**, demonstrando a aplicação prática de Python, análise de dados e boas práticas de desenvolvimento em um problema real do dia a dia.
---
## 🤖 Uso de Inteligência Artificial

A Inteligência Artificial foi utilizada como ferramenta de apoio durante o desenvolvimento do projeto, contribuindo para:

- Refinamento da lógica e fluxo do programa  
- Melhoria da legibilidade e organização do código  
- Revisão de regras de negócio e tratamento de exceções  

Todas as decisões finais de implementação, validação e testes foram realizadas manualmente.

---

## 🎯 Objetivo do Projeto

- Automatizar o cálculo de aportes mensais com base em uma alocação definida  
- Manter um histórico persistente de investimentos realizados  
- Identificar desbalanceamentos da carteira de forma clara e quantitativa  
- Gerar visualizações gráficas da evolução dos aportes  
- Aplicar conceitos de programação, análise de dados e organização de código  

---

## ✨ Funcionalidades

### 📈 Cálculo Automático de Aportes
- Distribuição ideal do aporte mensal
- Percentuais configuráveis por classe de ativo
- Relatório detalhado com valores e percentuais

### 📝 Registro Histórico
- Registro dos valores realmente investidos
- Armazenamento persistente em arquivo CSV
- Acúmulo automático dos aportes ao longo do tempo
- Registro de datas e valores

### ⚖️ Análise de Desbalanceamento
- Comparação entre alocação atual e alocação ideal
- Cálculo de desvios percentuais por classe
- Alertas graduados:
  - Informativo (≤ 10%)
  - Urgente (> 10%)
- Exibição de tabela comparativa detalhada

### 📊 Visualização Gráfica
- Gráfico de barras acumuladas da evolução da carteira
- Crescimento individual por classe de ativo
- Geração automática utilizando matplotlib

---

## 🗂️ Alocação Padrão da Carteira

| Classe de Ativo | Percentual Ideal |
|-----------------|------------------|
| Ações | 40% |
| FIIs | 20% |
| Reserva de Oportunidade | 20% |
| Cripto | 10% |
| Reserva de Emergência | 10% |

> Todos os percentuais podem ser alterados diretamente no código.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6+
- Biblioteca matplotlib

```bash
pip install matplotlib
