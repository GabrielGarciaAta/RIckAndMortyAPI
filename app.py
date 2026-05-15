import streamlit as st
import pandas as pd
import sqlite3

# Configuração do site 
st.set_page_config(page_title="Rick And Morty Data Hub", layout="wide", pagee_icon="🧪")

st.title("🧪 Rick And Morty - Explorer Interativo")
st.markdown("Interface moderna alimentada por um pipeline de Engenharia de Dados e Banco SQL.")
st.divider()

# Busca por status e gênero
st.sidebar.header("🔍 Filtros de Pesquisa")
status = st.sidebar.selectbox("Status de Vida:", ["Todos", "Alive", "Dead", "unknown"])
genero = st.sidebar.selectbox("Gênero:", ["Todos", "Male", "Female", "unknown", "Genderless"])

busca_nome = st.text_input("Pesquisar por nome(ex: Rick, Morty, Summer):")
