# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQFwxxM13bxUC0dpyd0w0PxfZIrJ-hp4Px-R6rsTiG3c3n-89JApzA0jYJpU9vNfxeNCvtJ0Cg35KtO/pub?gid=556192647&single=true&output=csv"
db = Ler_GooglePlanilha(url)
db.fillna('', inplace=True)
Escrever(db)

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("CARROS TURBINADOS")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Para amantes de carros")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Amo carros de verdade mesmo")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Texto interessante sobre carros muito interessantes.")

values = st.slider("Select a range of values", 0.0, 100.0, (75.0, 90.0))
st.write("Values:", values)
