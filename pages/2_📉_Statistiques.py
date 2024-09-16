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
st.write("Vous trouverez ici divers graphiques illustrant le statut des contrats, les types de contrats, le nombre d'employés par direction, ainsi que les contrats en dernière année. Ces visualisations vous permettront de mieux comprendre et analyser les données relatives aux contrats et aux employés.")
st.write("")
st.write('')
st.write('')
st.write('')

#importation du dataset
df = pd.read_excel(io='data/employee_data (3).xlsx')

#statut des contrats
st.sidebar.header('Statistiques par contrat:')
if st.sidebar.button('Statut des contrats'):
    frequence_contrat = df['Statut'].value_counts().reset_index()
    frequence_contrat.columns = ['Statut', 'Nombre']
    
    #diagramme circulaire pour observer le statut des contrats
    couleurs_personnalisees = ['#00e003', '#e04400']
    
    st.subheader('Répartition des contrats par statut')
    fig = px.pie(frequence_contrat, values='Nombre', names='Statut', width=600, height=600, color_discrete_sequence=couleurs_personnalisees)
    st.plotly_chart(fig, use_container_width=True)
    st.write('')

#type de contrat
if st.sidebar.button('Type de contrat'):
    st.subheader('Nombre de contrat par type de contrat')
    frequence_type = df['Type de contrat'].value_counts().reset_index()
    frequence_type.columns = ['Type de contrat', 'Nombre']
    
    fig = px.bar(frequence_type, x='Type de contrat', y='Nombre', template='seaborn', color='Type de contrat', text_auto = '')
    fig.update_traces(textfont_size = 18,  textangle = 0,  textposition = "outside",  cliponaxis = False, width=0.5 )
    fig.update_layout(yaxis_showgrid=False)

    st.plotly_chart(fig, use_container_width=True)
    
st.sidebar.markdown('---')

#contrat par direction
st.sidebar.header('Statistiques par Direction:')
if st.sidebar.button('Nbre Employés par direction'):
    st.subheader("Nombre d'employés par Direction")
    frequence_direction = df['Direction'].value_counts().reset_index()
    frequence_direction.columns = ['Direction', 'Nombre']
    
    fig = px.bar(frequence_direction, x='Direction', y='Nombre', template='seaborn', color='Direction', text_auto = '')
    fig.update_traces(textfont_size = 18,  textangle = 0,  textposition = "outside",  cliponaxis = False, width=0.5 )
    fig.update_layout(yaxis_showgrid=False)

    st.plotly_chart(fig, use_container_width=True)
    
st.sidebar.markdown('---')

#contrats en cours en fonction des années
st.sidebar.header('Statistiques par année:')
if st.sidebar.button('Contrats en dernière années'):
    st.subheader('Nombre de contrat en dernière années')
    df['Date fin période '] = pd.to_datetime(df['Date fin période '], format="%d/%m/%Y", errors='coerce')
    data_annee = df['Date fin période '].dt.year.value_counts().reset_index()
    data_annee.columns = ['Annee', 'Nombre']
    
    fig = px.bar(data_annee, x='Annee', y='Nombre', template='seaborn', color='Annee', text_auto = '')
    fig.update_traces(textfont_size = 18,  textangle = 0,  textposition = "outside",  cliponaxis = False, width=0.5)
    fig.update_layout(yaxis_showgrid=False)

    st.plotly_chart(fig, use_container_width=True)