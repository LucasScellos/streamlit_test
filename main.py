import streamlit as st

# Titre de l'application
st.title("Ma première application Streamlit")

# Ajouter du texte
st.write("Voici quelques éléments de base pour commencer avec Streamlit.")

# Ajouter un graphique
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot(plt)

# Ajouter un widget interactif
option = st.selectbox(
    'Choisissez une option',
    ['Option 1', 'Option 2', 'Option 3']
)

'Vous avez choisi:', option

# Afficher des données dynamiques
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)

# Afficher une image


# Ajouter une carte
st.map()

# Afficher des données en colonnes
col1, col2 = st.columns(2)
with col1:
    st.header("Colonne 1")
    st.write("Contenu de la colonne 1")

with col2:
    st.header("Colonne 2")
    st.write("Contenu de la colonne 2")
