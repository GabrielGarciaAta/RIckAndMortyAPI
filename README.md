# 🧪 Rick and Morty - End-to-End Data Pipeline & Explorer

Este é um projeto de Engenharia de Dados que demonstra a construção de um pipeline ETL (Extraction, Transformation, Load) de ponta a ponta. O ecossistema consome dados da API pública do Rick and Morty, realiza o tratamento e achatamento de dados brutos, armazena as informações em arquivos de alta performance (Apache Parquet), persiste em um banco de dados relacional indexado (SQLite) e entrega um produto de dados visual e interativo para o usuário final através de uma aplicação web.


## 🏗️ Arquitetura e Fluxo do Pipeline

O pipeline foi projetado utilizando o conceito de separação de responsabilidades e camadas de processamento de dados (inspirado na arquitetura medalhão):

1. **Extração (API ➡️ Bronze):** Consumo automatizado e resiliente via paginação de todos os 826 personagens da API oficial, respeitando os limites do servidor com controle de requisições (`time.sleep`).
2. **Transformação (Pandas ➡️ Silver):** Processamento de dados via Pandas para o achatamento (*json_normalize*) de objetos aninhados, seleção de atributos essenciais para o negócio, limpeza e renomeação de colunas para um padrão homogêneo.
3. **Armazenamento Otimizado (Data Lake ➡️ Parquet):** Persistência dos dados higienizados no formato colunar *Apache Parquet* utilizando compressão *Snappy*, reduzindo o custo de armazenamento e acelerando queries analíticas.
4. **Data Warehouse / Consumo (SQL ➡️ Gold):** Carga incremental/substitutiva das entidades tratadas diretamente em uma tabela estruturada dentro de um banco de dados relacional SQLite.
5. **Camada de Entrega (Streamlit App):** Dashboard web focado na experiência do usuário, que realiza consultas analíticas na memória via cache otimizado (`@st.cache_data`) e paginação inteligente de elementos para evitar sobrecarga no navegador.

---

## 📂 Estrutura de Pastas do Repositório

```text
rick-morty-pipeline/
├── data/                       # Camada de Armazenamento (Data Lake & DB)
│   ├── todos_personagens_rick_morty.csv
│   ├── todos_personagens.parquet
│   └── rick_and_morty.db       # Arquivo físico do Banco SQL Relacional
├── notebooks/                  # Desenvolvimento Modular no Jupyter
│   ├── 01_extracao_api.ipynb   # Pipeline de ingestão, limpeza e escrita em arquivos
│   └── 02_carga_sql.ipynb      # Carga analítica para o banco de dados
├── app.py                      # Código-fonte do produto web (Streamlit)
├── .gitignore                  # Arquivo de bloqueio de arquivos temporários e caches
└── README.md                   # Documentação técnica do projeto

```

## ⚡ Análise de Performance: CSV vs Apache Parquet

Como parte das boas práticas de Engenharia de Big Data, foi implementada a conversão dos dados de texto puro (CSV) para o formato binário colunar (Parquet). Mesmo em um ecossistema controlado de 826 registros, a diferença de eficiência é evidente:

* Tamanho do CSV: ~125 KB (Armazenado em linhas, texto plano)

* Tamanho do Parquet: ~43 KB (Armazenado em colunas, compressão Snappy)

* Taxa de Compressão: Redução de aproximadamente 65% no uso de disco.

Em cenários reais de produção com volumes na escala de Terabytes, essa otimização representa milhares de dólares economizados em armazenamento em nuvem (AWS/GCP) e processamento de queries distribuídas.

### 🛠️ Tecnologias Utilizadas

* Python 3.11+ (Linguagem core do pipeline)

* Pandas: Engenharia de atributos, limpeza e estruturação de DataFrames

* PyArrow & Snappy: Mecanismos de codificação, compressão e tipagem para arquivos Parquet

* SQLite3: Motor de banco de dados relacional para processamento de queries estruturadas

* Streamlit: Framework para prototipagem rápida e entrega de aplicações web de dados

* Requests / JSON: Consumo e desserialização de payloads de APIs RESTful



## 🚀 Como Executar este Projeto Localmente

1. Clonar o repositório:
    ```cmd 
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```
2. Configurar o Ambiente Virtual 
    ```cmd
    pip install pandas pyarrow fastparquet streamlit
    ```

3. Execute o pipeline de dados
    1. Abra e execute o notebook notebooks/01_extracao_api.ipynb para coletar os dados da API e gerar as bases em /data.

    2. Execute o notebook notebooks/02_carga_sql.ipynb para consumir o arquivo Parquet e criar a tabela indexada no banco de dados SQLite.

4. Iniciar a aplicação web (Na raiz do projeto inicie o servidor)
    ```cmd 
    python -m streamlit run app.py
    ```

## 👨‍💻 Sobre o Autor

Atualmente sou estudante de **Ciência da Computação na UFMS (Campo Grande)**, trazendo comigo a base técnica desenvolvida durante meu período de **Engenharia de Computação na sUSP São Carlos**. 

Este projeto faz parte dos meus estudos focados em **Engenharia de Dados**, onde busco aplicar conceitos de computação em problemas reais de pipeline de dados.

**Curiosidade:** Este código foi escrito entre aulas e sessões de treino, movido a muito **Tereré com limão** 🧉🍋.

![UFMS](https://img.shields.io/badge/UFMS-CC-blue)
![USP](https://img.shields.io/badge/USP-EC-orange)
![Local](https://img.shields.io/badge/Local-Campo%20Grande--MS-green)
