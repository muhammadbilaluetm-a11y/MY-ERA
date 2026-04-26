import streamlit as st
import google.generativeai as genai

# Page Setup
st.set_page_config(page_title="MY-ERA AI", page_icon="🌐")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { background-color: #007bff; color: white; border-radius: 8px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 MY-ERA: The Global AI")
st.write("Dunya ka har kaam, ab chotkion mein!")

with st.sidebar:
    st.header("Setup")
    # Yahan humne Gemini Key maangi hai
    gemini_key = st.text_input("Apni Gemini API Key yahan dalein", type="password")

if gemini_key:
    try:
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-pro')

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Hukum karein..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Key sahi nahi hai ya koi masla hai: {e}")
else:
    st.warning("Please enter your Gemini API Key in the sidebar to start.")
