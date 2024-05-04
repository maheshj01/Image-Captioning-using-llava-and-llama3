import streamlit as st
from config import Config
from utils.llm_utils import generate_response, stream_parser

page_title = Config.code_title


st.set_page_config(
    page_title=page_title,
    initial_sidebar_state='expanded'
)

CURRENT_THEME = "dark"
IS_DARK_THEME = True

st.title(page_title)
st.markdown("Welcome to Codellama, This app uses codellama to generate code for you"  )

codellama_model = Config.ollama_models[2]

if chat_input:= st.chat_input("Ask me anything related to Code. I am a Code Llama"):
    # if uploaded_file is None:
        with st.status("Thinking..."):
            stream = generate_response(codellama_model, chat_input)
            response = stream_parser(stream)
            st.write(response)
        st.stop()

