import streamlit as st
from config import Config
from utils.llm_utils import generate_image_desc, stream_parser
# from utils.image_utils import create_temp_file

page_title = Config.page_title

st.set_page_config(
    page_title=page_title,
    initial_sidebar_state='expanded'
)

CURRENT_THEME = "dark"
IS_DARK_THEME = True

st.title(page_title)
st.markdown("Welcome to Ai Caption Bot! This app uses llava with llama3 to generate caption for your images."  )

uploaded_file = st.file_uploader("Choose a image to Upload", type=["jpg", "jpeg", "png"])

# with st.sidebar:
#     st.markdown("## Settings")
#     image_model = st.selectbox("Select Image Model", Config.ollama_models)
llava_model = Config.ollama_models[1]
llama_model = Config.ollama_models[0]

if chat_input:= st.chat_input("Ask Questions about the Image"):
    if uploaded_file is None:
        st.error("Please upload an image file.")
        st.stop()

# caption_prompt = st.text_area("Caption Prompt", "Please generate a caption for this image.")
if uploaded_file is None:
    st.stop()
with st.status("Generating Image Caption..."):
    stream = generate_image_desc(uploaded_file, llava_model, chat_input)
    response = stream_parser(stream)
    st.write(response)
    # caption_stream = generate_image_desc(uploaded_file, llama_model, caption_prompt)
    # caption_response = stream_parser(caption_stream)