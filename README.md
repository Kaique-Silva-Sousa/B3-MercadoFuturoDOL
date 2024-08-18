# Resumo do Código para Coleta de Dados de Mercado Futuro do Dólar

Este código realiza a coleta de dados de ações de contratos futuros de dólar na bolsa de valores "B3" usando web scraping e salvando em um arquivo Excel. A seguir, está uma visão geral das principais etapas e funções do código:

## 1. Importação de Bibliotecas

- **numpy**: Para operações numéricas e manipulação de arrays.
- **pandas**: Para manipulação e análise de dados em formato tabular.
- **selenium**: Para automação de navegação na web e extração de dados.
- **datetime**: Para manipulação de datas e horários.

## 2. Configuração do Navegador

- **Configuração do Selenium**: Configura o navegador Chrome para operar no modo headless (sem interface gráfica).

## 3. Função `getDados`

- **Objetivo**: Coleta dados de preços futuros do dólar para os últimos 30 dias.

  1. **Navegação para o Site da B3**: Acessa o site da bolsa de valores para coletar dados.
  2. **Loop pelas Datas**: Para cada uma das últimas 30 datas, realiza:
     - Seleção da data no formulário.
     - Escolha do ativo "Dólar Comercial".
     - Coleta de dados de vencimentos e preços.
  3. **Tratamento de Erros**: Em caso de falha ao coletar dados, insere valores nulos e reinicia a página.
  4. **Criação de DataFrames**: Constrói DataFrames para vencimentos, preços e datas.
  5. **Mesclagem e Limpeza de Dados**: Mescla os DataFrames e limpa os dados.
  6. **Conversão e Salvamento**: Converte os valores para formato numérico e salva o resultado em um arquivo Excel.

# Comandos `pip` para Instalação de Bibliotecas

Para instalar as bibliotecas usadas no código, você pode usar os seguintes comandos `pip`:

```bash
pip install numpy
pip install pandas
pip install selenium
```

Este código é útil para análise de tendências e padrões nos preços futuros do dólar, ajudando investidores e analistas a tomar decisões informadas com base em dados históricos.
