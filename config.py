class Config:
    page_title = "AI Image Caption Generator"
    ollama_models = ['llama3:latest', 'llava:latest']
    default_model = 'llava:latest'
    default_prompt = 'You are a AI Image Caption Generator chatbot, built to generate image captions. You can ask me to generate image captions for you. You can also answer questions about the image.'