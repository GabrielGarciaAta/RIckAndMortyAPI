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

busca_nome = st.text_input("Pesquisar por nome(ex: Rick, Morty, Summer):")

# Lógica de consulta no SQL
def carregar_dados():

    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_banco = os.path.join(caminho_atual, 'data', 'rick_and_morty.db')

    # Acesso ao banco de dados
    conn = sqlite3.connect(caminho_banco)

    # Query base 
    query = "SELECT * FROM characters WHERE 1=1"

    # Filtros dinâmicos
    if busca_nome:
        query += f" AND name LIKE '%{busca_nome}%'"
    if status != "Todos":
        query += f" AND status = '{status}'"
    if genero != "Todos":
        query += f" AND genero = '{genero}'"

    df = pd.read_sql(query,conn)
    conn.close()
    return df

df_filtrado = carregar_dados()

st.write(f"Encontrados {len(df_filtrado)} personagens com os filtros aplicados:")

# Exibição dos dados
cols = st.columns(4) 

for i, row in df_filtrado.iterrows():
    with cols[i % 4]:
        st.image(row['url_foto'], use_column_width=True)
        st.subheader(row['nome'])
        st.write(f"🧬 **Espécie:** {row['especie']}")
        st.write(f"📍 **Origem:** {row['origem']}")
        emoji = "🟢" if row['status'] == 'Alive' else "🔴" if row['status'] == 'Dead' else "⚪"
        st.write(f"{emoji} **Status:** {row['status']}")
        st.divider()




















