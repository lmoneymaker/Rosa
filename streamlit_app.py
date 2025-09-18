import streamlit as st

# Function to load and inject CSS remains the same
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
    st.markdown("<p>This is a simulator to practice conversations with Rosa, a client in crisis.</p>", unsafe_allow_html=True)

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