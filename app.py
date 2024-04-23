import streamlit as st
from config import Config
from utils.llm_utils import generate_image_desc, stream_parser, generate_caption
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
        with st.status("Thinking..."):
            stream = generate_caption(llama_model, chat_input)
            response = stream_parser(stream)
            st.write(response)
        st.stop()

if uploaded_file is None:
    st.stop()
describe_prompt = "What do you see in this image?"
reading = True
response_str =''

with st.status("Reading the Image..."):
    stream = generate_image_desc(uploaded_file, llava_model, describe_prompt)
    response = stream_parser(stream)
    st.write(response)
    response_str = ''.join(response)

if(len(response_str) > 0):
    reading = False

print(response_str)
with st.status("Generating Caption..."):
    caption_prompt = "Please generate a caption for this image using this description:" + response_str
    caption_stream = generate_caption(llama_model, caption_prompt)
    caption_response = stream_parser(caption_stream)
    st.write(caption_response)
