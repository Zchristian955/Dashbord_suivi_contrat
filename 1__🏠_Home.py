import streamlit as st
import numpy as np
import pandas as pd
import smtplib as s
import os
from datetime import datetime
from email.mime.text import MIMEText

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
st.write("Bienvenue sur ce site dédié au suivi des contrats des employés de la SBIN. À partir de cette plateforme, vous pouvez facilement suivre l'état des contrats en cours, passés, ou expirés. Vous avez également la possibilité de rechercher des employés par nom ou prénom et de trier les contrats en fonction de leur statut. Profitez de ces fonctionnalités pour une gestion optimisée et simplifiée des contrats.")
st.write("")
st.write('')

recherche = st.text_input('Veuillez saisir le nom ou le prénom et appuyez sur entrer')
st.subheader("")

#importation des données
df = pd.read_excel(io='data/employee_data (3).xlsx')

#Recherche par nom ou par prénom
 
def recherhce_par_nom_ou_par_prénom(nom):
    if nom in df['Nom'].values:
        plage = df[df['Nom'] == nom]
    elif nom in df['Prenom'].values:
        plage = df[df['Prenom'] == nom]
    else:
        plage = pd.DataFrame()

    if not plage.empty:
        st.table(plage)
    else:
        st.write("Aucun résultat trouvé pour la recherche.")
        
if recherche:
    recherhce_par_nom_ou_par_prénom(recherche)
    
#selectbox pour le statut des contrats
st.sidebar.header("Sort by contract statut:")
statut_en_cours = st.sidebar.button('En cours')
statut_cloture = st.sidebar.button('Cloturé')

st.sidebar.write("")

st.sidebar.markdown('---')

def tri_par_statut_en_cours():
    st.write('')
    st.subheader('Sort by:')
    plage = df[(df['Statut'])== 'En cours']
    st.table(plage)
    
def tri_par_statut_cloturé():
    st.write('')
    st.subheader('Sort by:')
    plage = df[(df['Statut'])== 'Cloturé']
    st.table(plage)
    
    
if statut_en_cours:
    tri_par_statut_en_cours()
elif statut_cloture:
    tri_par_statut_cloturé()
    
#affichage de la database
st.write('')
st.dataframe(df, height=600, width=1500)
    
#trie des contrats venant à terme
contrats_exp = df[(df['Échéance'] == "< 45 jours") | (df['Échéance'] == "< 30 jours") | (df['Échéance'] == "< 15 jours")]

def notification(plage):
    email = "barondegbey2004@gmail.com"
    
    nom_mail = plage.groupby(['Nom', 'Date fin période ', 'Adresse mail', 'Fonction']).size().reset_index(name='count')
    adresse_trier = nom_mail[['Nom', 'Adresse mail', 'Date fin période ', 'Fonction']].drop_duplicates()
    
    for mail in adresse_trier['Adresse mail'].unique():
        df_adresse = adresse_trier[adresse_trier['Adresse mail'] == mail]
        
        for index, ligne in df_adresse.iterrows():          
            text = f"Bonjour {ligne['Nom']}\n\nVotre contrat en tant que {ligne['Fonction']} à la SBIN expire le {ligne['Date fin période ']}\n\nCordialement"
            
            msg = MIMEText(text, 'plain', 'utf-8')
            msg['Subject'] = "Notification d'expiration de contrat"
            msg['From'] = email
            msg['To'] = mail

            server = s.SMTP("smtp.gmail.com", 587)
            server.starttls()

            password = "faou ciga evsr ooov"
            if not password:
                raise ValueError("Le mot de passe de l'application Gmail n'est pas défini. Veuillez vérifier la variable d'environnement GMAIL_APP_PASSWORD.")


            server.login(email, password)
            server.sendmail(email, mail, msg.as_string())
            print(f"email has been sent to {mail}")
            server.quit()
notification(contrats_exp)