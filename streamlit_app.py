from matplotlib import widgets
import streamlit as st

import analyse_page
import machine_learning_page

st.title("Willkommen zur AutoScout24 Datenanalyse App!")

st.info("""
Diese App bietet:

- **Datenanzeige:** Sehen Sie die AutoScout24 Daten und filtern Sie nach Bedarf.
- **Diagramme:** Visualisieren Sie Trends und Muster der Autopreise.
- **Preisvorhersage:** Geben Sie Autodaten ein und erhalten Sie eine sofortige Preisprognose.

Viel Spaß bei Ihrer Analyse!
""")

# Definiere die Seiten der App, die verschiedene Aspekte von Streamlit vorstellen
pages = {
    "1. Analyse"   : analyse_page,
    "2. Preisvorhersage"     : machine_learning_page,
}

# Erstelle eine Seitenleiste für die Navigation im Projekt
st.sidebar.title("Navigation")
select = st.sidebar.radio("Gehe zu:", list(pages.keys()))

# Starte die ausgewählte Seite
pages[select].app()
