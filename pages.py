import streamlit as st

def show_intro_page():
    st.title("Questionnaire TSA")

    st.subheader("Madame, Monsieur,")
    st.write("""
    Nous vous remercions d’accepter de participer à l'étude exploratoire que nous menons sur les troubles du spectre autistique (TSA). Cette étude vise à enrichir les outils disponibles pour les professionnels de santé, faciliter l'accès aux soins et le dépistage pour les individus TSA, notamment ceux hésitants à s'engager dans un processus de diagnostic qui peut souvent se retrouver chronophage et complexe.
    """)

    st.subheader("I) Objectifs :")
    st.write("""
    L'étude a pour objectifs principaux d'augmenter le nombre d'outils de dépistage accessibles gratuitement aux professionnels de santé, d'améliorer l'accès aux soins pour les personnes TSA, et de faciliter leur dépistage précoce. Cela contribuera à une meilleure compréhension, reconnaissance, et prise en charge de ces patients.
    """)

    st.subheader("II) Bénéfices :")
    st.write("""
    Cette étude apportera des bénéfices à deux niveaux:
    - Au niveau populationnel : améliorer la qualité de vie et l'insertion professionnelle des personnes TSA par une meilleure compréhension et prise en charge de leurs difficultés.
    - Au niveau individuel : chaque participant pourra recevoir un rapport personnalisé sur le questionnaire qu'il aura complété dès la fin de l'étude.
    """)

    st.subheader("III) Risques :")
    st.write("Il n’y a aucun risque connu associé à votre participation à cette étude.")

    st.subheader("IV) Déroulement de l'étude :")
    st.write("""
    L'étude consiste en la complétion de 5 sections de questions sous forme de Google Forms, chacune prenant environ 4 minutes. Vous pouvez les remplir à votre rythme, dans un environnement confortable et sans contrainte de temps.
    """)

    st.subheader("V) Données recueillies et confidentialité :")
    st.write("""
    Toutes les données collectées seront traitées dans le respect de votre vie privée et de votre anonymat. Aucune information permettant de vous identifier ne sera partagée. En cas de questions ou de préoccupations concernant vos données, vous pouvez nous contacter directement.
    """)

    st.subheader("VI) Restitution des résultats de la recherche :")
    st.write("""
    À l'issue de l'étude, les résultats seront communiqués de manière écrite à tous les participants. Ces informations permettront de mieux comprendre les besoins spécifiques des personnes TSA et d'améliorer les outils de dépistage et de prise en charge.
    """)

    st.subheader("VII) Volontariat et droit de retrait :")
    st.write("""
    Votre participation à cette étude est entièrement volontaire. Vous êtes libre de vous retirer à tout moment sans avoir à fournir de justification. Cette décision n'aura aucune conséquence sur votre accès aux soins ou sur vos relations avec les professionnels de santé.
    """)

    st.write("Nous vous remercions pour votre intérêt et votre participation à ce projet de recherche.")

    if st.button("Commencer le questionnaire"):
        st.session_state['current_page'] = 'Page 1'


def show_page_one():
    st.subheader("Consentement")
    st.write("Je reconnais que :")

    consents = {
        "Je participe volontairement à cette recherche": ["Oui", "Non"],
        "Je peux cesser ma participation à tout moment sans avoir à donner d'explication": ["Oui", "Non"],
        "Toutes les informations que je fournirais seront confidentielles et mon identité ne sera jamais divulguée": ["Oui", "Non"],
        "J'autorise la conservation et l'utilisation de ces données confidentielles dans le cadre de la recherche scientifique en psychologie": ["Oui", "Non"]
    }

    user_inputs = st.session_state.get('user_inputs', {})

    with st.form(key='form1'):
        for consent, options in consents.items():
            user_inputs[consent] = st.radio(consent, options, key=consent)

        st.subheader("Déclaration sur l'honneur")
        honor_statement = st.radio(
            "Je certifie sur l'honneur que:",
            [
                "J'ai reçu un diagnostic de troubles du spectre autistique par un professionnel certifié",
                "Je n'ai jamais reçu de diagnostic de troubles du spectre autistique par un professionnel certifié"
            ],
            key="honor_statement"
        )
        user_inputs["honor_statement"] = honor_statement

        if st.form_submit_button("Page suivante"):
            st.session_state['user_inputs'] = user_inputs
            st.session_state['current_page'] = 'Page 2'


def show_page_two():
    st.subheader("Caractéristiques démographiques")

    user_inputs = st.session_state.get('user_inputs', {})

    with st.form(key='form2'):
        sex = st.radio("Votre sexe biologique est :", ('Masculin', 'Féminin'), key="sex")
        user_inputs["sex"] = sex

        gender = st.slider("Votre genre est :", 1, 6, 3, format='%d', key="gender")
        user_inputs["gender"] = gender

        age = st.number_input("Votre âge :", min_value=18, max_value=100, value=18, step=1, key="age")
        user_inputs["age"] = age

        city = st.text_input("Dans quelle ville habitez-vous ?", key="city")
        user_inputs["city"] = city

        department = st.text_input("Dans quel département habitez-vous (en chiffres format XX) ?", key="department")
        user_inputs["department"] = department

        country = st.text_input("Dans quel pays habitez-vous ?", value="France", key="country")
        user_inputs["country"] = country

        education_level = st.selectbox(
            "Votre niveau d'étude ?",
            ("CAP/BEP", "Baccalauréat professionnel", "Baccalauréat général", "Bac+2 (DUT/BTS)", "Bac+3 (Licence)", "Bac+5 (Master)", "Bac > +7 (Doctorat, écoles supérieures)"),
            key="education_level"
        )
        user_inputs["education_level"] = education_level

        if st.form_submit_button("Page suivante"):
            st.session_state['user_inputs'] = user_inputs
            st.session_state['current_page'] = 'Page 3'


def show_page_three():
    st.subheader("Le questionnaire ")

    st.write("""
    Veuillez évaluer chaque affirmation en fonction de votre propre expérience.
    Utilisez l'échelle de 1 à 6 où:
    - 1 signifie "Ne me ressemble pas du tout"
    - 6 signifie "Me ressemble complètement"
    """)

    questions = [
        "Le contact visuel avec autrui m'est inconfortable, et je trouve difficile de le maintenir ou d'interpréter son sens dans une conversation",
        "Je préfère souvent passer du temps seul(e) avec dans mes centres d’intérêts plutôt qu'avec des personnes.",
        "Je suis souvent indifférent(e) ou inattentif(ve) aux conversations ou activités qui ne concernent pas mes propres intérêts",
        "Je n'éprouve pas de plaisir à participer à des activités de groupe, et je préfère souvent rester seul(e).",
        "J'ai du mal à percevoir les subtilités dans les interactions sociales, comme l'ironie ou le sarcasme, ce qui rend la conversation confuse pour moi.",
        "Je me sens souvent différent(e) ou isolé(e) à cause de mes intérêts spécifiques.",
        "Le contact physique, même léger, peut être extrêmement inconfortable ou désagréable pour moi.",
        "Il m'est difficile d'interpréter les expressions faciales des autres, ce qui rend souvent les conversations mal comprises pour moi.",
        "J'ai des habitudes spécifiques pour organiser mes affaires, et je me sens très perturbé(e) si ces habitudes sont interrompues ou changées par quelqu'un d'autre.",
        "Je trouve difficile de comprendre les règles non dites des interactions sociales, comme savoir quand c'est mon tour de parler ou comment réagir aux plaisanteries.",
        "Il y a certaines textures que je ne peux absolument pas toucher sous peine de ressentir une forte gêne.",
        "Je me sens obligé(e) de répéter certaines actions physiques, comme aligner des objets ou tourner des éléments de manière spécifique, même quand cela n'est pas nécessaire",
        "Je peine à me détourner des sujets qui me passionnent pour parler d'autres choses.",
        "Même quand c'est mon tour de parler, j’ai des difficultés à trouver les bons mots pour exprimer ce que je ressens.",
        "Je peine à comprendre le langage corporel des autres, comme les gestes ou les postures, ce qui peut mener à des malentendus dans les interactions sociales.",
        "J'ai des routines spécifiques que je dois suivre, et cela me perturbe si je ne peux pas les réaliser",
        "J'ai tendance à éviter les interactions sociales parce que je ne sais pas comment partager mes expériences avec les autres.",
        "Je trouve très difficile de m'adapter à une nouvelle activité ou un changement dans mon emploi du temps",
        "Lorsque je suis stressé(e) ou anxieux(se), j'ai tendance à répéter les mêmes mots ou phrases, même si cela n'est pas pertinent dans la conversation.",
        "Lorsque quelqu'un exprime ses émotions, je me sens déconnecté(e) et incertain(e) de la façon de montrer de l'empathie.",
        "Je ne réagis pas de la même manière que les autres aux variations de température, comme le froid ou la chaleur extrême.",
        "Je peux rester fixé(e) pendant de longues périodes sur des objets en mouvement ou des jeux de lumière.",
        "Les situations où je dois offrir du soutien émotionnel à quelqu'un me rendent très inconfortable.",
        "La nécessité de changer mon itinéraire habituel me crée une sensation inconfortable.",
        "Je porte souvent des écouteurs, casques, ou des bouchons d'oreilles pour me protéger des bruits environnants qui me perturbent.",
        "Je passe la majorité de mon temps libre à me concentrer sur certaines activités spécifique.",
        "Je ne me rends pas compte quand il est approprié de partager des anecdotes personnelles ou de répondre aux histoires des autres.",
        "Je me sens contrarié(e) quand les choses ne se passent pas exactement comme je l'avais prévu.",
        "Je suis très attaché(e) à certains objets, au point de me sentir très mal à l’idée même de les remplacer.",
        "J'ai tendance à répéter des phrases ou des sons entendus dans des films, des émissions de télévision ou des conversations, même en l'absence de contexte approprié.",
        "J'ai du mal à interpréter les sentiments ou les intentions des autres, ce qui rend les relations personnelles compliquées pour moi.",
        "Je ne comprends pas toujours pourquoi les gens agissent d'une certaine manière dans les interactions sociales, ce qui me laisse confus(e) ou frustré(e).",
        "Je me sens obligé(e) de compter ou de mesurer des choses sans raison pratique, comme le nombre de marches d'un escalier.",
        "J'ai des habitudes verbales spécifiques, comme répéter la dernière phrase de mon interlocuteur ou utiliser des phrases clichées, que j'utilise fréquemment dans les conversations",
        "Je répète involontairement certains mouvements ou gestes, même en étant conscient(e) qu'ils ne sont pas essentiels ou bien acceptés dans les interactions sociales.",
        "Certains parfums ou odeurs peuvent me rendre très mal à l'aise",
        "Il m'est difficile de saisir l'ambiance générale dans une pièce ou un groupe sans que quelqu'un ne l'exprime explicitement.",
        "Je me sens mal à l'aise dans les interactions sociales car je crains de ne pas réagir correctement aux émotions des autres.",
        "Il m'arrive de sourire ou de rire à des moments inappropriés pendant une conversation, ce qui peut être mal interprété.",
        "Je suis naturellement attiré(e) par certains sujets ou activités spécifiques, et les autres me laissent indifférent(e).",
        "Je trouve épuisant d'essayer de maintenir une conversation quand l'autre personne ne parle pas de sujets qui m'intéressent directement.",
        "Je peux facilement passer des heures à me concentrer sur mes propres activités, en négligeant tout le reste",
        "Je me sens rapidement stressé(e) dans des environnements bruyants ou chaotiques, comme des centres commerciaux",
        "Je me sens très mal à l'aise à l'idée de prêter ou de laisser quelqu'un d'autre utiliser mes objets personnels.",
        "Je suis habitué(e) à manger les mêmes aliments, suivant un schéma précis, et je trouve difficile d'essayer de nouveaux plats.",
        "Je me sens indifférent(e) à l'idée de me faire de nouveaux amis ou de maintenir des relations avec les personnes que je connais déjà.",
        "Lorsque je suis en groupe, je me sens souvent perdu(e) et j'ai du mal à suivre les conversations ou les activités communes.",
        "Je ne comprends pas pourquoi les gens s'attendent à ce que je devine ce qu'ils ressentent sans qu'ils le disent clairement.",
        "Je ne réagis pas toujours de manière appropriée aux gestes des autres, ce qui peut rendre mes réactions inattendues ou inappropriées dans certaines situations.",
        "Je suis très sélectif(ve) concernant les aliments que je mange, en raison de leur texture ou de leur goût.",
        "Je ressens le besoin de chercher du réconfort chez les autres quand je suis contrarié(e) ou triste.",
        "Je répète souvent des mouvements corporels, comme me balancer, tapoter ou agiter mes mains, surtout dans des situations où je me sens inconfortable.",
        "Je me sens mal à l'aise ou confus(e) lorsque les autres utilisent des expressions non verbales, comme lever les yeux au ciel ou croiser les bras.",
        "Lorsque les autres parlent de choses qui ne m'intéressent pas, je me sens détaché(e) et j'ai tendance à me perdre dans mes propres pensées.",
        "Il m'est fréquemment difficile de déterminer quand et comment réagir avec des gestes comme les sourires ou les hochements de tête pendant les échanges sociaux.",
        "Les modifications imprévues de mon environnement habituel me perturbent beaucoup."
    ]

    user_inputs = st.session_state.get('user_inputs', {})
    responses = {}

    with st.form(key='form3'):
        for i, question in enumerate(questions):
            response = st.slider(
                question,
                min_value=1,
                max_value=6,
                value=3,
                key=f"question_{i}"
            )
            responses[question] = response

        user_inputs.update(responses)

        st.write("Soumettre le questionnaire pour envoyer les réponses.")

        if st.form_submit_button("Soumettre le questionnaire"):
            st.session_state['user_inputs'] = user_inputs
            st.session_state['current_page'] = 'End'
