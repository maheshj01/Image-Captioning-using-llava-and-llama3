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

3. Run the code
   ```sh
   streamlit run app.py
   ```
