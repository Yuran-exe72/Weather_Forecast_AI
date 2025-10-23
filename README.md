# 🌦️ Projeto de Previsão do Tempo com Rede Neural Artificial

Este projeto tem como objetivo prever a **temperatura do dia seguinte** com base em dados de temperaturas anteriores.  
Foi desenvolvida uma **rede neural artificial simples** utilizando a biblioteca **TensorFlow/Keras**, que aprende os padrões nos dados e realiza previsões futuras.



## 🎯 Objetivo do Projeto

O principal objetivo é aplicar os conhecimentos de **Aprendizagem de Máquina (AM)** para construir um modelo inteligente capaz de realizar previsões.  
A escolha do tema foi feita por ser um exemplo prático, fácil de entender e que mostra como a **inteligência artificial** pode ser usada em problemas do mundo real



## Conjunto de Dados

O conjunto de dados está no arquivo:
**data/temperaturas.csv**


O ficheiro contém duas colunas:

**Data** – dia da medição  
**Temperatura** – valor registado da temperatura

### Pré-processamento dos Dados
Antes de usar os dados no modelo:
Foram removidas linhas com erros ou valores em falta;
As temperaturas foram convertidas em valores numéricos;
Foram criadas duas listas: uma com a temperatura do dia atual e outra com a do dia seguinte.



## 🤖 Modelo Utilizado

Foi criada uma **Rede Neural Artificial** simples composta por:

**Camada 1** 8 neurónios, função de ativação *ReLU*  
**Camada 2** 1 neurónio (saída)

###  Configurações do Modelo
**Otimizador:** Adam  
**Função de perda:** MSE (Erro Médio Quadrático)  


O modelo aprende padrões de variação da temperatura e tenta prever o valor seguinte.



## 📈 Resultados Obtidos

Depois do treino o modelo conseguiu realizar previsões. 
Um gráfico foi gerado para mostrar a comparação entre as temperaturas reais e previstas:
🔵 Linha azul: Temperatura real  
🟠 Linha laranja tracejada: Temperatura prevista pelo modelo  

O gráfico demonstra que a rede neural conseguiu aprender o comportamento geral das temperaturas

##  Ferramentas Utilizadas:

**Python**  
**TensorFlow / Keras**  
**Pandas**  
**Matplotlib**  
**Visual Studio Code**



## Como rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Yuran-exe72/previsao_tempo_IA.git

