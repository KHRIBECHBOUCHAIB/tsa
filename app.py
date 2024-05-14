import streamlit as st
import pymongo
import hmac
import hashlib
import base64
from pages import show_intro_page, show_page_one, show_page_two, show_page_three

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Initialize connection to MongoDB
def init_connection():
    client = pymongo.MongoClient(st.secrets["mongo_uri"])
    return client

client = init_connection()
db = client[st.secrets["mongo"]["database_name"]]

# Check the password and store the state in session if correct
def check_password():
    if 'password_verified' not in st.session_state or not st.session_state['password_verified']:
        with st.sidebar.form(key='Password_form'):
            password_input = st.text_input("Entrez votre mot de passe :", type="password", placeholder="Tapez votre mot de passe ici")
            submit_button = st.form_submit_button("Soumettre")
            if submit_button and password_input:
                hashed_input = hmac.new(
                    key=st.secrets["secret_key"].encode(),
                    msg=password_input.encode(),
                    digestmod=hashlib.sha256
                ).hexdigest()
                if hmac.compare_digest(hashed_input, st.secrets["password_hash"]):
                    st.session_state['password_verified'] = True
                else:
                    st.error("Mot de passe incorrect. Veuillez réessayer.")
                    return False
        st.sidebar.image("images/logo.png", width=300)
    return st.session_state.get('password_verified', False)

# Function to save user inputs to the database
def save_data_to_db(user_inputs):
    db["tsa_questionnaire_responses"].insert_one(user_inputs)

# Function to center an image
def centered_image(image_path, width):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{encoded_string}" width="{width}px">
        </div>
        """,
        unsafe_allow_html=True,
    )

# Application main function
def main():
    if not check_password():
        st.stop()

    centered_image("images/logo.jpg", 150)  # Display logo at the beginning of each page

    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'Introduction'

    if 'user_inputs' not in st.session_state:
        st.session_state['user_inputs'] = {}

    page = st.session_state['current_page']

    if page == 'Introduction':
        show_intro_page()
    elif page == 'Page 1':
        show_page_one()
    elif page == 'Page 2':
        show_page_two()
    elif page == 'Page 3':
        show_page_three()
    elif page == 'End':
        st.success("Vos réponses ont été enregistrées avec succès. Merci pour votre participation !")
        save_data_to_db(st.session_state['user_inputs'])

    centered_image("images/logo.jpg", 150)  # Display logo at the end of each page

if __name__ == "__main__":
    main()
