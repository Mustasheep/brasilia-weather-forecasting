⚠️ Projeto em andamento...

# Análise de Séries Temporais Climáticas em Brasília

Este é um projeto da faculdade Cruzeiro do Sul Virtual, onde permitiu utilizar qualquer base real de preferência. Deste modo, este dataset contém informações diárias de qualidade do ar para Brasília, coletadas durante todo o ano de 2024, a partir do Banco de Dados Meteorológicos para Ensino e Pesquisa (BDMEP) do INMET. Os dados incluem variáveis como concentração de poluentes atmosféricos, temperatura, umidade, precipitação e outros parâmetros meteorológicos relevantes para análise ambiental e estudos de poluição do ar.

O objetivo deste conjunto de dados é permitir análises temporais, modelagem preditiva e estudos comparativos de qualidade do ar em Brasília ao longo do ano de 2024.

**Objetivos:**

- Coleta e exploração dos dados.
- Tratamento de valores ausentes e engenharia de features.
- Análise exploratória dos dados
- Treinamento de diferentes algoritmos de regressão.
- Avaliação e comparação de métricas (MAE, RMSE, R²).
- Construção de pipeline em Azure ML para simulação de implantação como serviço preditivo.

# Estrutura do Projeto

```
brasilia-weather-forecasting/
├── data/
│   ├── INMET_CO_DF_A001_BRASILIA_01-01-2024_A_31-12-2024.csv     # Dados obtidos do INMET
│   └── INMET_DF_processado.csv                                   # Dados limpos e processados
├── notebooks/          
│   ├── 01_process_data.ipynb           # limpeza e engenharia de features
│   └── 02_eda.ipynb                    # análise exploratória dos dados
├── .gitignore                          # impede upload de arquivos locais ao git
├── LICENSE                             # Licença do MIT
├── requirements.txt                    # documento para instalar as bibliotecas
└── README.md
```


