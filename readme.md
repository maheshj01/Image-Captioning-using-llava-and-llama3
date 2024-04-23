### Image Caption Generator

This project uses LLaVA (Large Language-and-Vision Assistant) , an end-to-end trained large multimodal model that connects a vision encoder and LLM for general-purpose visual and language understanding.

llava generates the description of the image and the description is the fed to llama3 to generate the caption of the image.

### Installation

1. Clone the repo

   ```sh
   git clone <URL>
   ```

2. Install requirements

   ```sh
   pip install -r requirements.txt
   ```

3. Download the llms using the following command

   ```sh
   ollama pull llama3
   ollama pull llava
   ```

4. Start the local ollama server

   ```sh
   ollama serve
   ```

5. Run the code

   ```sh
   streamlit run app.py
   ```
