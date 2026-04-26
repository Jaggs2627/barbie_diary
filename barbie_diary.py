import streamlit as st
from cryptography.fernet import Fernet
import base64

# 1. Barbiecore Styling
st.set_page_config(page_title="Barbie's Secret Journal", page_icon="💖")

st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F5; /* Lavender Blush */
    }
    h1, h2, h3 {
        color: #FF1493 !important; /* Deep Pink */
        font-family: 'Georgia', serif;
    }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 50px;
        border: none;
        box-shadow: 0px 4px 10px rgba(255, 105, 180, 0.3);
    }
    .stTabs [data-baseweb="tab"] {
        color: #FF69B4;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💖 BARBIE'S SECRET CIPHER 💖")
st.subheader("Cyber Sparkle Letter")

# 2. Secret Key 
def generate_key(secret_word):
    key = base64.urlsafe_b64encode(secret_word.ljust(32)[:32].encode())
    return key

user_key = generate_key("J262427")
cipher = Fernet(user_key)

# 3. UI Tabs
tab1, tab2 = st.tabs(["✨ HIDE A SECRET", "🔓 REVEAL THE MAGIC"])

with tab1:
    st.write("Write something sweet to turn it into a glittery code:")
    secret_text = st.text_area("Your Message:", placeholder="Hey Barbie! Let's watch a movie!")
    if st.button("Sparkle-ify Message"):
        if secret_text:
            encrypted_text = cipher.encrypt(secret_text.encode()).decode()
            st.success("Your secret is safe in the Dreamhouse! Send this code:")
            st.code(encrypted_text)
        else:
            st.warning("A Barbie always has something to say!")

with tab2:
    st.write("Paste the glittery jumbled code here to read the secret:")
    incoming_web = st.text_input("Enter Secret Code:")
    if st.button("Unlock the Journal"):
        try:
            decrypted_text = cipher.decrypt(incoming_web.encode()).decode()
            st.snow() # Falling hearts/snow effec
            st.toast('Message Decrypted!', icon='✨')
        except:
            st.error("Oops! That's not the right key for this journal.")

st.markdown("---")
st.write("🎀 *Stay fabulous and stay secure.*")
