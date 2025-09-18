import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel
from google.oauth2 import service_account

# --- Configuration ---
# !!! REPLACE WITH YOUR VALUES !!!
PROJECT_ID = "Rosa"
LOCATION = "us-central1"
MODEL_ID = 2843925308149596160 # Paste the ID you copied from Vertex AI
KEY_FILE_PATH = "complete-will-472500-j3-fd7559f7c69e.json" # The name of your service account key file
# ---------------------

# --- Authentication and Model Loading ---
# This part connects to Google Cloud and loads your specific model
try:
    credentials = service_account.Credentials.from_service_account_file(KEY_FILE_PATH)
    vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)
    tuned_model = GenerativeModel(MODEL_ID)
except Exception as e:
    st.error(f"Error initializing Vertex AI. Please check your configuration and key file. Details: {e}")
    st.stop()
# ----------------------------------------

# Load the CSS
local_css("style.css")

# Placeholder function remains the same
def get_rosa_response_placeholder(prompt: str) -> str:
    """
    Takes a user prompt and returns a fixed, hard-coded response.
    """
    print(f"Placeholder received prompt: '{prompt}'")
    return "This is a placeholder response from Rosa. The real model is still training."

# --- New Feature: Sidebar with a button to clear the chat ---
if st.sidebar.button("Start New Session"):
    st.session_state.messages = []

# --- Start of New Layout Structure ---
# The main container will hold the title, subtext, and chat history
with st.container():
    # We apply our custom CSS class to this container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # All UI elements that should be centered go inside this container
    st.markdown("<h1>ROSA</h1>", unsafe_allow_html=True)
    st.markdown("<p>This is a simulator for social workers to practice conversations with Rosa, a virtual client in crisis.</p>", unsafe_allow_html=True)

    # Initialize and display chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # We close the custom CSS div tag here
    st.markdown('</div>', unsafe_allow_html=True)
# --- End of New Layout Structure ---


# The chat input is placed OUTSIDE the main container to appear below it
if prompt := st.chat_input("What do you want to say to Rosa?"):
    # Store and display the current prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get and store the placeholder's response
    response = get_rosa_response_placeholder(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Rerun the app to display the new messages immediately
    st.rerun()