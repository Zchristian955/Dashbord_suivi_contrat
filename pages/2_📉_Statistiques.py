import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title='Statistiques',
    page_icon=':bar_chart:',
    layout='wide'
    )

st.header('Statistiques')
st.write("Vous pourrez observer ici des graphiques sur zones géographiques bénéficiant de la meilleure couverture pour les offres proposées, la progression des contrats dans les différentes localités, l'évaluation des agents commerciaux basée sur le volume de contrats qu'ils ont gérés, les contrats les plus sollicités par les clients, et sur les status des contrats en fonctions offres")
st.write('')
st.write('')
st.write('')
st.write('')

#importation du dataset
df = pd.read_excel(io='data/test_contrat_VF.xlsx')
df['Date de début'] = pd.to_datetime(df['Date de début'], format="%d/%m/%Y", errors='coerce')
df['Date de fin'] = pd.to_datetime(df['Date de fin'], format="%d/%m/%Y", errors='coerce')

st.sidebar.header('Statistiques par localité :')
#conversion de la colonne date de début en datetime pour pouvoir extraire l'annee
df['Date de début'] = pd.to_datetime(df['Date de début'])
df['Annee'] = df['Date de début'].dt.year

def progression_contrats(localite):
    st.subheader(f'Progression des contrats au niveau des {localite}')
    souscriptions = df.groupby([localite, 'Annee']).size().unstack(fill_value=0).reset_index()
    for loc in souscriptions[localite].unique():
        donnee_localite = souscriptions[souscriptions[localite] == loc]
        donnee_loc = donnee_localite.melt(id_vars=[localite], var_name='Annee', value_name='Nombre')
        
        fig = px.line(donnee_loc, x='Annee', y='Nombre', color=localite, title=f'Evolution des contrats {loc}')
        fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
        st.plotly_chart(fig, use_container_width=True)  
        st.subheader("")
    
localite = st.sidebar.selectbox('Sélectionner la localité', ('Departement','Commune'))

if st.sidebar.button('Progression des contrats'):
    progression_contrats(localite)
        

#zones géographiques bénéficiant de la meilleure couverture pour les offres proposées
if st.sidebar.button('Zone géographique couvert'):
    frequence_departement = df['Departement'].value_counts().reset_index()
    frequence_departement.columns = ['Departement', 'Nombre']
    
    frequence_commune = df['Commune'].value_counts().reset_index()
    frequence_commune.columns = ['Commune', 'Nombre']

    #diagramme circulaire pour observer la couvertures des offres
    st.subheader('Répartition des offres par département et par commune')
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(frequence_departement, values='Nombre', names='Departement', title='Département')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        fig = px.pie(frequence_commune, values='Nombre', names='Commune', title='Commune')
        st.plotly_chart(fig, use_container_width=True)

st.sidebar.markdown('---')

st.sidebar.header('Statistiques par entreprise:')
#contrats les plus sollicités par les clients
def contrats_sollicités(type_de_clients):
    st.subheader(f'Contrats les plus sollicités chez les {type_de_clients}')
    data = df[df['Type de client'] == type_de_clients]
    frequence_offre = data['Offres'].value_counts().reset_index()
    frequence_offre.columns = ['Offres', 'Nombre']
    
    fig = px.bar(frequence_offre, x='Offres', y='Nombre', template='seaborn', text_auto = '')
    fig.update_traces(textfont_size = 12,  textangle = 0,  textposition = "outside",  cliponaxis = False )

    st.plotly_chart(fig, use_container_width=True)

type_de_clients = st.sidebar.selectbox('Sélectionner le type de client', ('ETAT', 'Entreprise'))
    
if st.sidebar.button('Contrats récurrents'):
    contrats_sollicités(type_de_clients) 
    
st.sidebar.markdown('---')

        
#status des contrats en fonctions offres
if st.sidebar.button('Status des Offres'):
    etat = df.groupby(['Offres','Status']).size().unstack(fill_value=0).reset_index()
    
    status = df['Status'].unique()
    status.sort()
    
    for statu in status:
        etat_status = etat[['Offres', statu]].rename(columns={statu: 'Nombre'})
        fig = px.bar(etat_status, x='Offres', y='Nombre',color='Offres', text_auto = '', title=f"Offres {statu}")
        fig.update_traces(textfont_size = 12,  textangle = 0,  textposition = "outside",  cliponaxis = False ) 
        st.plotly_chart(fig, use_container_width=True)
        st.subheader('')


#Évaluation des agents commerciaux basée sur le volume de contrats qu'ils ont gérés
if st.sidebar.button('Evaluation des agents'):
    st.subheader('Evaluation des agents')
    frequence_agents = df['Agent SBIN(Responsable contrat)'].value_counts().reset_index()
    frequence_agents.columns = ['Agents', 'Nombre']
    fig = px.bar(frequence_agents, x='Agents', y='Nombre', template='seaborn', text_auto = '',)
    fig.update_traces(textfont_size = 12,  textangle = 0,  textposition = "outside",  cliponaxis = False )
    st.plotly_chart(fig, use_container_width=True)
    
