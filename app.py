import streamlit as st
from PIL import Image
import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="E-Portfolio - Camille Franceschin",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Sidebar
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Aller à la section :",
    ["🏠 Accueil", "👤 Présentation générale", "💪 Compétences", "🚀 Réalisations", "📞 Contacts et liens", "🚆 RATP"]
)

# Fonction pour créer un bouton de téléchargement
def create_download_button(file_path, file_name, button_text):
    try:
        with open(file_path, "rb") as file:
            btn = st.download_button(
                label=button_text,
                data=file,
                file_name=file_name,
                mime="application/pdf"
            )
        return btn
    except FileNotFoundError:
        st.warning("Fichier non trouvé. Assurez-vous que le CV est dans le bon répertoire.")
        return None

# Section Accueil
if section == "🏠 Accueil":
    st.markdown("<h1 class='main-header'>🎓 Bienvenue sur mon E-Portfolio</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; font-size: 1.2em; line-height: 1.6; background-color: #f8f9fa; padding: 2rem; border-radius: 15px; margin: 2rem 0;'>
            <strong>Je suis Camille Franceschin</strong>, étudiante en Sciences des Données, 
            en d'autres mots : tout ce qui touche aux <strong>statistiques</strong>, à l'<strong>informatique</strong> et la <strong>data</strong>. 
            <br><br>
            Cet E-Portfolio est aussi bien un projet d'étude, qu'un élément permettant de mettre en avant mes savoirs et compétences.
        </div>
        """, unsafe_allow_html=True)

# Section Présentation générale
elif section == "👤 Présentation générale":
    st.markdown("<h2 class='section-header'>👤 Présentation générale</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("Z:/BUT3/E-portfolio_Camille_Franceschin/E-portfolio/Images/photo.jpg", width=300)
    
    with col2:
        st.markdown("""
        Je m'appelle **Camille Franceschin**, j'ai actuellement **23 ans** et je suis étudiante 
        (et alternante !) en deuxième année de **BUT Science des Données**.
        
        Je suis originaire de la région **Île-de-France** et ai toujours suivi mes études à Paris. 
        On peut se demander pourquoi à 23 ans je ne suis qu'en deuxième année, il s'avère que, 
        suite à une erreur de parcours, j'ai d'abord tenté de faire des études en histoire-géographie. 
        
        Ces études de géographie m'ont donné goût aux **statistiques** et c'est vers celles-ci 
        que j'ai décidé de me tourner lors de ma réorientation.
        """)
    
    # Parcours scolaire
    st.markdown("<h3 class='subsection-header'>🎓 Parcours scolaire</h3>", unsafe_allow_html=True)
    
    parcours = [
        {
            "formation": "BUT2 Science des Données, IUT Paris Rives de Seine",
            "periode": "Depuis septembre 2023 (diplômée en septembre 2026)",
            "details": "Parcours VCOD (Visualisation, Conception d'Outils Décisionnels), Alternance (2e et 3e année) chez INTERSPORT"
        },
        {
            "formation": "Bi-licence Histoire-Géographie, Université Paris Cité",
            "periode": "Septembre 2020 à Juillet 2023",
            "details": "Première année validée puis redoublement deuxième année et réorientation"
        },
        {
            "formation": "Bac ES, Lycée Nikola Tesla",
            "periode": "Septembre 2017 à Juin 2020",
            "details": "Mention Assez Bien, spécialité mathématiques"
        }
    ]
    
    for p in parcours:
        with st.container():
            st.markdown(f"""
            <div class='skill-box'>
                <h4 style='color: #2E86AB; margin-bottom: 0.5rem;'>{p['formation']}</h4>
                <p style='margin-bottom: 0.5rem;'><strong>Période :</strong> {p['periode']}</p>
                <p style='margin-bottom: 0;'><strong>Détails :</strong> {p['details']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Passions et centres d'intérêt
    st.markdown("<h3 class='subsection-header'>❤️ Passions, centres d'intérêt</h3>", unsafe_allow_html=True)
    
    passion_tab = st.tabs(["✈️ Voyages", "🏛️ Paris et son histoire", "📚 Lecture"])
    
    with passion_tab[0]:
        st.markdown("""
        **Les voyages :** J'aime beaucoup voyager que ce soit avec ma famille ou mes amis, 
        dès que j'ai l'occasion de partir, je prends mes billets, ma valise et je m'envole à travers l'Europe. 
        Que ce soit la plage ou la ville, j'aime être dépaysée et découvrir de nouveaux endroits.
        """)
        st.image("Z:/BUT3/E-portfolio_Camille_Franceschin/E-portfolio/Images/Voyage.png", width=300)
    
    with passion_tab[1]:
        st.markdown("""
        **Paris et son histoire :** Malgré le fait que j'aime quitter la région parisienne et être dépaysée, 
        mon endroit favori reste Paris. J'adore m'y balader, faire des musées, voir les monuments, manger... 
        Même si j'ai délaissé mes études d'histoire, je reste tout de même intéressée et ai de l'intérêt 
        pour cette ville remplie d'histoire.
        """)
        st.image("Z:/BUT3/E-portfolio_Camille_Franceschin/E-portfolio/Images/Paris.png", width=300)
    
    with passion_tab[2]:
        st.markdown("""
        **Lecture :** Même si Paris reste ma ville de cœur, ce que j'apprécie moins sont les transports... 
        Je passe donc mon temps à y lire des livres de tout genre. En passant par des auteurs classiques, 
        puis des auteurs populaires du moment, ou alors des biographies, je me passionne pour la lecture 
        et peux lire plusieurs heures par jour.
        """)
        st.image("Z:/BUT3/E-portfolio_Camille_Franceschin/E-portfolio/Images/livres.png", width=300)

# Section Compétences
elif section == "💪 Compétences":
    st.markdown("<h2 class='section-header'>💪 Compétences</h2>", unsafe_allow_html=True)
    
    # Compétences personnelles
    st.markdown("<h3 class='subsection-header'>🌟 Compétences Personnelles</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        traits = ["Rigoureuse", "Ponctuelle", "Sérieuse", "Investie et passionnée", "Adaptable"]
        traits_html = "".join([f"<span class='personal-trait'>{trait}</span> " for trait in traits])
        st.markdown(traits_html, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='skill-box'>
            <p>Depuis que j'ai l'âge de 16 ans je travaille, et ai pu acquérir ces compétences grâce à cela. 
            J'ai su m'adapter à tout ce que l'on me demandait et je l'ai fait de manière sérieuse.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Compétences techniques
    st.markdown("<h3 class='subsection-header'>🔧 Statistiques et Informatique</h3>", unsafe_allow_html=True)
    
    st.markdown("Grâce à mes études en Science des Données, j'ai pu acquérir de nombreuses compétences que ce soit en Statistiques ou en Informatique.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='project-card'>
            <h4 style='color: #2E86AB;'>📊 Statistiques</h4>
            <ul>
                <li>Maîtrise d'outils d'analyse</li>
                <li>Utilisation des méthodes de modélisation</li>
                <li>Interprétation des données</li>
                <li>Mise en forme des résultats</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='project-card'>
            <h4 style='color: #A23B72;'>💻 Informatique décisionnelle</h4>
            <ul>
                <li>Requêtage de base de données</li>
                <li>Stockage des données</li>
                <li>Langages de programmation</li>
                <li>Algorithmes pour faire des prédictions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Outils maîtrisés
    st.markdown("<h4 style='color: #F18F01; text-align: center; margin: 2rem 0;'>🛠️ Outils maîtrisés</h4>", unsafe_allow_html=True)
    
    tools_col1, tools_col2, tools_col3 = st.columns(3)
    
    tools = [
        ("Suite Microsoft", "💼"),
        ("SQL", "🗃️"),
        ("R Studio", "📈"),
        ("SAS", "📊"),
        ("Python", "🐍"),
        ("Power BI", "📊")
    ]
    
    for i, (tool, emoji) in enumerate(tools):
        col = [tools_col1, tools_col2, tools_col3][i % 3]
        with col:
            st.markdown(f"""
            <div class='contact-item'>
                <h4>{emoji}</h4>
                <p><strong>{tool}</strong></p>
            </div>
            """, unsafe_allow_html=True)

# Section Réalisations
elif section == "🚀 Réalisations":
    st.markdown("<h2 class='section-header'>🚀 Réalisations</h2>", unsafe_allow_html=True)
    
    # Projets universitaires
    st.markdown("<h3 class='subsection-header'>🎓 Projets universitaires</h3>", unsafe_allow_html=True)
    
    projets = [
        {
            "titre": "📋 Mise en place d'une enquête",
            "description": """Ce projet avait pour but d'élaborer de A à Z une enquête à destination des étudiants et personnels de l'IUT. 
            Il portait sur la place de l'IA dans les études supérieures. C'était un travail par groupe de 4.
            
            Pour ce faire nous avons d'abord créé notre questionnaire sur la plateforme LimeSurvey. Par manque de réponses nous avons dû faire un travail de terrain et aller auprès de nos potentiels répondants pour solliciter des réponses.
            
            Nous avons ensuite fait un gros travail de nettoyage des données, sur Excel, et nous avons gardé environ 600 réponses et sélectionné certaines questions. Notre problématique était la suivante : "Comment les membres de l'IUT perçoivent l'utilisation de l'IA dans l'enseignement supérieur ?"
            
            Nous avons ensuite fait nos différentes analyses et élaboré un reporting sur PowerPoint que nous avons par la suite présenté."""
        },
        {
            "titre": "📊 Tableau de bord",
            "description": """Un concours national entre tous les BUT1 SD de France était organisé dans le but d'un projet noté. Une entreprise, dans notre cas Météo France, nous fournissait des données ainsi qu'une problématique et l'objectif était de créer un tableau de bord sur Power BI pour y répondre.
            
            Nous avions une journée entière pour réaliser ce projet. Avec mon groupe nous sommes partis sur la question "Est-ce qu'il pleut tout le temps en Bretagne ?". Le travail de nettoyage sur Excel a été complexe, nous sommes ensuite passés sur Power BI afin de mettre en place notre tableau de bord.
            
            A la fin de la journée, nous avons élu le meilleur de la promo afin qu'il aille en finale nationale. C'est mon groupe qui a gagné au sein de l'IUT mais nous n'avons malheureusement pas gagné le concours."""
        },
        {
            "titre": "📈 Modèle de régression linéaire",
            "description": """Ce projet d'analyse avait pour objectif de comparer la taille en fonction de l'âge d'enfants provenant de deux pays différents. Ce travail était à faire par 2 et il nous a été attribué la Polynésie Française et Sainte Lucie.
            
            Nous avons eu les données en CSV et avons dû les traiter sur R Studio. Il nous a fallu faire une analyse descriptive des données puis un ajustement polynomial des courbes de croissance. Tout cela dans le but de comparer les filles, les garçons, les classes d'âge et les deux pays.
            
            Tout a été réalisé sur R Studio, le rendu était un rapport écrit des résultats qui reprenait notre code avec des explications ainsi que de multiples graphiques. Il a fallu également faire une conclusion en anglais."""
        }
    ]
    
    for projet in projets:
        st.markdown(f"""
        <div class='project-card'>
            <h4>{projet['titre']}</h4>
            <p>{projet['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Alternance
    st.markdown("<h3 class='subsection-header'>💼 Alternance</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("Z:/BUT3/E-portfolio_Camille_Franceschin/E-portfolio/Images/intersport.png", width=300)
    
    with col2:
        st.markdown("""
        Je suis en alternance depuis **septembre 2024** et jusqu'à **septembre 2026** dans l'entreprise **Intersport** 
        au pôle Data du service Marketing Client. Intersport est une entreprise de distribution d'articles de sport, 
        possédant plus de 900 magasins principalement en France.
        
        L'équipe de la Data est composée de **6 personnes** (dont moi !) et a pour but d'avoir une connaissance des différents profils clients fidélisés ainsi que de suivre et analyser les opérations marketing se déroulant tout au long de l'année. De plus, diverses enquêtes sont également mises en place par notre équipe.
        """)
    
    st.markdown("<h4 style='color: #F18F01; margin-top: 2rem;'>🎯 Mes missions</h4>", unsafe_allow_html=True)
    
    missions = [
        "S'assurer chaque jour que les données de la veille ont bien été chargées sur nos serveurs, et le cas échéant les récupérer (SAS)",
        "Créer des suivis quotidiens pour les opérations marketing puis en faire un bilan sous forme de reporting à la fin de l'opération (SAS, EXCEL, POWERPOINT)",
        "Faire des analyses sur la base clients (SAS, EXCEL, POWERPOINT)",
        "Présenter les résultats",
        "Répondre à des demandes spécifiques concernant la base clients"
    ]
    
    for mission in missions:
        st.markdown(f"• {mission}")

# Section Contacts et liens
elif section == "📞 Contacts et liens":
    st.markdown("<h2 class='section-header'>📞 Contacts et liens</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='contact-item'>
            <h4>✉️ Contact</h4>
            <p>Vous pouvez me contacter ici :</p>
            <p><strong>camillefr2@gmail.com</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📧 Envoyer un email", key="email_btn"):
            st.markdown("[Cliquez ici pour envoyer un email](mailto:camillefr2@gmail.com)")
    
    with col2:
        st.markdown("""
        <div class='contact-item'>
            <h4>📄 CV</h4>
            <p>Téléchargez mon CV :</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Bouton de téléchargement du CV
        create_download_button("Z:/BUT3/E-portfolio_Camille_Franceschin/E-portfolio/Images/CV.pdf", "CV_Camille_Franceschin.pdf", "📥 Télécharger CV")
    
    with col3:
        st.markdown("""
        <div class='contact-item'>
            <h4>💼 LinkedIn</h4>
            <p>Retrouvez-moi sur LinkedIn :</p>
            <p><em>(Profil en cours de création)</em></p>
        </div>
        """, unsafe_allow_html=True)



# Section RATP
if section == "🚆 RATP":
    st.markdown("<h1 class='main-header'>🖥️ Exercice Python & Streamlit</h1>", unsafe_allow_html=True)

    df=pd.read_csv("emplacement-des-gares-idf.csv", sep=";")
    st.write ("Aperçu du jeu de données :")
    st.write ("Le jeu de données porte sur toutes les stations du réseau IDF Mobilités")
    st.write (df.head(5))
    st.write("")
    st.write("")
    st.write("")

    counts = df['idf'].value_counts()

    # Création du camembert
    fig = px.pie(
        values=counts.values,
        names=["Île-de-France", "Hors Île-de-France"],
        color=["Île-de-France", "Hors Île-de-France"],  # pour gérer les couleurs
        color_discrete_map={
            "Île-de-France": "#1f77b4",       # bleu
            "Hors Île-de-France": "#ff7f0e"   # orange
        }
    )

    # Options de mise en forme
    fig.update_traces(
        textinfo='label+percent',
        textfont_size=12  # taille du texte
    )

    fig.update_layout(
        width=400,   # largeur du graphique
        height=400,  # hauteur du graphique
        margin=dict(t=20, b=20, l=20, r=20)
    )

    # Affichage dans Streamlit
    st.plotly_chart(fig)

