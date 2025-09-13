# Análise de Séries Temporais Climáticas em Brasília

Este é um projeto da faculdade Cruzeiro do Sul Virtual, onde permitiu utilizar qualquer base real de preferência. Deste modo, este dataset contém informações diárias de qualidade do ar para Brasília, coletadas durante todo o ano de 2024, a partir do Banco de Dados Meteorológicos para Ensino e Pesquisa (BDMEP) do INMET. Os dados incluem variáveis como concentração de poluentes atmosféricos, temperatura, umidade, precipitação e outros parâmetros meteorológicos relevantes para análise ambiental e estudos de poluição do ar.

**Objetivos:**

- Coleta e exploração dos dados.
- Tratamento de valores ausentes e engenharia de features.
- Análise exploratória dos dados
- Treinamento de diferentes algoritmos de classificação.
- Avaliação e comparação de métricas (F1-Score, Precision, Recall, AUC).

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


Aqui está uma sugestão para finalizar o README do seu repositório, com uma seção de "Considerações Finais" e "Como usar", que traz clareza para quem acessar o projeto:

***

## Considerações Finais

Este projeto demonstra como técnicas de Machine Learning podem ser aplicadas para previsão climática em Brasília, com foco na classificação de eventos de chuva usando dados reais e temporais. O uso do XGBoost se destacou por sua alta capacidade preditiva e equilíbrio entre sensibilidade e precisão, aspectos fundamentais para aplicações meteorológicas.

Além da modelagem, o projeto também proporciona insights relevantes sobre as variáveis climáticas que mais impactam a previsão.

Este trabalho reflete um passo importante para a integração de dados abertos e métodos avançados visando o monitoramento ambiental e apoio a políticas públicas.

***

## Como usar este repositório

1. Clone o repositório:
   ```bash
   git clone https://github.com/Mustasheep/brasilia-weather-forecasting.git
   cd brasilia-weather-forecasting
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute os notebooks na ordem:
   - `01_process_data.ipynb`: para limpeza e engenharia de features
   - `02_eda.ipynb`: para análise exploratória 
   - `03_trai_data.ipynb`: para treinamento dos modelos

4. Explore os resultados e métricas apresentadas para entender o desempenho dos modelos.

***

## Contato

Para dúvidas, sugestões ou colaborações, entre em contato!

  <p align="left">
  <a href="https://www.linkedin.com/in/thiago-mustasheep"><img width="32px" alt="LinkedIn" title="LinkedIn" src="https://img.icons8.com/?size=100&id=lMUZwFHycz7a&format=png&color=000000"/></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;
  <a href="mailto:thiagoassis.scientist@gmail.com" width="32px" alt="Gmail" title="Email"><img width="32px" src="https://img.icons8.com/?size=100&id=48165&format=png&color=000000"/></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;
</p>

***
