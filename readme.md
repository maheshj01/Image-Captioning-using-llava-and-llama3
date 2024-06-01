### Image Caption Generator

This project uses LLaVA (Large Language-and-Vision Assistant) , an end-to-end trained large multimodal model that connects a vision encoder and LLM for general-purpose visual and language understanding.

llava generates the description of the image and the description is the fed to llama3 to generate the caption of the image.

### Installation

1. Clone the repo

   ```sh
   git clone <URL>
   ```

2. Activate a virtual env
   ```
   python3 -m venv cenv
   source cenv/bin/activate
   ```

3. Install requirements

   ```sh
   pip install -r requirements.txt
   ```

4. Download the llms using the following command

   ```sh
   ollama pull llama3
   ollama pull llava
   ```

5. Start the local ollama server

   ```sh
   ollama serve
   ```

6. Run the backend server

   ```sh
   uvicorn main:app --reload
   ```

7. Run the code

   ```sh
   streamlit run app.py
   ```
