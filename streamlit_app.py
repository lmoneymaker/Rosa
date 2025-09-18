import streamlit as st
# I've commented out the OpenAI import since we are not using it.
# from openai import OpenAI

# --- Start of New Code Block ---
# This is our stand-in for the real AI model.
def get_rosa_response_placeholder(prompt: str) -> str:
    """
    Takes a user prompt, prints it for debugging, and returns a
    fixed, hard-coded response.
    """
    print(f"Placeholder received prompt: '{prompt}'") # Useful for checking your work in the terminal
    
    # This is the hard-coded response that will be displayed in the chat UI
    return "This is a placeholder response from Rosa. The real model is still training."
# --- End of New Code Block ---


# Show title and description.

st.markdown("<h1 style='text-align: center; font-family: Futura, sans-serif; font-weight: 500; font-size: 48px;'>Rosa</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>This is a simulator for social workers in training to practice conversations with Rosa, a client in crisis.</p>", unsafe_allow_html=True)

# --- I have removed the section that asks for the OpenAI API Key ---


# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("What do you want to say to Rosa?"):

    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- I have replaced the OpenAI API call with our placeholder function ---
    # Generate a response using the placeholder function.
    with st.chat_message("assistant"):
        response = get_rosa_response_placeholder(prompt)
        st.markdown(response) # Use st.markdown to display the simple text response
    
    # Store the placeholder's response in session state.
    st.session_state.messages.append({"role": "assistant", "content": response})