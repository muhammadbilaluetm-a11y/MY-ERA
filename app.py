import streamlit as st
from groq import Groq

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
    groq_api_key = st.text_input("Apni Groq API Key yahan dalein", type="password")
    st.info("MY-ERA aapka personal super assistant.")

if groq_api_key:
    try:
        client = Groq(api_key=groq_api_key)
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
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[
                        {"role": "system", "content": "You are MY-ERA AI, a super intelligent global assistant. Solve any task perfectly."},
                        *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                    ]
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("Shuru karne ke liye sidebar mein Groq API Key enter karein.")
