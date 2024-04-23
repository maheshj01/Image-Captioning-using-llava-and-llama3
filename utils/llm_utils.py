from config import Config
from utils.image_utils import get_image_bytes
from ollama import generate

system_prompt = Config.default_prompt

def generate_image_desc(image_file, model, user_prompt):
    image_bytes = get_image_bytes(image_file)
    stream = generate(model=model,prompt=user_prompt, images=[image_bytes], stream=True)
    return stream

# handles stream response back from LLM
def stream_parser(stream):
    for data in stream:
        if data.get('response'):
            yield data['response']
        if data.get('done'):
            break