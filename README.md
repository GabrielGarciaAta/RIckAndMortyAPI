# ETL Pipeline: Rick and Morty API 🚀

Este projeto faz parte da minha jornada de estudos em **Engenharia de Dados**. O objetivo é construir um pipeline de dados completo (ETL), desde o consumo de uma API externa até o armazenamento otimizado para análise.

## 📌 Status do Projeto: Versão 1.0 (MVP)

Nesta primeira etapa, o foco foi dominar a manipulação de arquivos **JSON** complexos e aninhados utilizando Python e Pandas.

### 🛠️ Tecnologias Utilizadas
*   **Linguagem:** Python 3.10+
*   **Bibliotecas:** 
    *   `Pandas`: Manipulação e tratamento de dados.
    *   `Requests`: Consumo da API REST.
    *   `JSON`: Formatação e visualização da estrutura bruta.
*   **Ambiente:** Jupyter Notebook (Anaconda)

---

## 🧬 O Processo ETL (Extract, Transform, Load)

### 1. Extração (Extract)
Utilizei a biblioteca `requests` para conectar à [Rick and Morty API](https://rickandmortyapi.com/). Nesta fase, capturei os dados brutos da primeira página de personagens, lidando com a estrutura de dicionários e listas do JSON.

### 2. Transformação (Transform)
Esta foi a fase mais crítica, onde apliquei:
*   **Data Flattening:** Uso do `pd.json_normalize()` para transformar objetos aninhados (como `origin` e `location`) em colunas separadas.
*   **Data Cleaning:** Seleção das colunas essenciais para análise e renomeação para o português, garantindo uma tabela limpa e legível.

### 3. Carga (Load)
O resultado final foi exportado para o formato **CSV**, gerando uma tabela pronta para ser utilizada em ferramentas de BI ou bancos de dados SQL.

---

## 📈 Próximos Passos
- [ ] Implementar um loop de paginação para capturar todos os 800+ personagens da série.
- [ ] Otimizar o armazenamento utilizando o formato **Apache Parquet**.
- [ ] Integrar os dados tratados em um banco de dados SQL.

## 👨‍💻 Sobre o Autor

Atualmente sou estudante de **Ciência da Computação na UFMS (Campo Grande)**, trazendo comigo a base técnica desenvolvida durante meu período de Engenharia de Computação na **USP São Carlos**. 

Este projeto faz parte dos meus estudos focados em **Engenharia de Dados**, onde busco aplicar conceitos de computação em problemas reais de pipeline de dados.

**Curiosidade:** Este código foi escrito entre aulas e sessões de treino, movido a muito **Tereré com limão** 🧉🍋.

![UFMS](https://img.shields.io/badge/UFMS-CC-blue)
![USP](https://img.shields.io/badge/USP-EC-orange)
![Local](https://img.shields.io/badge/Local-Campo%20Grande--MS-green)
