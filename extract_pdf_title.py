import streamlit as st
import pdfplumber

st.set_page_config(page_title="Extraction de Titre PDF", layout="centered")
st.title("📰 Application Web - Extraction de Titre PDF")

st.markdown("""
Cette application vous permet d'extraire automatiquement le **titre** de la première page d’un fichier PDF.  
Le titre est détecté en analysant le texte ayant la **plus grande taille de police**.
""")

uploaded_file = st.file_uploader("📎 Choisissez un fichier PDF", type="pdf")

if uploaded_file:
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            page = pdf.pages[0]
            elements = page.extract_words(extra_attrs=["size"])

            if elements:
                # Trier les mots par taille de police décroissante
                titre = sorted(elements, key=lambda x: -x['size'])[0]['text']
                st.success(f"**Titre extrait :** {titre}")
            else:
                st.warning("Aucun texte détecté sur la première page.")

            with st.expander("📄 Voir le texte complet de la première page"):
                texte_complet = page.extract_text()
                st.text(texte_complet if texte_complet else "Aucun texte disponible.")
    except Exception as e:
        st.error(f"Erreur lors de l'analyse du PDF : {e}")
else:
    st.info("Veuillez importer un fichier PDF pour commencer.")
