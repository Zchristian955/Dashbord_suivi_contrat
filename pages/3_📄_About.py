import streamlit as st

st.set_page_config(
    page_title='About',
    page_icon=':page_facing_up:',
    layout='wide'
)

st.header('About')
st.write('')
st.write("Pour assurer une gestion optimale des contrats des employés de la SBIN, il est essentiel de disposer d'un outil permettant une vue d'ensemble claire et précise. Cette application web a été spécifiquement conçue pour répondre à ce besoin. Elle offre une interface utilisateur intuitive et se compose de trois pages principales : Home, pour une vue d'ensemble conviviale et un accès rapide aux informations clés ; Statistiques, pour une analyse détaillée des données contractuelles à travers des graphiques interactifs, permettant de visualiser les tendances et d'optimiser la gestion des contrats ; et About, une section dédiée à la présentation de l'application, de ses objectifs, et de son importance stratégique pour la SBIN. Cet outil est conçu pour faciliter une gestion efficace et éclairée des contrats des employés.")
st.write('')

st.subheader('')
st.subheader('Home')
st.write("Cette page offre une vue complète de l'ensemble des employés de la SBIN, en détaillant leur direction, la durée de leur contrat, ainsi que le type de contrat associé. Elle permet de filtrer les contrats par statut et de rechercher des contrats par nom ou prénom, facilitant ainsi une gestion précise et personnalisée des informations contractuelles. Grâce à ces fonctionnalités, vous pouvez accéder rapidement aux données pertinentes et gérer efficacement les contrats en fonction de vos besoins spécifiques.")
st.write('')
st.image("images\Capture d'écran 2024-09-16 153821.png")

st.subheader('')
st.subheader('')
st.subheader('Statistiques')
st.write("Cette interface propose une série de graphiques interactifs qui permettent de visualiser divers aspects des contrats. Vous pouvez observer le statut des contrats, les types de contrats, ainsi que le nombre d'employés pour chaque type de contrat. Elle offre également des visualisations détaillées du nombre d'employés par direction et des contrats arrivant à leur échéance. Ces graphiques fournissent une vue d'ensemble claire et approfondie des données contractuelles, facilitant ainsi une gestion stratégique et informée.")
st.write('')
st.image("images\Capture d'écran 2024-09-16 153858.png")
st.subheader('')
st.image("images\Capture d'écran 2024-09-16 153915.png")