import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title='Home',
    page_icon=':house:',
    layout='wide'
    )

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
"""

#Présentation de l'application
st.header("Dashboard")
st.write("")
st.write('')

recherche = st.text_input('Search by name')
st.subheader("")

#importation des données
df = pd.read_excel(io='data/employee_data (3).xlsx')

#affichage de la database
st.write('')
st.dataframe(df, height=600, width=1500)

#selectbox pour les types de contrats
st.sidebar.header("Sort by:")
type_de_contrat = st.sidebar.selectbox('Contract type', df['Type de contrat'].unique())

st.sidebar.write("")

st.sidebar.markdown('---')

#filtrage par type de contrat
def tri_contrat(contrat):
    st.write('')
    st.subheader('Sort by contract:')
    plage = df[(df['Type de contrat'] == contrat)]
    st.table(plage)
    
if type_de_contrat:
    tri_contrat(type_de_contrat)