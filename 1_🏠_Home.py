import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
st.write("Bienvenue sur ce site dédié au suivis des contrats clients des abonnés à la fibre celtiis. Vous pouvez depuis ici suivre le status des contrats. Vous pouvez également rechercher des clients en particuliers par leurs noms et prénoms, numéro et effectuer des tris en fonction du contrat client, du mois et de l'année.")
st.write('')

recherche = st.text_input('Search by name or by contract number')
st.subheader("")

#importation des données
df = pd.read_excel(io='data/test_contrat_VF.xlsx')

#Recherche par nom ou par numéro de contrat
 
def recherhce_par_nom_ou_par_numero(nom):
    if nom in df['Nom'].values:
        plage = df[df['Nom'] == nom]
    elif nom in df['Numéro Contrat'].values:
        plage = df[df['Numéro Contrat'] == nom]
    else:
        plage = pd.DataFrame()

    if not plage.empty:
        st.table(plage)
    else:
        st.write("Aucun résultat trouvé pour la recherche.")
        
if recherche:
    recherhce_par_nom_ou_par_numero(recherche)

st.write('')
st.dataframe(df, height=600)

#conversion des dates dans un format permettant d'extraire le mois et l'année
df['Date de début'] = pd.to_datetime(df['Date de début'], format="%d/%m/%Y", errors='coerce')
df['Date de fin'] = pd.to_datetime(df['Date de fin'], format="%d/%m/%Y", errors='coerce')


#Partie des tries
st.sidebar.header("Sort by:")
mois_selectionner = st.sidebar.selectbox('Month', ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 
                            'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre'))
    
st.sidebar.write("")    
annee_selectionner = st.sidebar.selectbox('Year', df['Date de début'].dt.year.unique())
st.sidebar.write("")

st.sidebar.markdown('---')
st.sidebar.write("") 
st.sidebar.header("Sort by:")
offres_selectionner = st.sidebar.selectbox('Offers', ('FTTH', 'Celtiis Business RNIS', 'Celtiis Business Fixe', 'SERVEUR VIRTUEL', 'SOLUTIONS DE COLOCALISATION', 'BUSINESS VPN'))

#Filtrage des données

def tri_par_annee(annee):
    st.write('')
    st.subheader('Sort by year:')
    plage = df[(df['Date de fin'].dt.year == annee)]
    st.table(plage)
    
def tri_par_mois_annee(mois, annee):
    #Conversion des mois en format numérique
    st.write('')
    st.subheader('Sort by month or year:')
    mois_numerique = {
        "Janvier": 1, "Février": 2, "Mars": 3, "Avril": 4,
        "Mai": 5, "Juin": 6, "Juillet": 7, "Août": 8, "Septembre": 9,
        "Octobre": 10, "Novembre": 11, "Décembre": 12
    }[mois]
    plage = df[(df['Date de fin'].dt.year <= annee) & (df['Date de fin'].dt.month <= mois_numerique)]
    st.table(plage)
    
def tri_par_offres(offres):
    st.write('')
    st.subheader('Sort by offer:')
    plage = df[df['Offres'] == offres]
    st.table(plage)
    
def tri_par_mois_annee_offres(mois, annee, offres):
    st.write('')
    st.subheader('Sort by month, year and by offer:')
    mois_numerique = {
        "Janvier": 1, "Février": 2, "Mars": 3, "Avril": 4,
        "Mai": 5, "Juin": 6, "Juillet": 7, "Août": 8, "Septembre": 9,
        "Octobre": 10, "Novembre": 11, "Décembre": 12
    }[mois]
    plage = df[(df['Date de fin'].dt.year <= annee) & (df['Date de fin'].dt.month <= mois_numerique) & (df['Offres'] == offres)]
    st.table(plage)
    
    
#a revoir par vous
if annee_selectionner:
    tri_par_annee(annee_selectionner)
if mois_selectionner and annee_selectionner:
    tri_par_mois_annee(mois_selectionner, annee_selectionner)
if offres_selectionner:
    tri_par_offres(offres_selectionner)
if mois_selectionner and annee_selectionner and offres_selectionner:
    tri_par_mois_annee_offres(mois_selectionner, annee_selectionner, offres_selectionner)
    

