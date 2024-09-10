import streamlit as st

st.set_page_config(
    page_title='About',
    page_icon=':page_facing_up:',
    layout='wide'
)

st.header('About')
st.write('')
st.write("Dans un contexte où la gestion des contrats clients devient de plus en plus complexe et essentielle pour le bon fonctionnement de la SBIN, le besoin de développer une application interne performante s'est imposé. Cette application web est spécialement conçue pour le suivi rigoureux des contrats des clients ayant souscrit à une offre de fibre optique Celtiis. Elle offre une interface utilisateur intuitive et se compose de trois pages principales. Home pour une vue d'ensemble conviviale pour un accès rapide aux informations clés, Statistiques pour une analyse détaillée des données contractuelles à travers des graphiques interactifs, permettant de visualiser les tendances et d'optimiser la gestion des contrats, et About une section dédiée à la présentation de l'application, ses objectifs, et son importance stratégique pour la SBIN.")
st.write('')

st.subheader('')
st.subheader('Home')
st.write("Cette page présente l'ensemble des clients ayant souscrit à des offres de la fibre Celtiis. Elle permet de filtrer les contrats par année, par mois ou par offres, et de rechercher des contrats par nom ou par numéro de contrat, offrant ainsi une gestion précise et adaptée des informations contractuelles.")
st.write('')
st.image("images\Capture d'écran 2024-08-30 153419.png")

st.subheader('')
st.subheader('')
st.subheader('Statistiques')
st.write("Cette interface présente des graphiques permettant d'observer les zones couvertes par les offres, la progression des offres dans différentes localités, le statut des contrats, ainsi que l'évaluation des agents en fonction du nombre de contrats gérés.")
st.write('')
st.image("images\Capture d'écran 2024-08-30 154446.png")
st.subheader('')
st.image("images\Capture d'écran 2024-09-05 114343.png")