# Importando bibliotécas

import pandas as pd
import streamlit as st
import plotly.express as px

# Configuração de Layout da página 
st.set_page_config(layout="wide")

# Abrindo dataset
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# Range para seleção de livros
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

# Slider 
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

# Graficos para análise visualização
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
