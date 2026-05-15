import streamlit as st
import pandas as pd
import sqlite3
import os 

# Configuração do site 
st.set_page_config(page_title="Rick And Morty Data Hub", layout="wide", page_icon="🧪")

st.title("🧪 Rick And Morty - Explorer Interativo")
st.markdown("Interface moderna alimentada por um pipeline de Engenharia de Dados e Banco SQL.")
st.divider()

# Busca por status e gênero
st.sidebar.header("🔍 Filtros de Pesquisa")
status = st.sidebar.selectbox("Status de Vida:", ["Todos", "Alive", "Dead", "unknown"])
genero = st.sidebar.selectbox("Gênero:", ["Todos", "Male", "Female", "unknown", "Genderless"])

# Otimização de Performance
limite_exibicao = st.sidebar.slider("Quantidade de cards exibidos:", 8, 100, 24)

busca_nome = st.text_input("Pesquisar por nome(ex: Rick, Morty, Summer):")

# Lógica de consulta no SQL
# stcache faz o app carregar o banco só uma vez
@st.cache_data
def carregar_dados_do_banco():
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_banco = os.path.join(caminho_atual, 'data', 'rick_and_morty.db')

    # Acesso ao banco de dados
    conn = sqlite3.connect(caminho_banco)

    # Query base 
    query = "SELECT * FROM personagens"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df_completo = carregar_dados_do_banco()
df_filtrado = df_completo.copy()

# Filtros dinâmicos
if busca_nome:
    df_filtrado = df_filtrado[df_filtrado['nome'].str.contains(busca_nome, case=False, na=False)]
if status != "Todos":
    df_filtrado = df_filtrado[df_filtrado['status'] == status]
if genero != "Todos":
    df_filtrado = df_filtrado[df_filtrado['genero'] == genero]

total_encontrados = len(df_filtrado)
st.write(f"Encontrados {total_encontrados} personagens. Mostrando os primeiros{min(limite_exibicao, total_encontrados)}:")

# Corta o DataFrame para apenas a quantidade limite
df_exibicao = df_filtrado.head(limite_exibicao)

# Exibição dos dados
cols = st.columns(4) 

for i, row in df_exibicao.reset_index(drop=True).iterrows():
    with cols[i % 4]:
        st.image(row['url_foto'], use_container_width=True)
        st.subheader(row['nome'])
        st.write(f"🧬 **Espécie:** {row['especie']}")
        st.write(f"📍 **Origem:** {row['origem']}")
        
        emoji = "🟢" if row['status'] == 'Alive' else "🔴" if row['status'] == 'Dead' else "⚪"
        st.write(f"{emoji} **Status:** {row['status']}")
        st.divider()




















